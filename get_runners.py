import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
from access_tokens import gitlab_access_token, gitlab_server_address

runners_list = []
runners_list_to_print = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}
status_list = ["online", "offline", "stale", "never_contacted", "all"]

def get_runners():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        runners_status = input("Enter runners status (\033[1;92monline\033[1;00m, \033[1;90moffline\033[1;00m, \033[;93mstale\033[1;00m, \033[;91mnever_contacted\033[1;00m, all): ")
        if runners_status not in status_list:
            sys.exit("\033[1;93mWrong input!\033[1;00m")
        if runners_status == "all":
            print("\033[1;90m\nCollecting data...\033[1;00m")
            print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
            page_counter = 0
            while 1:
                target_runners = requests.get("{0}/api/v4/runners/all?per_page=100&page={1}".format(gitlab_server_address, page_counter), headers=headers)
                runners = target_runners.json()
                if len(runners) == 0:
                    break
                item_counter = 0
                for item in runners:
                    try:
                        item = "id: " + str(runners[item_counter]["id"]) + " description: " + runners[item_counter]["description"] + " ip_address: " + str(runners[item_counter]["ip_address"] + " active: " + str(runners[item_counter]["active"]) + " is_shared: " + str(runners[item_counter]["is_shared"]) + " runner_type: " + runners[item_counter]["runner_type"] + " status: " + runners[item_counter]["status"])
                        runners_list.append(item)
                        item = item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(runners[item_counter]["id"]) + "\033[1;94m description\033[1;00m: \033[1;92m" + runners[item_counter]["description"] + "\033[1;94m ip_address\033[1;00m: \033[1;92m" + str(runners[item_counter]["ip_address"] + "\033[1;94m active\033[1;00m: \033[1;92m" + str(runners[item_counter]["active"]) + "\033[1;94m is_shared\033[1;00m: \033[1;92m" + str(runners[item_counter]["is_shared"]) + " \033[1;94mrunner_type\033[1;00m: \033[1;92m" + runners[item_counter]["runner_type"] + " \033[1;94mstatus\033[1;00m: \033[1;92m" + runners[item_counter]["status"] + "\033[1;00m")
                        runners_list_to_print.append(item_to_print)
                    except KeyError:
                        item = "id\033[1;00m: " + str(runners[item_counter]["id"]) + " description\033[1;00m: " + runners[item_counter]["description"] + " ip_address\033[1;00m: " + str(runners[item_counter]["ip_address"] + " is_shared\033[1;00m: " + str(runners[item_counter]["is_shared"]) + " runner_type\033[1;00m: " + runners[item_counter]["runner_type"] + " status\033[1;00m: " + runners[item_counter]["status"])
                        runners_list.append(item)
                    item_counter += 1
                time.sleep(0.1)
                page_counter += 1
            
            for item in set(runners_list_to_print):
                print(item)

            if not os.path.exists("{}/reports".format(os.getcwd())):
                os.mkdir("{}/reports".format(os.getcwd()))
            runners_output(runners_status=runners_status)
        
        else:
            print("\033[1;90m\nCollecting data...\033[1;00m")
            print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
            page_counter = 0
            while 1:
                target_runners = requests.get("{0}/api/v4/runners/all?status={1}&per_page=100&page={2}".format(gitlab_server_address, runners_status, page_counter), headers=headers)
                runners = target_runners.json()
                if len(runners) == 0:
                    break
                item_counter = 0
                for item in runners:
                    try:
                        item = "id: " + str(runners[item_counter]["id"]) + " description: " + runners[item_counter]["description"] + " ip_address: " + str(runners[item_counter]["ip_address"] + " active: " + str(runners[item_counter]["active"]) + " is_shared: " + str(runners[item_counter]["is_shared"]) + " runner_type: " + runners[item_counter]["runner_type"] + " status: " + runners[item_counter]["status"])
                        runners_list.append(item)
                        item = item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(runners[item_counter]["id"]) + "\033[1;94m description\033[1;00m: \033[1;92m" + runners[item_counter]["description"] + "\033[1;94m ip_address\033[1;00m: \033[1;92m" + str(runners[item_counter]["ip_address"] + "\033[1;94m active\033[1;00m: \033[1;92m" + str(runners[item_counter]["active"]) + "\033[1;94m is_shared\033[1;00m: \033[1;92m" + str(runners[item_counter]["is_shared"]) + " \033[1;94mrunner_type\033[1;00m: \033[1;92m" + runners[item_counter]["runner_type"] + " \033[1;94mstatus\033[1;00m: \033[1;92m" + runners[item_counter]["status"] + "\033[1;00m")
                        runners_list_to_print.append(item_to_print)
                    except KeyError:
                        item = "id\033[1;00m: " + str(runners[item_counter]["id"]) + " description\033[1;00m: " + runners[item_counter]["description"] + " ip_address\033[1;00m: " + str(runners[item_counter]["ip_address"] + " is_shared\033[1;00m: " + str(runners[item_counter]["is_shared"]) + " runner_type\033[1;00m: " + runners[item_counter]["runner_type"] + " status\033[1;00m: " + runners[item_counter]["status"])
                        runners_list.append(item)
                    item_counter += 1
                time.sleep(0.1)
                page_counter += 1

            for item in set(runners_list_to_print):
                print(item)
            
            if not os.path.exists("{}/reports".format(os.getcwd())):
                os.mkdir("{}/reports".format(os.getcwd()))
            runners_output(runners_status=runners_status)

        print("\nRunners amount is \033[1;94m{}\033[1;00m".format(len(set(runners_list))))
        print("\nOne can find results in \033[1;95m{}/reports/runners_info.txt\033[1;00m\n".format(os.getcwd()))

    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
        runners_output(runners_status)
    except KeyboardInterrupt:
        print("\033[1;93m\nResults not saved!\033[1;00m")

def runners_output(runners_status):
    with open("{}/reports/runners_info.txt".format(os.getcwd()), 'a') as output:
        output.write('{} RUNNERS INFO => \n'.format(runners_status))
        for row in set(runners_list):
            output.write(str(row) + '\n')
