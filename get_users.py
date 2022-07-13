import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
from access_tokens import gitlab_access_token, gitlab_server_address

users_list = []
users_list_to_print = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}
status_list = ["admins", "active", "blocked", "external", "without_projects", "all"]

def get_users():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        users_status = input("Enter users status (\033[1;95madmins\033[1;00m, \033[1;92mactive\033[1;00m, \033[1;91mblocked\033[1;00m, \033[;93mexternal\033[1;00m, \033[;90mwithout_projects\033[1;00m, all): ")
        if users_status not in status_list:
            sys.exit("\033[1;93mWrong input!\033[1;00m")
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
                        item = "id: " + str(users[item_counter]["id"]) + " username: " + users[item_counter]["username"] + " name: " + users[item_counter]["name"] + " state: " + users[item_counter]["state"] + " web_url: " + users[item_counter]["web_url"]
                        users_list.append(item)
                        item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(users[item_counter]["id"]) + "\033[1;94m username\033[1;00m: \033[1;92m" + users[item_counter]["username"] + "\033[1;94m name\033[1;00m: \033[1;92m" + users[item_counter]["name"] + "\033[1;94m state\033[1;00m: \033[1;92m" + users[item_counter]["state"] + "\033[1;94m web_url\033[1;00m: \033[1;92m" + users[item_counter]["web_url"] + "\033[1;00m"
                        users_list_to_print.append(item_to_print)
                    except KeyError:
                        item = "id: " + str(users[item_counter]["id"]) + " username: " + users[item_counter]["username"] + " name: " + users[item_counter]["name"] + " state: " + users[item_counter]["state"] + " web_url: " + users[item_counter]["web_url"]
                        users_list.append(item)
                    item_counter += 1
                time.sleep(0.1)
                page_counter += 1
            for item in set(users_list_to_print):
                print(item)
            
            if not os.path.exists("{}/reports".format(os.getcwd())):
                os.mkdir("{}/reports".format(os.getcwd()))
            with open("{}/reports/users_info.txt".format(os.getcwd()), 'a') as output:
                output.write('USERS {} INFO => \n'.format(users_status))
                for row in set(users_list):
                    output.write(str(row) + '\n')
        
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
                        item = "id: " + str(users[item_counter]["id"]) + " username: " + users[item_counter]["username"] + " name: " + users[item_counter]["name"] + " state: " + users[item_counter]["state"] + " web_url: " + users[item_counter]["web_url"]
                        users_list.append(item) 
                        item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(users[item_counter]["id"]) + "\033[1;94m username\033[1;00m: \033[1;92m" + users[item_counter]["username"] + "\033[1;94m name\033[1;00m: \033[1;92m" + users[item_counter]["name"] + "\033[1;94m state\033[1;00m: \033[1;92m" + users[item_counter]["state"] + "\033[1;94m web_url\033[1;00m: \033[1;92m" + users[item_counter]["web_url"] + "\033[1;00m"
                        users_list_to_print.append(item_to_print)
                    except KeyError:
                        item = "id: " + str(users[item_counter]["id"]) + " username: " + users[item_counter]["username"] + " name: " + users[item_counter]["name"] + " state: " + users[item_counter]["state"] + " web_url: " + users[item_counter]["web_url"]
                        users_list.append(item)
                    item_counter += 1
                time.sleep(0.1)
                page_counter += 1
            for item in set(users_list_to_print):
                print(item)
       
            if not os.path.exists("{}/reports".format(os.getcwd())):
                os.mkdir("{}/reports".format(os.getcwd()))
            with open("{}/reports/users_info.txt".format(os.getcwd()), 'a') as output:
                output.write('USERS {} INFO => \n'.format(users_status))
                for row in set(users_list):
                    output.write(str(row) + '\n')

        print("\n{0} users amount is \033[1;94m{1}\033[1;00m".format(users_status, len(set(users_list))))
        print("\nOne can find results in \033[1;95m{}/reports/users_info.txt\033[1;00m\n".format(os.getcwd()))

    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        print("\033[1;93m\nResults not saved!\033[1;00m")

