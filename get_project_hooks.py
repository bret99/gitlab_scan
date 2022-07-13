import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
from access_tokens import gitlab_access_token, gitlab_server_address

hooks_list = []
hooks_list_to_print = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}

def get_project_hooks():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        project_id = input("Enter project ID: ")
        print("\033[1;90m\nCollecting data...\033[1;00m")
        print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
        page_counter = 0
        while 1:
            target_project_hooks = requests.get("{0}/api/v4/projects/{1}/hooks?per_page=100&page={2}".format(gitlab_server_address, project_id, page_counter), headers=headers)
            hooks = target_project_hooks.json()
            if len(hooks) == 0:
                break
            item_counter = 0
            for item in hooks:
                try:
                    item = "id: " + str(hooks[item_counter]["id"]) + " url " + hooks[item_counter]["url"] + " created_at: " + hooks[item_counter]["created_at"]
                    hooks_list.append(item)
                    item = item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(hooks[item_counter]["id"]) + " \033[1;94murl\033[1;00m: \033[1;92m" + hooks[item_counter]["url"] + "\033[1;94m created_at\033[1;00m: \033[1;92m" + hooks[item_counter]["created_at"] + "\033[1;00m"
                    hooks_list_to_print.append(item_to_print)
                except KeyError:
                    item = "id: " + str(hooks[item_counter]["id"]) + " url " + hooks[item_counter]["url"] + " created_at: " + hooks[item_counter]["created_at"]
                    hooks_list.append(item)
                item_counter += 1
            time.sleep(0.1)
            page_counter += 1

        for item in set(hooks_list_to_print):
            print(item)
                    
        if not os.path.exists("{}/reports".format(os.getcwd())):
            os.mkdir("{}/reports".format(os.getcwd()))
        with open("{}/reports/project_hooks_info.txt".format(os.getcwd()), 'a') as output:
            output.write('PROJECT {} HOOKS INFO => \n'.format(project_id))
            for row in set(hooks_list):
                output.write(str(row) + '\n')
                
        print("\nProject hooks amount is \033[1;94m{}\033[1;00m".format(len(set(hooks_list))))
        print("\nOne can find results in \033[1;95m{}/reports/project_hooks_info.txt\033[1;00m".format(os.getcwd()))
   
    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr project ID is not correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        print("\033[1;93m\nResults not saved!\033[1;00m")
