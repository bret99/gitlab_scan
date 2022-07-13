import requests
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
import os
import sys
import time
from access_tokens import gitlab_access_token, gitlab_server_address

headers = {"PRIVATE-TOKEN": gitlab_access_token}

def get_namespace_info():
    if gitlab_access_token == "":
        print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    elif "http" not in gitlab_server_address:
        print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
        sys.exit()
    try:
        namespace_id = input("Enter namespace ID: ")
        print("\033[1;90m\nCollecting data...\033[1;00m\n")
        target_namespaces = requests.get("{0}/api/v4/namespaces/{1}".format(gitlab_server_address, namespace_id), headers=headers)
        namespaces = target_namespaces.json()
        print(" \033[1;94mid\033[1;00m: \033[1;92m{}\033[1;00m".format(namespaces["id"]))
        print(" \033[1;94mname\033[1;00m: \033[1;92m{}\033[1;00m".format(namespaces["name"]))
        print(" \033[1;94mpath\033[1;00m: \033[1;92m{}\033[1;00m".format(namespaces["path"]))
        print(" \033[1;94mkind\033[1;00m: \033[1;92m{}\033[1;00m".format(namespaces["kind"]))
        print(" \033[1;94mfull_path\033[1;00m: \033[1;92m{}\033[1;00m".format(namespaces["full_path"]))
        print(" \033[1;94mparent_id\033[1;00m: \033[1;92m{}\033[1;00m".format(namespaces["parent_id"]))
        print(" \033[1;94mavatar_url\033[1;00m: \033[1;92m{}\033[1;00m".format(namespaces["avatar_url"]))
        print(" \033[1;94mweb_url\033[1;00m: \033[1;92m{}\033[1;00m".format(namespaces["web_url"]))
    except (InvalidURL, MissingSchema):
        print("\033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr namspace ID is not correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        pass
