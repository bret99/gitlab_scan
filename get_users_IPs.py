import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import json
import time
from access_tokens import gitlab_access_token, gitlab_server_address, abuseipdb_token, ipgeolocation_token

users_IDs = []
users_IPs = []
items_to_print = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}
geolocation_services = ["abuseipdb", "ipgeolocation"]
status_list = ["admins", "active", "blocked", "external", "without_projects", "all"]

def get_users_IPs():
    try:
        if gitlab_access_token == "":
            print("\nOne should write correct value to \033[1;95mgitlab_access_token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
            sys.exit()
        elif "http" not in gitlab_server_address:
            print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
            sys.exit()
        users_status = input("Enter users status (\033[1;95madmins\033[1;00m, \033[1;92mactive\033[1;00m, \033[1;91mblocked\033[1;00m, \033[;93mexternal\033[1;00m, \033[;90mwithout_projects\033[1;00m, all): ")
        if users_status not in status_list:
            sys.exit("\033[1;93mWrong input!\033[1;00m")
        geolocation_choose = input("Choose IP to geolocation reverse service (\033[1;95mabuseipdb\033[1;00m, \033[1;96mipgeolocation\033[1;00m): ")
        if geolocation_choose == "abuseipdb":
            if abuseipdb_token == "":
                print("\nOne should write correct value to \033[1;95mabuseipdb_token \033[1;00min \033[1;95maccess_token.py \033[1;00mto get IPs geolocations!")
            get_users_IPs_abuseipdb(users_status, geolocation_choose=geolocation_choose)
        elif geolocation_choose == "ipgeolocation":
            if ipgeolocation_token == "":
                print("\nOne should write correct value to \033[1;96mipgeolocation_token \033[1;00min \033[1;95maccess_token.py \033[1;00mto get IPs geolocations!")
            get_users_IPs_ipgeolocation(users_status, geolocation_choose=geolocation_choose)
        else:
            sys.exit("\033[1;93mWrong input!\033[1;00m")
        print("\n{0} users amount is \033[1;94m{1}\033[1;00m".format(users_status, len(set(users_IDs))))
        print("\nOne can find results in \033[1;95m{}/reports/users_IPs_info.txt\033[1;00m\n".format(os.getcwd()))

    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
        users_IPs_output(users_status, items_to_print, geolocation_choose)
    except KeyboardInterrupt:
        print("\033[1;93m\nResults not saved!\033[1;00m")

def get_users_IPs_ipgeolocation(users_status, geolocation_choose):
    if users_status == "all":
        print("\033[1;90m\nCollecting data...\033[1;00m")
        print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
        page_counter = 0
        while 1:
            target_users = requests.get("{0}/api/v4/users?per_page=100&page={1}".format(gitlab_server_address, page_counter), headers=headers)
            users = target_users.json()
            if len(users) == 0:
                break
            item_counter = 0
            for item in users:
                try:
                    item = str(users[item_counter]["id"])
                    users_IDs.append(item)
                except KeyError:
                    users_IDs.append(item)
                item_counter += 1
            time.sleep(0.1)
            page_counter += 1

        for item in set(users_IDs):
            try:
                target_IPs = requests.get("{0}/api/v4/users/{1}".format(gitlab_server_address, item), headers=headers)
                IPs = target_IPs.json()
                user_current_sign_in_ip = IPs["current_sign_in_ip"]
                response = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey={0}&ip={1}".format(ipgeolocation_token, user_current_sign_in_ip))
                decodedResponse = response.json()
                item_to_list = ("user_id: {0} => {1} [country: {2} city: {3} latitude: {4} longitude: {5}]".format(item, IPs["current_sign_in_ip"], decodedResponse['country_code2'], decodedResponse['city'], decodedResponse['latitude'], decodedResponse['longitude']))
                items_to_print.append(item_to_list)
                print("\033[1;94muser_id\033[1;00m: \033[1;92m{0}\033[1;00m => \033[1;90m{1} \033[1;00m[ \033[1;94mcountry\033[1;00m:\033[1;92m {2} \033[1;94mcity\033[1;00m: \033[1;92m{3} \033[1;94mlatitude\033[1;00m: \033[1;92m{4} \033[1;94mlongitude\033[1;00m: \033[1;92m{5}\033[1;00m ]\033[1;00m".format(item, IPs["current_sign_in_ip"], decodedResponse['country_code2'], decodedResponse['city'], decodedResponse['latitude'], decodedResponse['longitude']))
            except KeyError:
                item_to_list = ("user_id: {0} => {1}".format(item, IPs["current_sign_in_ip"]))
                items_to_print.append(item_to_list)
                print("\033[1;94muser_id\033[1;00m: \033[1;92m{0}\033[1;00m => \033[1;90m{1}\033[1;00m".format(item, IPs["current_sign_in_ip"]))

        users_IPs_output(users_status, items_to_print, geolocation_choose)

    else:
        print("\033[1;90m\nCollecting data...\033[1;00m")
        print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
        page_counter = 0
        while 1:
            target_users = requests.get("{0}/api/v4/users?{1}=true&per_page=100&page={2}".format(gitlab_server_address, users_status, page_counter), headers=headers)
            users = target_users.json()
            if len(users) == 0:
                break
            item_counter = 0
            for item in users:
                try:
                    item = str(users[item_counter]["id"])
                    users_IDs.append(item)
                except KeyError:
                    users_IDs.append(item)
                item_counter += 1
            time.sleep(0.1)
            page_counter += 1
        
        for item in set(users_IDs):
            try:
                target_IPs = requests.get("{0}/api/v4/users/{1}".format(gitlab_server_address, item), headers=headers)
                IPs = target_IPs.json()
                user_current_sign_in_ip = IPs["current_sign_in_ip"]
                response = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey={0}&ip={1}".format(ipgeolocation_token, user_current_sign_in_ip))
                decodedResponse = response.json()
                item_to_list = ("user_id: {0} => {1} [country: {2} city: {3} latitude: {4} longitude: {5} isp: {6}]".format(item, IPs["current_sign_in_ip"], decodedResponse['country_code2'], decodedResponse['city'], decodedResponse['latitude'], decodedResponse['longitude'], decodedResponse['isp']))
                items_to_print.append(item_to_list)
                print("\033[1;94muser_id\033[1;00m: \033[1;92m{0}\033[1;00m => \033[1;90m{1} \033[1;00m[ \033[1;94mcountry\033[1;00m:\033[1;92m {2} \033[1;94mcity\033[1;00m: \033[1;92m{3} \033[1;94mlatitude\033[1;00m: \033[1;92m{4} \033[1;94mlongitude\033[1;00m: \033[1;92m{5}\033[1;00m \033[1;94misp\033[1;00m:\033[1;92m {6}\033[1;00m ]\033[1;00m".format(item, IPs["current_sign_in_ip"], decodedResponse['country_code2'], decodedResponse['city'], decodedResponse['latitude'], decodedResponse['longitude'], decodedResponse['isp']))
            except KeyError:
                item_to_list = ("user_id: {0} => {1}".format(item, IPs["current_sign_in_ip"]))
                items_to_print.append(item_to_list)
                print("\033[1;94muser_id\033[1;00m: \033[1;92m{0}\033[1;00m => \033[1;90m{1}\033[1;00m".format(item, IPs["current_sign_in_ip"]))

        users_IPs_output(users_status, items_to_print, geolocation_choose)

def get_users_IPs_abuseipdb(users_status, geolocation_choose):
    if users_status == "all":
        print("\033[1;90m\nCollecting data...\033[1;00m")
        print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
        page_counter = 0
        while 1:
            target_users = requests.get("{0}/api/v4/users?per_page=100&page={1}".format(gitlab_server_address, page_counter), headers=headers)
            users = target_users.json()
            if len(users) == 0:
                break
            item_counter = 0
            for item in users:
                try:
                    item = str(users[item_counter]["id"])
                    users_IDs.append(item)
                except KeyError:
                    users_IDs.append(item)
                item_counter += 1
            time.sleep(0.1)
            page_counter += 1

        for item in set(users_IDs):
            try:
                target_IPs = requests.get("{0}/api/v4/users/{1}".format(gitlab_server_address, item), headers=headers)
                IPs = target_IPs.json()
                user_current_sign_in_ip = IPs["current_sign_in_ip"]
                response = requests.request(method='GET', url='https://api.abuseipdb.com/api/v2/check', headers={'Accept': 'application/json', 'Key': abuseipdb_token}, params={'ipAddress': user_current_sign_in_ip, 'maxAgeInDays': '90'})
                decodedResponse = json.loads(response.text)
                item_to_list = ("user_id: {0} => {1} [country: {2} domain: {3} isp: {4} usage_type: {5}]".format(item, IPs["current_sign_in_ip"], decodedResponse['data']['countryCode'], decodedResponse['data']['domain'], decodedResponse['data']['isp'], decodedResponse['data']['usageType']))
                items_to_print.append(item_to_list)
                print("\033[1;94muser_id\033[1;00m: \033[1;92m{0}\033[1;00m => \033[1;90m{1} \033[1;00m[ \033[1;94mcountry\033[1;00m:\033[1;92m {2} \033[1;94mdomain\033[1;00m: \033[1;92m{3} \033[1;94misp\033[1;00m: \033[1;92m{4} \033[1;94musage_type\033[1;00m: \033[1;92m{5}\033[1;00m ]\033[1;00m".format(item, IPs["current_sign_in_ip"], decodedResponse['data']['countryCode'], decodedResponse['data']['domain'], decodedResponse['data']['isp'], decodedResponse['data']['usageType']))
            except KeyError:
                item_to_list = ("user_id: {0} => {1}".format(item, IPs["current_sign_in_ip"]))
                items_to_print.append(item_to_list)
                print("\033[1;94muser_id\033[1;00m: \033[1;92m{0}\033[1;00m => \033[1;90m{1}\033[1;00m".format(item, IPs["current_sign_in_ip"]))

        users_IPs_output(users_status, items_to_print, geolocation_choose)

    else:
        print("\033[1;90m\nCollecting data...\033[1;00m")
        print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
        page_counter = 0
        while 1:
            target_users = requests.get("{0}/api/v4/users?{1}=true&per_page=100&page={2}".format(gitlab_server_address, users_status, page_counter), headers=headers)
            users = target_users.json()
            if len(users) == 0:
                break
            item_counter = 0
            for item in users:
                try:
                    item = str(users[item_counter]["id"])
                    users_IDs.append(item)
                except KeyError:
                    users_IDs.append(item)
                item_counter += 1
            time.sleep(0.1)
            page_counter += 1
        
        for item in set(users_IDs):
            try:
                target_IPs = requests.get("{0}/api/v4/users/{1}".format(gitlab_server_address, item), headers=headers)
                IPs = target_IPs.json()
                user_current_sign_in_ip = IPs["current_sign_in_ip"]
                response = requests.request(method='GET', url='https://api.abuseipdb.com/api/v2/check', headers={'Accept': 'application/json', 'Key': abuseipdb_token}, params={'ipAddress': user_current_sign_in_ip, 'maxAgeInDays': '90'})
                decodedResponse = json.loads(response.text)
                item_to_list = ("user_id: {0} => {1} [country: {2} domain: {3} isp: {4} usage_type: {5}]".format(item, IPs["current_sign_in_ip"], decodedResponse['data']['countryCode'], decodedResponse['data']['domain'], decodedResponse['data']['isp'], decodedResponse['data']['usageType']))
                items_to_print.append(item_to_list)
                print("\033[1;94muser_id\033[1;00m: \033[1;92m{0}\033[1;00m => \033[1;90m{1} \033[1;00m[ \033[1;94mcountry\033[1;00m:\033[1;92m {2} \033[1;94mdomain\033[1;00m: \033[1;92m{3} \033[1;94misp\033[1;00m: \033[1;92m{4} \033[1;94musage_type\033[1;00m: \033[1;92m{5}\033[1;00m ]\033[1;00m".format(item, IPs["current_sign_in_ip"], decodedResponse['data']['countryCode'], decodedResponse['data']['domain'], decodedResponse['data']['isp'], decodedResponse['data']['usageType']))
            except KeyError:
                item_to_list = ("user_id: {0} => {1}".format(item, IPs["current_sign_in_ip"]))
                print("\033[1;94muser_id\033[1;00m: \033[1;92m{0}\033[1;00m => \033[1;90m{1}\033[1;00m".format(item, IPs["current_sign_in_ip"]))
                items_to_print.append(item_to_list)

        users_IPs_output(users_status, items_to_print, geolocation_choose)

def users_IPs_output(users_status, items_to_print, geolocation_choose):
    if not os.path.exists("{}/reports".format(os.getcwd())):
        os.mkdir("{}/reports".format(os.getcwd()))
    with open("{}/reports/users_IPs_info.txt".format(os.getcwd()), 'a') as output:
        output.write('USERS {0} IPs {1} INFO => \n'.format(users_status, geolocation_choose))
        for row in set(items_to_print):
            output.write(str(row) + '\n')
