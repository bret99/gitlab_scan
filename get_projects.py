import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
from access_tokens import gitlab_access_token, gitlab_server_address

projects_list = []
projects_list_to_print = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}
status_list = ["running", "success", "failed", "canceled", "all"]

def get_projects():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    print("\033[1;90m\nCollecting data...\033[1;00m")
    print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
    try:
        page_counter = 0
        while 1:
            target_projects = requests.get("{0}/api/v4/projects?per_page=100&page={1}".format(gitlab_server_address, page_counter), headers=headers)
            projects = target_projects.json()
            if len(projects) == 0:
                break
            item_counter = 0
            for item in projects:
                try:
                    item = "id: " + str(projects[item_counter]["id"]) + " name " + projects[item_counter]["name"] + " visibility: " + projects[item_counter]["visibility"] + " namespace_id: " + str(projects[item_counter]["namespace"]["id"]) + " web_url: " + projects[item_counter]["web_url"]
                    projects_list.append(item)
                    item = item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(projects[item_counter]["id"]) + " \033[1;94mname\033[1;00m: \033[1;92m" + projects[item_counter]["name"] + "\033[1;94m visibility\033[1;00m: \033[1;92m" + projects[item_counter]["visibility"] + " \033[1;94mnamespace_id\033[1;00m: \033[1;92m" + str(projects[item_counter]["namespace"]["id"]) + " \033[1;94mweb_url\033[1;00m: \033[1;92m" + projects[item_counter]["web_url"] + "\033[1;00m"
                    projects_list_to_print.append(item_to_print)
                except KeyError:
                    item = "id: " + str(projects[item_counter]["id"]) + " name " + projects[item_counter]["name"] + " visibility: " + projects[item_counter]["visibility"] + " namespace_id: " + str(projects[item_counter]["namespace"]["id"]) + " web_url: " + projects[item_counter]["web_url"]
                    projects_list.append(item)
                item_counter += 1
            time.sleep(0.1)
            page_counter += 1

        for item in set(projects_list_to_print):
            print(item)
                    
        if not os.path.exists("{}/reports".format(os.getcwd())):
            os.mkdir("{}/reports".format(os.getcwd()))
        projects_output()

        print("\nProjects amount is \033[1;94m{}\033[1;00m".format(len(set(projects_list))))
        print("\nOne can find results in \033[1;95m{}/reports/projects_info.txt\033[1;00m".format(os.getcwd()))
   
    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr namspace ID is not correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
        projects_output()
    except KeyboardInterrupt:
        print("\033[1;93m\nResults not saved!\033[1;00m")

def projects_output():
    with open("{}/reports/projects_info.txt".format(os.getcwd()), 'a') as output:
        output.write('PROJECTS INFO => \n')
        for row in set(projects_list):
            output.write(str(row) + '\n')
