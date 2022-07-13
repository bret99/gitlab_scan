import requests
import sys
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
from access_tokens import gitlab_access_token, gitlab_server_address

headers = {"PRIVATE-TOKEN": gitlab_access_token}

def get_hook_info():
    try:
        if gitlab_access_token == "":
            print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
            sys.exit()
        elif "http" not in gitlab_server_address:
            print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
            sys.exit()
        project_id = input("Enter project ID: ")
        hook_id = input("Enter hook ID: ")
        print("\033[1;90m\nCollecting data...\033[1;00m\n")
        target_hook = requests.get("{0}/api/v4/projects/{1}/hooks/{2}".format(gitlab_server_address, project_id, hook_id), headers=headers)
        hook = target_hook.json()
        print(" \033[1;94mid\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["id"]))
        print(" \033[1;94murl\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["url"]))
        print(" \033[1;94mcreated_at\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["created_at"]))
        print(" \033[1;94mpush_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["push_events"]))
        print(" \033[1;94mtag_push_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["tag_push_events"]))
        print(" \033[1;94mmerge_requests_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["merge_requests_events"]))
        print(" \033[1;94mrepository_update_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["repository_update_events"]))
        print(" \033[1;94menable_ssl_verification\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["enable_ssl_verification"]))
        print(" \033[1;94mproject_idd\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["project_id"]))
        print(" \033[1;94missues_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["issues_events"]))
        print(" \033[1;94mconfidential_issues_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["confidential_issues_events"]))
        print(" \033[1;94mnote_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["note_events"]))
        print(" \033[1;94mconfidential_note_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["confidential_note_events"]))
        print(" \033[1;94mpipeline_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["pipeline_events"]))
        print(" \033[1;94mwiki_page_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["wiki_page_events"]))
        print(" \033[1;94mdeployment_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["deployment_events"]))
        print(" \033[1;94mjob_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["job_events"]))
        print(" \033[1;94mreleases_events\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["releases_events"]))
        print(" \033[1;94mpush_events_branch_filter\033[1;00m: \033[1;92m{}\033[1;00m".format(hook["push_events_branch_filter"]))
    except (InvalidURL, MissingSchema):
        print(" \033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr project\033[1;00m/\033[1;93mhook ID is not correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        pass
