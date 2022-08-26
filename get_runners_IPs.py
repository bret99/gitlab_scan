import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
import json
from access_tokens import gitlab_access_token, gitlab_server_address, abuseipdb_token, ipgeolocation_token

runners_IPs = []
runners_IPs_info = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}

def get_runners_IPs():
    try:
        if gitlab_access_token == "":
            print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
            sys.exit()
        elif "http" not in gitlab_server_address:
            print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
            sys.exit()
        geolocation_choose = input("Choose IP to geolocation reverse service (\033[1;95mabuseipdb\033[1;00m, \033[1;96mipgeolocation\033[1;00m): ")
        if geolocation_choose == "abuseipdb":
            if abuseipdb_token == "":
                print("\nOne should write correct value to \033[1;95mabuseipdb_token \033[1;00min \033[1;95maccess_token.py \033[1;00mto get IPs geolocationsm!")
            get_users_IPs_abuseipdb(geolocation_choose=geolocation_choose)
        elif geolocation_choose == "ipgeolocation":
            if ipgeolocation_token == "":
                print("\nOne should write correct value to \033[1;96mipgeolocation_token \033[1;00min \033[1;95maccess_token.py \033[1;00mto get IPs geolocations!")
            get_users_IPs_ipgeolocation(geolocation_choose=geolocation_choose)
        else:
            sys.exit("\033[1;93mWrong input!\033[1;00m")

        print("\nRunners amount is \033[1;94m{}\033[1;00m".format(len(set(runners_IPs))))
        print("\nOne can find results in \033[1;95m{}/reports/runners_IPs_info.txt\033[1;00m".format(os.getcwd()))
 
    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab/AbuseIPDB access tokens in \033[1;95maccess_tokens.py \033[1;93mare correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
        runners_IPs_output(runners_IPs_info, geolocation_choose)
    except KeyboardInterrupt:
        print("\033[1;93m\nResults not saved!\033[1;00m")

def get_users_IPs_abuseipdb(geolocation_choose):
    print("\033[1;90m\nCollecting data...\033[1;00m")
    print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
    page_counter = 0
    while 1:
        target_runners = requests.get("{0}/api/v4/runners/all?&per_page=100&page={1}".format(gitlab_server_address, page_counter), headers=headers)
        runners = target_runners.json()
        if len(runners) == 0:
            break
        item_counter = 0
        for item in runners:
            try:
                runners_IPs.append(runners[item_counter]["ip_address"])
            except KeyError:
                pass
            item_counter += 1
        time.sleep(0.1)
        page_counter += 1

    for IP in set(runners_IPs):
        try:
            response = requests.request(method='GET', url='https://api.abuseipdb.com/api/v2/check', headers={'Accept': 'application/json', 'Key': abuseipdb_token}, params={'ipAddress': IP, 'maxAgeInDays': '90'})
            decodedResponse = json.loads(response.text)
            print("\033[1;90m{}\033[1;00m =>".format(IP), "\033[1;94mcountry\033[1;00m:\033[1;92m", decodedResponse['data']['countryCode'], "\033[1;94mdomain\033[1;00m:\033[1;92m", decodedResponse['data']['domain'], "\033[1;94misp\033[1;00m:\033[1;92m",  decodedResponse['data']['isp'], "\033[1;94musage_type\033[1;00m:\033[1;92m", decodedResponse['data']['usageType'], "\033[1;00m")
            IP_to_list = IP + " country", decodedResponse['data']['countryCode'], "domain", decodedResponse['data']['domain'], "isp",  decodedResponse['data']['isp'], "usage_type", decodedResponse['data']['usageType']
            runners_IPs_info.append(IP_to_list)
            time.sleep(0.5)
        except KeyError:
            IP_to_list = IP 
            runners_IPs_info.append(IP_to_list)
            print("\033[1;94m{}\033[1;00m".format(IP), "\033[1;00m")

    runners_IPs_output(runners_IPs_info, geolocation_choose)

def get_users_IPs_ipgeolocation(geolocation_choose):
    print("\033[1;90m\nCollecting data...\033[1;00m")
    print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
    page_counter = 0
    while 1:
        target_runners = requests.get("{0}/api/v4/runners/all?&per_page=100&page={1}".format(gitlab_server_address, page_counter), headers=headers)
        runners = target_runners.json()
        if len(runners) == 0:
            break
        item_counter = 0
        for item in runners:
            try:
                runners_IPs.append(runners[item_counter]["ip_address"])
            except KeyError:
                pass
            item_counter += 1
        time.sleep(0.1)
        page_counter += 1

    for IP in set(runners_IPs):
        try:
            response = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey={0}&ip={1}".format(ipgeolocation_token, IP))
            decodedResponse = response.json()
            print("\033[1;90m{}\033[1;00m =>".format(IP), "\033[1;94mcountry\033[1;00m:\033[1;92m", decodedResponse['country_code2'], "\033[1;94mcity\033[1;00m:\033[1;92m", decodedResponse['city'], "\033[1;94mlatitude\033[1;00m:\033[1;92m", decodedResponse['latitude'], "\033[1;94mlongitude\033[1;00m:\033[1;92m",  decodedResponse['longitude'], "\033[1;94misp\033[1;00m:\033[1;92m", decodedResponse['isp'], "\033[1;00m")
            IP_to_list = IP + " country", decodedResponse['country_code2'], "city", decodedResponse['city'], "latitude",  decodedResponse['latitude'], "longitude", decodedResponse['longitude'], "isp", decodedResponse['isp']
            runners_IPs_info.append(IP_to_list)
            time.sleep(0.5)
        except KeyError:
            IP_to_list = IP 
            runners_IPs_info.append(IP_to_list)
            print("\033[1;94m{}\033[1;00m".format(IP), "\033[1;00m")

    runners_IPs_output(runners_IPs_info, geolocation_choose)

def runners_IPs_output(runners_IPs_info, geolocation_choose):
    if not os.path.exists("{}/reports".format(os.getcwd())):
        os.mkdir("{}/reports".format(os.getcwd()))
    with open("{}/reports/runners_IPs_info.txt".format(os.getcwd()), 'a') as output:
        output.write('RUNNERS IPs {} INFO => \n'.format(geolocation_choose))
        for row in list(set(runners_IPs_info)):
            output.write(str(row) + '\n')
