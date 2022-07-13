import requests
import sys
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
from access_tokens import gitlab_access_token, gitlab_server_address

headers = {"PRIVATE-TOKEN": gitlab_access_token}

def get_runner_info():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        runner_id = input("Enter runner ID: ")
        print("\033[1;90m\nCollecting data...\033[1;00m\n")
        target_runner = requests.get("{0}/api/v4/runners/{1}".format(gitlab_server_address, runner_id), headers=headers)
        runner = target_runner.json()
        print(" \033[1;94mid\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["id"]))
        print(" \033[1;94mdescription\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["description"]))
        print(" \033[1;94mip_address\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["ip_address"]))
        print(" \033[1;94mactive\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["active"]))
        print(" \033[1;94mpaused\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["paused"]))
        print(" \033[1;94mis_shared\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["is_shared"]))
        print(" \033[1;94mrunner_type\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["runner_type"]))
        print(" \033[1;94mname\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["name"]))
        print(" \033[1;94monline\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["online"]))
        print(" \033[1;94mstatus\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["status"]))
        print(" \033[1;94mrun_untagged\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["run_untagged"]))
        print(" \033[1;94mlocked\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["locked"]))
        print(" \033[1;94mmaximum_timeout\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["maximum_timeout"]))
        print(" \033[1;94maccess_level\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["access_level"]))
        print(" \033[1;94mversion\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["version"]))
        print(" \033[1;94mrevision\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["revision"]))
        print(" \033[1;94mplatform\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["platform"]))
        print(" \033[1;94marchitecture\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["architecture"]))
        print(" \033[1;94mcontacted_at\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["contacted_at"]))
        print(" \033[1;94mprojects\033[1;00m:")
        projects_counter = 0
        if len(runner["projects"]) == 0:
            print(" \033[1;94mprojects\033[1;00m: \033[;00m[]")
        for projects in runner["projects"]:
            print(" \033[1;94m   id\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["id"]))
            print(" \033[1;94m   description\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["description"]))
            print(" \033[1;94m   name\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["name"]))
            print(" \033[1;94m   name_with_namespace\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["name_with_namespace"]))
            print(" \033[1;94m   path\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["path"]))
            print(" \033[1;94m   path_with_namespace\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["path_with_namespace"]))
            print(" \033[1;94m   created_at\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["created_at"]))
            print(" \033[1;94m   default_branch\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["default_branch"]))
            tags_counter = 0
            if len(runner["projects"][projects_counter]["tag_list"]) == 0:
                print(" \033[1;94m   tag_list\033[1;00m: \033[;00m[]")
            for tags in runner["projects"][projects_counter]["tag_list"]:
                print(" \033[1;94m   tag_list\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["tag_list"][tags_counter]))
                tags_counter += 1
            topics_counter = 0
            if len(runner["projects"][projects_counter]["topics"]) == 0:
                print(" \033[1;94m   topics\033[1;00m: \033[;00m[]")
            for topics in runner["projects"][projects_counter]["topics"]:
                print(" \033[1;94m   topics\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["topics"][topics_counter]))
                topics_counter += 1
            print(" \033[1;94m   ssh_url_to_repo\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["ssh_url_to_repo"]))
            print(" \033[1;94m   http_url_to_repo\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["http_url_to_repo"]))
            print(" \033[1;94m   web_url\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["web_url"]))
            print(" \033[1;94m   forks_count\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["forks_count"]))
            print(" \033[1;94m   star_count\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["star_count"]))
            print(" \033[1;94m   last_activity_at\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["last_activity_at"]))
            print(" \033[1;94m   namespace\033[1;00m:")
            print(" \033[1;94m       id\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["namespace"]["id"]))
            print(" \033[1;94m       path\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["namespace"]["path"]))
            print(" \033[1;94m       kind\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["namespace"]["kind"]))
            print(" \033[1;94m       full_path\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["namespace"]["full_path"]))
            print(" \033[1;94m       parent_id\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["namespace"]["parent_id"]))
            print(" \033[1;94m       web_url\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["projects"][projects_counter]["namespace"]["web_url"]))
            projects_counter += 1
        groups_counter = 0
        if len(runner["groups"]) == 0:
            print(" \033[1;94mgroups\033[1;00m: \033[;00m[]")
        for groups in runner["groups"]:
            print(" \033[1;94mgroups\033[1;00m: \033[1;92m{}\033[1;00m".format(runner["groups"][groups_counter]))
            groups_counter += 1
    except (InvalidURL, MissingSchema):
        print(" \033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr runner ID is not correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        pass
