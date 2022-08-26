import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
from access_tokens import gitlab_access_token, gitlab_server_address

jobs_list = []
jobs_list_to_print = []
headers = {"PRIVATE-TOKEN": gitlab_access_token}
status_list = ["running", "success", "failed", "canceled", "all"]

def get_runner_jobs():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        runner_id = input("Enter runner ID: ")
        jobs_status = input("Enter jobs status (\033[1;96mrunning\033[1;00m, \033[1;92msuccess\033[1;00m, \033[;90mfailed\033[1;00m, \033[;91mcanceled\033[1;00m, all): ")
        if jobs_status not in status_list:
            sys.exit("\033[1;93mWrong input!\033[1;00m")
        if jobs_status == "all":
            print("\033[1;90m\nCollecting data...\033[1;00m")
            print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
            page_counter = 0
            while 1:
                target_jobs = requests.get("{0}/api/v4/runners/{1}/jobs?per_page=100&page={2}".format(gitlab_server_address, runner_id, page_counter), headers=headers)
                jobs = target_jobs.json()
                if len(jobs) == 0:
                    break
                item_counter = 0
                for item in jobs:
                    try:
                        item = "id: " + str(jobs[item_counter]["id"]) + " status: " + jobs[item_counter]["status"] + " stage: " + jobs[item_counter]["stage"] + " name: " + jobs[item_counter]["name"] + " user_id: " + str(jobs[item_counter]["user"]["id"]) + " username: " + jobs[item_counter]["user"]["username"] + " project_id: " + str(jobs[item_counter]["project"]["id"]) + " web_url: " + jobs[item_counter]["web_url"]
                        jobs_list.append(item)
                        item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(jobs[item_counter]["id"]) + " \033[1;94mstatus\033[1;00m: \033[1;92m" + jobs[item_counter]["status"] + "\033[1;94m stage\033[1;00m: \033[1;92m" + jobs[item_counter]["stage"] + "\033[1;94m name\033[1;00m: \033[1;92m" + jobs[item_counter]["name"] + "\033[1;94m user_id\033[1;00m: \033[1;92m" + str(jobs[item_counter]["user"]["id"]) + "\033[1;94m username\033[1;00m: \033[1;92m" + jobs[item_counter]["user"]["username"] + " \033[1;94mproject_id\033[1;00m: \033[1;92m" + str(jobs[item_counter]["project"]["id"]) + " \033[1;94mweb_url\033[1;00m: \033[1;92m" + jobs[item_counter]["web_url"] + "\033[1;00m"
                        jobs_list_to_print.append(item_to_print)
                    except KeyError:
                        item = "id: " + str(jobs[item_counter]["id"]) + " status: " + jobs[item_counter]["status"] + " stage: " + jobs[item_counter]["stage"] + " name: " + jobs[item_counter]["name"] + " user_id: " + str(jobs[item_counter]["user"]["id"]) + " username: " + jobs[item_counter]["user"]["username"] + " project_id: " + str(jobs[item_counter]["project"]["id"]) + " web_url: " + jobs[item_counter]["web_url"]
                        jobs_list.append(item)
                    item_counter += 1
                time.sleep(0.1)
                page_counter += 1
                 
            for item in set(jobs_list_to_print):
                print(item)

            if not os.path.exists("{}/reports".format(os.getcwd())):
                os.mkdir("{}/reports".format(os.getcwd()))
            runner_jobs_output(runner_id=runner_id, jobs_status=jobs_status)

        else:
            print("\033[1;90m\nCollecting data...\033[1;00m")
            print("\033[1;90mThis may take some time. Be patient..\033[1;00m\n")
            page_counter = 0
            while 1:
                target_jobs = requests.get("{0}/api/v4/runners/{1}/jobs?&status={2}&per_page=100&page={3}".format(gitlab_server_address, runner_id, jobs_status, page_counter), headers=headers)
                jobs = target_jobs.json()
                if len(jobs) == 0:
                    break
                item_counter = 0
                for item in jobs:
                    try:
                        item = "id: " + str(jobs[item_counter]["id"]) + " status: " + jobs[item_counter]["status"] + " stage: " + jobs[item_counter]["stage"] + " name: " + jobs[item_counter]["name"] + " user_id: " + str(jobs[item_counter]["user"]["id"]) + " username: " + jobs[item_counter]["user"]["username"] + " project_id: " + str(jobs[item_counter]["project"]["id"]) + " web_url: " + jobs[item_counter]["web_url"]
                        jobs_list.append(item)
                        item = item_to_print = "\033[1;94mid\033[1;00m: \033[1;92m" + str(jobs[item_counter]["id"]) + " \033[1;94mstatus\033[1;00m: \033[1;92m" + jobs[item_counter]["status"] + "\033[1;94m stage\033[1;00m: \033[1;92m" + jobs[item_counter]["stage"] + "\033[1;94m name\033[1;00m: \033[1;92m" + jobs[item_counter]["name"] + "\033[1;94m user_id\033[1;00m: \033[1;92m" + str(jobs[item_counter]["user"]["id"]) + "\033[1;94m username\033[1;00m: \033[1;92m" + jobs[item_counter]["user"]["username"] + " \033[1;94mproject_id\033[1;00m: \033[1;92m" + str(jobs[item_counter]["project"]["id"]) + " \033[1;94mweb_url\033[1;00m: \033[1;92m" + jobs[item_counter]["web_url"] + "\033[1;00m"
                        jobs_list_to_print.append(item_to_print)
                    except KeyError:
                        item = "id: " + str(jobs[item_counter]["id"]) + " status: " + jobs[item_counter]["status"] + " stage: " + jobs[item_counter]["stage"] + " name: " + jobs[item_counter]["name"] + " user_id: " + str(jobs[item_counter]["user"]["id"]) + " username: " + jobs[item_counter]["user"]["username"] + " project_id: " + str(jobs[item_counter]["project"]["id"]) + " web_url: " + jobs[item_counter]["web_url"]
                        jobs_list.append(item)
                    item_counter += 1
                time.sleep(0.1)
                page_counter += 1
        
            for item in set(jobs_list_to_print):
                print(item)
    
            if not os.path.exists("{}/reports".format(os.getcwd())):
                os.mkdir("{}/reports".format(os.getcwd()))
            runner_jobs_output(runner_id=runner_id, jobs_status=jobs_status)
                
        print("\n{0} jobs amount is \033[1;94m{1}\033[1;00m".format(jobs_status, len(set(jobs_list))))
        print("\nOne can find results in \033[1;95m{}/reports/runner_jobs_info.txt\033[1;00m\n".format(os.getcwd()))

    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr runner ID is not correct\033[1;00m")
    except TypeError:
        print("\033[1;93mRunner with such ID is absent\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
        runner_jobs_output(runner_id, jobs_status)
    except KeyboardInterrupt:
        print("\033[1;93m\nResults not saved!\033[1;00m")

def runner_jobs_output(runner_id, jobs_status):
    with open("{}/reports/runner_jobs_info.txt".format(os.getcwd()), 'a') as output:
        output.write('RUNNER ID {} {} JOBS INFO => \n'.format(runner_id, jobs_status))
        for row in set(jobs_list):
            output.write(str(row) + '\n')
