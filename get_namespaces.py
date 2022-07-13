import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
from access_tokens import gitlab_access_token, gitlab_server_address

namespaces_list = []
namespaces_to_print_list = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}

def get_namespaces():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        print("\033[1;90m\nCollecting data...\033[1;00m")
        print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
        page_counter = 0
        while 1:
            target_namespaces = requests.get("{0}/api/v4/namespaces?per_page=100&page={1}".format(gitlab_server_address, page_counter), headers=headers)
            namespaces = target_namespaces.json()
            if len(namespaces) == 0:
                break
            item_counter = 0
            for item in namespaces:
                try:
                    item = "id: " + str(namespaces[item_counter]["id"]) + " name: " + namespaces[item_counter]["name"] + " path: " + namespaces[item_counter]["path"] + " kind: " + namespaces[item_counter]["kind"] + " full_path: " + namespaces[item_counter]["full_path"] + " parent_id: " + str(namespaces[item_counter]["parent_id"]) + " web_url: " + namespaces[item_counter]["web_url"]
                    namespaces_list.append(item)
                    item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(namespaces[item_counter]["id"]) + "\033[1;94m name\033[1;00m: \033[1;92m" + namespaces[item_counter]["name"] + "\033[1;94m path\033[1;00m: \033[1;92m" + namespaces[item_counter]["path"] + "\033[1;94m kind\033[1;00m: \033[1;92m" + namespaces[item_counter]["kind"] + "\033[1;94m web_url\033[1;00m: \033[1;92m" + namespaces[item_counter]["web_url"] + "\033[1;00m"
                    namespaces_to_print_list.append(item_to_print)
                except KeyError:
                    item = "id: " + str(namespaces[item_counter]["id"]) + " name: " + namespaces[item_counter]["name"] + " path: " + namespaces[item_counter]["path"] + " kind: " + namespaces[item_counter]["kind"] + " full_path: " + namespaces[item_counter]["full_path"] + " parent_id: " + str(namespaces[item_counter]["parent_id"]) + " web_url: " + namespaces[item_counter]["web_url"]
                    namespaces_list.append(item)
                item_counter += 1
            time.sleep(0.1)
            page_counter += 1

        for item in set(namespaces_to_print_list):
            print(item)

        if not os.path.exists("{}/reports".format(os.getcwd())):
            os.mkdir("{}/reports".format(os.getcwd()))
        with open("{}/reports/namespaces_info.txt".format(os.getcwd()), 'w') as output:
            output.write('NAMESPACES INFO => \n')
            for row in set(namespaces_list):
                output.write(str(row) + '\n')
        
        print("\nNamespaces amount is \033[1;94m{}\033[1;00m".format(len(set(namespaces_list))))
        print("\nOne can find results in \033[1;95m{}/reports/namespaces_info.txt\033[1;00m\n".format(os.getcwd()))

    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        print("\033[1;93m\nResults not saved!\033[1;00m")
