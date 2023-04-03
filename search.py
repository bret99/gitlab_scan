import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
from access_tokens import gitlab_access_token, gitlab_server_address

users_list = []
users_list_to_print = []
projects_list = []
projects_list_to_print = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}
search_scope_list = ["users", "projects"]

def get_search():
    try:
        search_scope = input("Enter the scope to get (\033[1;92musers\033[1;00m/\033[1;94mprojects\033[1;00m): ")
        if search_scope not in search_scope_list:
            sys.exit("\033[1;93mWrong input!\033[1;00m")
        else:
            search_target = input("Enter the target to get: ")
            if search_scope == "users":
                print("\033[1;90m\nCollecting data...\033[1;00m")
                print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
                page_counter = 0
                while 1:
                    target_search = requests.get("{0}/api/v4/search?scope=users&search={1}&page_counter=100&page={2}".format(gitlab_server_address, search_target, page_counter), headers=headers)
                    search = target_search.json()
                    if len(search) == 0:
                        break
                    item_counter = 0
                    for item in search:
                        try:
                            item = "id: " + str(search[item_counter]["id"]) + " username: " + search[item_counter]["username"] + " name: " + search[item_counter]["name"] + " state: " + search[item_counter]["state"] + " web_url: " + search[item_counter]["web_url"]
                            users_list.append(item)
                            item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(search[item_counter]["id"]) + "\033[1;94m username\033[1;00m: \033[1;92m" + search[item_counter]["username"] + "\033[1;94m name\033[1;00m: \033[1;92m" + search[item_counter]["name"] + "\033[1;94m state\033[1;00m: \033[1;92m" + search[item_counter]["state"] + "\033[1;94m web_url\033[1;00m: \033[1;92m" + search[item_counter]["web_url"] + "\033[1;00m"
                            users_list_to_print.append(item_to_print)
                        except KeyError:
                            item = "id: " + str(search[item_counter]["id"]) + " username: " + search[item_counter]["username"] + " name: " + search[item_counter]["name"] + " state: " + search[item_counter]["state"] + " web_url: " + search[item_counter]["web_url"]
                            users_list.append(item)
                        item_counter += 1
                    time.sleep(0.1)
                    page_counter += 1
                for item in set(users_list_to_print):
                    print(item)
            
                if len(users_list) == 0:
                    print("\nUsers amount is \033[1;94m{0}\033[1;00m".format(len(set(users_list))))
                else:
                    if not os.path.exists("{}/reports".format(os.getcwd())):
                        os.mkdir("{}/reports".format(os.getcwd()))
                    with open("{}/reports/search_users_info.txt".format(os.getcwd()), 'a') as output:
                        output.write('SEARCH USERS {} INFO => \n'.format(search_target))
                        for row in set(users_list):
                            output.write(str(row) + '\n')
                    print("\nUsers amount is \033[1;94m{0}\033[1;00m".format(len(set(users_list))))
                    print("\nOne can find results in \033[1;95m{}/reports/search_users_info.txt\033[1;00m\n".format(os.getcwd()))
                
            elif search_scope == "projects":
                print("\033[1;90m\nCollecting data...\033[1;00m")
                print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
                page_counter = 0
                while 1:
                    target_search = requests.get("{0}/api/v4/search?scope=projects&search={1}&page_counter=100&page={2}".format(gitlab_server_address, search_target, page_counter), headers=headers)
                    search = target_search.json()
                    if len(search) == 0:
                        break
                    item_counter = 0
                    for item in search:
                        try:
                            item = "id: " + str(search[item_counter]["id"]) + " name: " + search[item_counter]["name"] + " name_with_namespace: " + search[item_counter]["name_with_namespace"] + " state: " + " web_url: " + search[item_counter]["web_url"]
                            projects_list.append(item)
                            item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(search[item_counter]["id"]) + "\033[1;94m name\033[1;00m: \033[1;92m" + search[item_counter]["name"] + "\033[1;94m name_with_namespace\033[1;00m: \033[1;92m" + search[item_counter]["name_with_namespace"] + "\033[1;94m web_url\033[1;00m: \033[1;92m" + search[item_counter]["web_url"] + "\033[1;00m"
                            projects_list_to_print.append(item_to_print)
                        except KeyError:
                            item = "id: " + str(search[item_counter]["id"]) + " name: " + search[item_counter]["name"] + " name_with_namespace: " + search[item_counter]["name_with_namespace"] + " web_url: " + search[item_counter]["web_url"]
                            projects_list.append(item)
                        item_counter += 1
                    time.sleep(0.1)
                    page_counter += 1
                for item in set(projects_list_to_print):
                    print(item)
            
                if len(projects_list) == 0:
                    print("\nProjects amount is \033[1;94m{0}\033[1;00m".format(len(set(users_list))))
                else:
                    if not os.path.exists("{}/reports".format(os.getcwd())):
                        os.mkdir("{}/reports".format(os.getcwd()))
                    with open("{}/reports/search_projects_info.txt".format(os.getcwd()), 'a') as output:
                        output.write('SEARCH PROJECTS {} INFO => \n'.format(search_target))
                        for row in set(projects_list):
                            output.write(str(row) + '\n')
                    print("\nProjects amount is \033[1;94m{0}\033[1;00m".format(len(set(projects_list))))
                    print("\nOne can find results in \033[1;95m{}/reports/search_projects_info.txt\033[1;00m\n".format(os.getcwd()))
                
    except (InvalidURL, MissingSchema):
        print(" \033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr project ID is not correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        pass

