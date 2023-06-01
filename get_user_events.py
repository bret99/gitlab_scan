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


def get_user_events():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        user_id = input("Enter user ID: ")
        date_after = input("Enter the date (\033[1;93mYYYY\033[1;00m-\033[1;93mMM\033[1;00m-\033[1;93mDD\033[1;00m) after which one should count events [press <\033[1;93mEnter\033[1;00m> for now]: ")
        date_before = input("Enter the date (\033[1;93mYYYY\033[1;00m-\033[1;93mMM\033[1;00m-\033[1;93mDD\033[1;00m) before which one should count events [press <\033[1;93mEnter\033[1;00m> for now]: ")
        if date_before == "":
            date_before = str(date.today())
        if date_after == "":
            date_after = str(date.today())
        print("\033[1;90m\nCollecting data...\033[1;00m")
        page_counter = 0
        while 1:
            target_user = requests.get("{0}/api/v4/users/{1}/events?after={2}&before={3}&per_page=100&page={4}".format(gitlab_server_address, user_id, date_after, date_before, page_counter), headers=headers)
            user = target_user.json()
            if len(user) == 0:
                break
            item_counter = 0
            for item in user:
                if user[item_counter]["action_name"].startswith("push"):
                    item = "\nproject_id: " + str(user[item_counter]["project_id"]) + "\naction_name: " + str(user[item_counter]["action_name"]) + "\ncreated_at: " + str(user[item_counter]["created_at"]) + "\n\tpush_data: {" + "\n\t\taction: " + str(user[item_counter]["push_data"]["action"]) + "\n\t\tref_type: " + str(user[item_counter]["push_data"]["ref_type"]) + "\n\t\tref: " + str(user[item_counter]["push_data"]["ref"]) + "\n\t\tcommit_title: " + str(user[item_counter]["push_data"]["commit_title"]) + "\n\t\t}"
                    events_list.append(item)
                    item_to_print = "\033[1;94m\nproject_id\033[1;00m: \033[1;92m" + str(user[item_counter]["project_id"]) + "\033[1;94m\n\taction_name\033[1;00m: \033[1;92m" + str(user[item_counter]["action_name"]) + "\033[1;94m\n\tcreated_at\033[1;00m: \033[1;92m" + str(user[item_counter]["created_at"]) + "\n\t\033[1;94mpush_data\033[1;00m: {" + "\033[1;94m\n\t\taction\033[1;00m: \033[1;92m" + str(user[item_counter]["push_data"]["action"]) + "\033[1;94m\n\t\tref_type\033[1;00m: \033[1;92m" + str(user[item_counter]["push_data"]["ref_type"]) + "\033[1;94m\n\t\tref\033[1;00m : \033[1;92m" + str(user[item_counter]["push_data"]["ref"]) + "\033[1;94m\n\t\tcommit_title\033[1;00m: \033[1;92m" + str(user[item_counter]["push_data"]["commit_title"]) + "\033[1;00m\n\t\t}"
                    events_to_print_list.append(item_to_print)
                else:
                    item = "\nproject_id: " + str(user[item_counter]["project_id"]) + "\naction_name: " + str(user[item_counter]["action_name"]) + "\ncreated_at: " + str(user[item_counter]["created_at"]) + "\033[1;00m"
                    events_list.append(item)
                    item_to_print = "\n\033[1;94mproject_id\033[1;00m: \033[1;92m" + str(user[item_counter]["project_id"]) + "\033[1;94m\n\taction_name\033[1;00m: \033[1;92m" + str(user[item_counter]["action_name"]) + "\033[1;94m\n\tcreated_at\033[1;00m: \033[1;92m" + str(user[item_counter]["created_at"]) + "\033[1;00m"
                    events_to_print_list.append(item_to_print)

                item_counter += 1
            time.sleep(0.1)
            page_counter += 1
                    
        for item in set(events_to_print_list):
            print(item)

        if not os.path.exists("{}/reports".format(os.getcwd())):
            os.mkdir("{}/reports".format(os.getcwd()))
        events_output(user_id)
        
        print("\nUser events amount is \033[1;94m{}\033[1;00m".format(len(set(events_list))))
        print("\nOne can find results in \033[1;95m{}/reports/user_events_info.txt\033[1;00m\n".format(os.getcwd()))
                    
    except (InvalidURL, MissingSchema):
        print("\n\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\n\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr input is not correct\033[1;00m")
    except ConnectionError:
        print("\n\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        pass

def events_output(userid):
    with open("{}/reports/user_events_info.txt".format(os.getcwd()), 'w') as output:
        output.write('USER {} EVENTS INFO => \n'.format(userid))
        for row in set(events_list):
            output.write(str(row) + '\n')
