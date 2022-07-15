import sys
import os
from get_users import get_users
from get_user_info import get_user_info
from get_users_IPs import get_users_IPs
from get_namespaces import get_namespaces
from get_namespace_info import get_namespace_info
from get_projects import get_projects
from get_project_info import get_project_info
from get_project_users import get_project_users
from get_project_hooks import get_project_hooks
from get_hook_info import get_hook_info
from get_runners import get_runners
from get_runner_info import get_runner_info
from get_runner_jobs import get_runner_jobs
from get_runners_IPs import get_runners_IPs
from search import get_search

def main_menu():
    try:
        print(
            "\033[1;91m\nGitlab Scanner \033[1;00mmodules:\n\n[\033[1;91m1\033[1;00m] Get users\n\033[1;00m[\033[1;91m2\033[1;00m] Get user info\n\033[1;00m[\033[1;91m3\033[1;00m] Get users IPs\n\033[1;00m[\033[1;91m4\033[1;00m] Get namespaces\n\033[1;00m[\033[1;91m5\033[1;00m] Get namespace info\033[1;00m\n[\033[1;91m6\033[1;00m] Get projects\033[1;00m\n[\033[1;91m7\033[1;00m] Get project info\033[1;00m\n[\033[1;91m8\033[1;00m] Get project users\n\033[1;00m[\033[1;91m9\033[1;00m] Get project hooks\n\033[1;00m[\033[1;91m10\033[1;00m] Get hook info\n\033[1;00m[\033[1;91m11\033[1;00m] Get runners\n\033[1;00m[\033[1;91m12\033[1;00m] Get runner info\n\033[1;00m[\033[1;91m13\033[1;00m] Get runner jobs\n\033[1;00m[\033[1;91m14\033[1;00m] Get runners IPs\n\033[1;00m[\033[1;91m15\033[1;00m] Search\n\033[1;00m[\033[1;91m99\033[1;00m]\033[1;90m Exit\033[1;00m\n"
        )
        choose_module = input("Enter module number: ")
        if choose_module == "1":
            get_users()
            main_menu()
        elif choose_module == "2":
            get_user_info()
            main_menu()
        elif choose_module == "3":
            get_users_IPs()
            main_menu()
        elif choose_module == "4":
            get_namespaces()
            main_menu()
        elif choose_module == "5":
            get_namespace_info()
            main_menu()
        elif choose_module == "6":
            get_projects()
            main_menu()
        elif choose_module == "7":
            get_project_info()
            main_menu()
        elif choose_module == "8":
            get_project_users()
            main_menu()
        elif choose_module == "9":
            get_project_hooks()
            main_menu()
        elif choose_module == "10":
            get_hook_info()
            main_menu()
        elif choose_module == "11":
            get_runners()
            main_menu()
        elif choose_module == "12":
            get_runner_info()
            main_menu()
        elif choose_module == "13":
            get_runner_jobs()
            main_menu()
        elif choose_module == "14":
            get_runners_IPs()
            main_menu()
        elif choose_module == "15":
            get_search()
            main_menu()
        elif choose_module == "99":
            sys.exit()
        else:
            sys.exit("\033[1;93mWrong input!\033[1;00m")
    except KeyboardInterrupt:
        sys.exit()


main_menu()
