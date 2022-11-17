import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
from access_tokens import gitlab_access_token, gitlab_server_address

headers = {"PRIVATE-TOKEN": gitlab_access_token}

def get_user_info():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        user_id = input("Enter user ID: ")
        print("\033[1;90m\nCollecting data...\033[1;00m\n")
        target_user = requests.get("{0}/api/v4/users/{1}".format(gitlab_server_address, user_id), headers=headers)
        user = target_user.json()
        print(" \033[1;94mid\033[1;00m: \033[1;92m{}\033[1;00m".format(user["id"]))
        print(" \033[1;94musername\033[1;00m: \033[1;92m{}\033[1;00m".format(user["username"]))
        print(" \033[1;94mname\033[1;00m: \033[1;92m{}\033[1;00m".format(user["name"]))
        print(" \033[1;94mstate\033[1;00m: \033[1;92m{}\033[1;00m".format(user["state"]))
        print(" \033[1;94mavatar_url\033[1;00m: \033[1;92m{}\033[1;00m".format(user["avatar_url"]))
        print(" \033[1;94mweb_url\033[1;00m: \033[1;92m{}\033[1;00m".format(user["web_url"]))
        print(" \033[1;94mcreated_at\033[1;00m: \033[1;92m{}\033[1;00m".format(user["created_at"]))
        print(" \033[1;94mbio\033[1;00m: \033[1;92m{}\033[1;00m".format(user["bio"]))
        print(" \033[1;94mlocation\033[1;00m: \033[1;92m{}\033[1;00m".format(user["location"]))
        print(" \033[1;94mpublic_email\033[1;00m: \033[1;92m{}\033[1;00m".format(user["public_email"]))
        print(" \033[1;94mskype\033[1;00m: \033[1;92m{}\033[1;00m".format(user["skype"]))
        print(" \033[1;94mlinkedin\033[1;00m: \033[1;92m{}\033[1;00m".format(user["linkedin"]))
        print(" \033[1;94mtwitter\033[1;00m: \033[1;92m{}\033[1;00m".format(user["twitter"]))
        print(" \033[1;94mwebsite_url\033[1;00m: \033[1;92m{}\033[1;00m".format(user["website_url"]))
        print(" \033[1;94morganization\033[1;00m: \033[1;92m{}\033[1;00m".format(user["organization"]))
        print(" \033[1;94mjob_title\033[1;00m: \033[1;92m{}\033[1;00m".format(user["job_title"]))
        print(" \033[1;94mpronouns\033[1;00m: \033[1;92m{}\033[1;00m".format(user["pronouns"]))
        print(" \033[1;94mbot\033[1;00m: \033[1;92m{}\033[1;00m".format(user["bot"]))
        print(" \033[1;94mwork_information\033[1;00m: \033[1;92m{}\033[1;00m".format(user["work_information"]))
        print(" \033[1;94mfollowers\033[1;00m: \033[1;92m{}\033[1;00m".format(user["followers"]))
        print(" \033[1;94mfollowing\033[1;00m: \033[1;92m{}\033[1;00m".format(user["following"]))
        print(" \033[1;94mlocal_time\033[1;00m: \033[1;92m{}\033[1;00m".format(user["local_time"]))
        print(" \033[1;94mlast_sign_in_at\033[1;00m: \033[1;92m{}\033[1;00m".format(user["last_sign_in_at"]))
        print(" \033[1;94mconfirmed_at\033[1;00m: \033[1;92m{}\033[1;00m".format(user["confirmed_at"]))
        print(" \033[1;94mlast_activity_on\033[1;00m: \033[1;92m{}\033[1;00m".format(user["last_activity_on"]))
        print(" \033[1;94memail\033[1;00m: \033[1;92m{}\033[1;00m".format(user["email"]))
        print(" \033[1;94mtheme_id\033[1;00m: \033[1;92m{}\033[1;00m".format(user["theme_id"]))
        print(" \033[1;94mcolor_scheme_id\033[1;00m: \033[1;92m{}\033[1;00m".format(user["color_scheme_id"]))
        print(" \033[1;94mprojects_limit\033[1;00m: \033[1;92m{}\033[1;00m".format(user["projects_limit"]))
        print(" \033[1;94mcurrent_sign_in_at\033[1;00m: \033[1;92m{}\033[1;00m".format(user["current_sign_in_at"]))
        print(" \033[1;94midentities\033[1;00m:")
        try:
            identities_counter = 0
            if len(user["identities"]) == 0:
                print(" \033[1;94midentities\033[1;00m: \033[;00m[]")
            for identities in user["identities"]:
                print(" \033[1;94m  provider\033[1;00m: \033[1;92m{}\033[1;00m".format(user["identities"][identities_counter]["provider"]))
                print(" \033[1;94m  extern_uid\033[1;00m: \033[1;92m{}\033[1;00m".format(user["identities"][identities_counter]["extern_uid"]))
                identities_counter += 1
        except KeyError:
            pass
        print(" \033[1;94mcan_create_group\033[1;00m: \033[1;92m{}\033[1;00m".format(user["can_create_group"]))
        print(" \033[1;94mcan_create_project\033[1;00m: \033[1;92m{}\033[1;00m".format(user["can_create_project"]))
        print(" \033[1;94mtwo_factor_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(user["two_factor_enabled"]))
        print(" \033[1;94mexternal\033[1;00m: \033[1;92m{}\033[1;00m".format(user["external"]))
        print(" \033[1;94mprivate_profile\033[1;00m: \033[1;92m{}\033[1;00m".format(user["private_profile"]))
        print(" \033[1;94mcommit_email\033[1;00m: \033[1;92m{}\033[1;00m".format(user["commit_email"]))
        print(" \033[1;94mis_admin\033[1;00m: \033[1;92m{}\033[1;00m".format(user["is_admin"]))
        print(" \033[1;94mnote\033[1;00m: \033[1;92m{}\033[1;00m".format(user["note"]))
        print(" \033[1;94mhighest_role\033[1;00m: \033[1;92m{}\033[1;00m".format(user["highest_role"]))
        print(" \033[1;94mcurrent_sign_in_ip\033[1;00m: \033[1;92m{}\033[1;00m".format(user["current_sign_in_ip"]))
        print(" \033[1;94mlast_sign_in_ip\033[1;00m: \033[1;92m{}\033[1;00m".format(user["last_sign_in_ip"]))
        print(" \033[1;94msign_in_count\033[1;00m: \033[1;92m{}\033[1;00m".format(user["sign_in_count"]))
        print(" \033[1;94mnamespace_id\033[1;00m: \033[1;92m{}\033[1;00m".format(user["namespace_id"]))
        print(" \033[1;94mcreated_by\033[1;00m: \033[1;92m{}\033[1;00m".format(user["created_by"]))
    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr user ID is not correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        pass
