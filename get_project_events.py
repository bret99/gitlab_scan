import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
from datetime import date
import time
import os
import sys
from access_tokens import gitlab_access_token, gitlab_server_address

events_list = []
events_to_print_list = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}


def get_project_events():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        project_id = input("Enter project ID: ")
        date_after = input("Enter the date (\033[1;93mYYYY\033[1;00m-\033[1;93mMM\033[1;00m-\033[1;93mDD\033[1;00m) after which one should count events [press <\033[1;93mEnter\033[1;00m> for now]: ")
        date_before = input("Enter the date (\033[1;93mYYYY\033[1;00m-\033[1;93mMM\033[1;00m-\033[1;93mDD\033[1;00m) before which one should count events [press <\033[1;93mEnter\033[1;00m> for now]: ")
        if date_before == "":
            date_before = str(date.today())
        if date_after == "":
            date_after = str(date.today())
        print("\033[1;90m\nCollecting data...\033[1;00m")
        print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
        page_counter = 0
        while 1:
            target_project = requests.get("{0}/api/v4/projects/{1}/events?after={2}&before={3}&per_page=100&page={4}".format(gitlab_server_address, project_id, date_after, date_before, page_counter), headers=headers)
            project = target_project.json()
            if len(project) == 0:
                break
            item_counter = 0
            for item in project:
                if project[item_counter]["action_name"].startswith("push"):
                    item = "author_id: " + str(project[item_counter]["author"]["id"]) + " username: " + str(project[item_counter]["author"]["username"]) + " action_name: " + str(project[item_counter]["action_name"]) + " created_at: " + str(project[item_counter]["created_at"]) + " push_action: " + str(project[item_counter]["push_data"]["action"]) + " ref_type: " + str(project[item_counter]["push_data"]["ref_type"]) + " ref: " + str(project[item_counter]["push_data"]["ref"]) + " commit_title: " + str(project[item_counter]["push_data"]["commit_title"])
                    events_list.append(item)
                    item_to_print = "\033[1;94mauthor_id\033[1;00m: \033[1;92m" + str(project[item_counter]["author"]["id"]) + " \033[1;94musername\033[1;00m: \033[1;92m" + str(project[item_counter]["author"]["username"]) + " \033[1;94maction_name\033[1;00m: \033[1;92m" + str(project[item_counter]["action_name"]) + " \033[1;94mcreated_at\033[1;00m: \033[1;92m" + str(project[item_counter]["created_at"]) + " \033[1;94mpush_action\033[1;00m: \033[1;92m" + str(project[item_counter]["push_data"]["action"]) + " \033[1;94mref_type\033[1;00m: \033[1;92m" + str(project[item_counter]["push_data"]["ref_type"]) + " \033[1;94mref\033[1;00m: \033[1;92m" + str(project[item_counter]["push_data"]["ref"]) + " \033[1;94mcommit_title\033[1;00m: \033[1;92m" + str(project[item_counter]["push_data"]["commit_title"]) + "\033[1;00m"
                    events_to_print_list.append(item_to_print)
                else:
                    item = "author_id: " + str(project[item_counter]["author"]["id"]) + " username: " + str(project[item_counter]["author"]["username"]) + "]" + " action_name: " + str(project[item_counter]["action_name"]) + " created_at: " + str(project[item_counter]["created_at"])
                    events_list.append(item)
                    item_to_print = "\033[1;94mauthor_id\033[1;00m: \033[1;92m" + str(project[item_counter]["author"]["id"]) + " \033[1;94musername\033[1;00m: \033[1;92m" + str(project[item_counter]["author"]["username"]) + " \033[1;94maction_name\033[1;00m: \033[1;92m" + str(project[item_counter]["action_name"]) + " \033[1;94mcreated_at\033[1;00m: \033[1;92m" + str(project[item_counter]["created_at"]) + "\033[1;00m"
                    events_to_print_list.append(item_to_print)

                item_counter += 1
            time.sleep(0.1)
            page_counter += 1
                    
        for item in set(events_to_print_list):
            print(item)

        if not os.path.exists("{}/reports".format(os.getcwd())):
            os.mkdir("{}/reports".format(os.getcwd()))
        events_output(project_id)
        
        print("\nProject events amount is \033[1;94m{}\033[1;00m".format(len(set(events_list))))
        print("\nOne can find results in \033[1;95m{}/reports/project_events_info.txt\033[1;00m\n".format(os.getcwd()))
                    
    except (InvalidURL, MissingSchema):
        print("\n\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\n\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr input is not correct\033[1;00m")
    except ConnectionError:
        print("\n\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        pass

def events_output(projectid):
    with open("{}/reports/project_events_info.txt".format(os.getcwd()), 'w') as output:
        output.write('PROJECT {} EVENTS INFO => \n'.format(projectid))
        for row in set(events_list):
            output.write(str(row) + '\n')
