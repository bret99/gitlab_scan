import requests
import sys
from requests.exceptions import InvalidURL, MissingSchema, ConnectionError
from access_tokens import gitlab_access_token, gitlab_server_address

headers = {"PRIVATE-TOKEN": gitlab_access_token}

def get_project_info():
    try:
        try:
            if gitlab_access_token == "":
                print("\nOne should write correct value to \033[1;95mgitlab_access__token \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
                sys.exit()
            elif "http" not in gitlab_server_address:
                print("\nOne should write correct value to \033[1;95mgitlab_server_address \033[1;00min \033[1;95maccess_token.py\033[1;00m!")
                sys.exit()
            project_id = input("Enter project ID: ")
            print("\033[1;90m\nCollecting data...\033[1;00m\n")
            target_project = requests.get("{0}/api/v4/projects/{1}".format(gitlab_server_address, project_id), headers=headers)
            project = target_project.json()
            print(" \033[1;94mid\033[1;00m: \033[1;92m{}\033[1;00m".format(project["id"]))
            print(" \033[1;94mdescription\033[1;00m: \033[1;92m{}\033[1;00m".format(project["description"]))
            print(" \033[1;94mname\033[1;00m: \033[1;92m{}\033[1;00m".format(project["name"]))
            print(" \033[1;94mname_with_namespace\033[1;00m: \033[1;92m{}\033[1;00m".format(project["name_with_namespace"]))
            print(" \033[1;94mpath\033[1;00m: \033[1;92m{}\033[1;00m".format(project["path"]))
            print(" \033[1;94mpath_with_namespace\033[1;00m: \033[1;92m{}\033[1;00m".format(project["path_with_namespace"]))
            print(" \033[1;94mcreated_at\033[1;00m: \033[1;92m{}\033[1;00m".format(project["created_at"]))
            print(" \033[1;94mdefault_branch\033[1;00m: \033[1;92m{}\033[1;00m".format(project["default_branch"]))
            tags_counter = 0
            if len(project["tag_list"]) == 0:
                print("\033[1;94m tag_list\033[1;00m: \033[;00m[]")
            for tags in project["tag_list"]:
                print(" \033[1;94mtag_list\033[1;00m: \033[1;92m{}\033[1;00m".format(project["tag_list"][tags_counter]))
                tags_counter += 1
            topics_counter = 0
            if len(project["topics"]) == 0:
                print(" \033[1;94mtopics\033[1;00m: \033[;00m[]")
            for topics in project["topics"]:
                print(" \033[1;94m   topics\033[1;00m: \033[1;92m{}\033[1;00m".format(project["projects"]["topics"][topics_counter]))
                topics_counter += 1
            print(" \033[1;94mssh_url_to_repo\033[1;00m: \033[1;92m{}\033[1;00m".format(project["ssh_url_to_repo"]))
            print(" \033[1;94mhttp_url_to_repo\033[1;00m: \033[1;92m{}\033[1;00m".format(project["http_url_to_repo"]))
            print(" \033[1;94mweb_url\033[1;00m: \033[1;92m{}\033[1;00m".format(project["web_url"]))
            print(" \033[1;94mreadme_url\033[1;00m: \033[1;92m{}\033[1;00m".format(project["readme_url"]))
            print(" \033[1;94mavatar_url\033[1;00m: \033[1;92m{}\033[1;00m".format(project["avatar_url"]))
            print(" \033[1;94mlast_activity_at\033[1;00m: \033[1;92m{}\033[1;00m".format(project["last_activity_at"]))
            print(" \033[1;94mnamespace\033[1;00m:")
            print(" \033[1;94m   id\033[1;00m: \033[1;92m{}\033[1;00m".format(project["namespace"]["id"]))
            print(" \033[1;94m   name\033[1;00m: \033[1;92m{}\033[1;00m".format(project["namespace"]["name"]))
            print(" \033[1;94m   path\033[1;00m: \033[1;92m{}\033[1;00m".format(project["namespace"]["path"]))
            print(" \033[1;94m   kind\033[1;00m: \033[1;92m{}\033[1;00m".format(project["namespace"]["id"]))
            print(" \033[1;94m   full_path\033[1;00m: \033[1;92m{}\033[1;00m".format(project["namespace"]["full_path"]))
            print(" \033[1;94m   parent_id\033[1;00m: \033[1;92m{}\033[1;00m".format(project["namespace"]["parent_id"]))
            print(" \033[1;94m   web_url\033[1;00m: \033[1;92m{}\033[1;00m".format(project["namespace"]["web_url"]))
            print(" \033[1;94m_links\033[1;00m:")
            print(" \033[1;94m   self\033[1;00m: \033[1;92m{}\033[1;00m".format(project["_links"]["self"]))
            print(" \033[1;94m   issues\033[1;00m: \033[1;92m{}\033[1;00m".format(project["_links"]["issues"]))
            print(" \033[1;94m   merge_requests\033[1;00m: \033[1;92m{}\033[1;00m".format(project["_links"]["merge_requests"]))
            print(" \033[1;94m   repo_branches\033[1;00m: \033[1;92m{}\033[1;00m".format(project["_links"]["repo_branches"]))
            print(" \033[1;94m   labels\033[1;00m: \033[1;92m{}\033[1;00m".format(project["_links"]["labels"]))
            print(" \033[1;94m   events\033[1;00m: \033[1;92m{}\033[1;00m".format(project["_links"]["events"]))
            print(" \033[1;94m   members\033[1;00m: \033[1;92m{}\033[1;00m".format(project["_links"]["members"]))
            print(" \033[1;94mpackages_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["packages_enabled"]))
            print(" \033[1;94mempty_repo\033[1;00m: \033[1;92m{}\033[1;00m".format(project["empty_repo"]))
            print(" \033[1;94marchived\033[1;00m: \033[1;92m{}\033[1;00m".format(project["archived"]))
            print(" \033[1;94mvisibility\033[1;00m: \033[1;92m{}\033[1;00m".format(project["visibility"]))
            print(" \033[1;94mresolve_outdated_diff_discussions\033[1;00m: \033[1;92m{}\033[1;00m".format(project["resolve_outdated_diff_discussions"]))
            print(" \033[1;94mcontainer_expiration_policy\033[1;00m:")
            print(" \033[1;94m   cadence\033[1;00m: \033[1;92m{}\033[1;00m".format(project["container_expiration_policy"]["cadence"]))
            print(" \033[1;94m   enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["container_expiration_policy"]["enabled"]))
            print(" \033[1;94m   keep_n\033[1;00m: \033[1;92m{}\033[1;00m".format(project["container_expiration_policy"]["keep_n"]))
            print(" \033[1;94m   older_than\033[1;00m: \033[1;92m{}\033[1;00m".format(project["container_expiration_policy"]["older_than"]))
            print(" \033[1;94m   next_run_at\033[1;00m: \033[1;92m{}\033[1;00m".format(project["container_expiration_policy"]["next_run_at"]))
            print(" \033[1;94missues_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["issues_enabled"]))
            print(" \033[1;94mmerge_requests_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["merge_requests_enabled"]))
            print(" \033[1;94mwiki_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["wiki_enabled"]))
            print(" \033[1;94mjobs_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["jobs_enabled"]))
            print(" \033[1;94msnippets_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["snippets_enabled"]))
            print(" \033[1;94mcontainer_registry_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["container_registry_enabled"]))
            print(" \033[1;94mservice_desk_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["service_desk_enabled"]))
            print(" \033[1;94mservice_desk_address\033[1;00m: \033[1;92m{}\033[1;00m".format(project["service_desk_address"]))
            print(" \033[1;94mcan_create_merge_request_in\033[1;00m: \033[1;92m{}\033[1;00m".format(project["can_create_merge_request_in"]))
            print(" \033[1;94missues_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["issues_access_level"]))
            print(" \033[1;94mrepository_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["repository_access_level"]))
            print(" \033[1;94mmerge_requests_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["merge_requests_access_level"]))
            print(" \033[1;94mforking_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["forking_access_level"]))
            print(" \033[1;94mwiki_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["wiki_access_level"]))
            print(" \033[1;94mbuilds_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["builds_access_level"]))
            print(" \033[1;94msnippets_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["snippets_access_level"]))
            print(" \033[1;94mpages_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["pages_access_level"]))
            print(" \033[1;94moperations_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["operations_access_level"]))
            print(" \033[1;94manalytics_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["analytics_access_level"]))
            print(" \033[1;94mcontainer_registry_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["container_registry_access_level"]))
            print(" \033[1;94msecurity_and_compliance_access_level\033[1;00m: \033[1;92m{}\033[1;00m".format(project["security_and_compliance_access_level"]))
            print(" \033[1;94memails_disabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["emails_disabled"]))
            print(" \033[1;94mshared_runners_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["shared_runners_enabled"]))
            print(" \033[1;94mlfs_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["lfs_enabled"]))
            print(" \033[1;94mcreator_id\033[1;00m: \033[1;92m{}\033[1;00m".format(project["creator_id"]))
            print(" \033[1;94mimport_status\033[1;00m: \033[1;92m{}\033[1;00m".format(project["import_status"]))
            print(" \033[1;94mimport_error\033[1;00m: \033[1;92m{}\033[1;00m".format(project["import_error"]))
            print(" \033[1;94mopen_issues_count\033[1;00m: \033[1;92m{}\033[1;00m".format(project["open_issues_count"]))
            print(" \033[1;94mrunners_token\033[1;00m: \033[1;92m{}\033[1;00m".format(project["runners_token"]))
            print(" \033[1;94mci_default_git_depth\033[1;00m: \033[1;92m{}\033[1;00m".format(project["ci_default_git_depth"]))
            print(" \033[1;94mci_forward_deployment_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["ci_forward_deployment_enabled"]))
            print(" \033[1;94mci_job_token_scope_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["ci_job_token_scope_enabled"]))
            print(" \033[1;94mpublic_jobs\033[1;00m: \033[1;92m{}\033[1;00m".format(project["public_jobs"]))
            print(" \033[1;94mbuild_git_strategy\033[1;00m: \033[1;92m{}\033[1;00m".format(project["build_git_strategy"]))
            print(" \033[1;94mbuild_timeout\033[1;00m: \033[1;92m{}\033[1;00m".format(project["build_timeout"]))
            print(" \033[1;94mauto_cancel_pending_pipelines\033[1;00m: \033[1;92m{}\033[1;00m".format(project["auto_cancel_pending_pipelines"]))
#            print(" \033[1;94mbuild_coverage_regex\033[1;00m: \033[1;92m{}\033[1;00m".format(project["build_coverage_regex"]))
            print(" \033[1;94mci_config_path\033[1;00m: \033[1;92m{}\033[1;00m".format(project["ci_config_path"]))
            shared_with_groups_counter = 0
            if len(project["shared_with_groups"]) == 0:
                print(" \033[1;94mshared_with_groups\033[1;00m: \033[;00m[]")
            for tags in project["shared_with_groups"]:
                print(" \033[1;94mshared_with_groups\033[1;00m: \033[1;92m{}\033[1;00m".format(project["shared_with_groups"][shared_with_groups_counter]))
                shared_with_groups_counter += 1
            print(" \033[1;94monly_allow_merge_if_pipeline_succeeds\033[1;00m: \033[1;92m{}\033[1;00m".format(project["only_allow_merge_if_pipeline_succeeds"]))
            print(" \033[1;94mallow_merge_on_skipped_pipeline\033[1;00m: \033[1;92m{}\033[1;00m".format(project["allow_merge_on_skipped_pipeline"]))
            print(" \033[1;94mrestrict_user_defined_variables\033[1;00m: \033[1;92m{}\033[1;00m".format(project["restrict_user_defined_variables"]))
            print(" \033[1;94mrequest_access_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["request_access_enabled"]))
            print(" \033[1;94monly_allow_merge_if_all_discussions_are_resolved\033[1;00m: \033[1;92m{}\033[1;00m".format(project["only_allow_merge_if_all_discussions_are_resolved"]))
            print(" \033[1;94mremove_source_branch_after_merge\033[1;00m: \033[1;92m{}\033[1;00m".format(project["remove_source_branch_after_merge"]))
            print(" \033[1;94mprinting_merge_request_link_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["printing_merge_request_link_enabled"]))
            print(" \033[1;94mmerge_method\033[1;00m: \033[1;92m{}\033[1;00m".format(project["merge_method"]))
            print(" \033[1;94msquash_option\033[1;00m: \033[1;92m{}\033[1;00m".format(project["squash_option"]))
            print(" \033[1;94msuggestion_commit_message\033[1;00m: \033[1;92m{}\033[1;00m".format(project["suggestion_commit_message"]))
            print(" \033[1;94mmerge_commit_template\033[1;00m: \033[1;92m{}\033[1;00m".format(project["merge_commit_template"]))
            print(" \033[1;94msquash_commit_template\033[1;00m: \033[1;92m{}\033[1;00m".format(project["squash_commit_template"]))
            print(" \033[1;94mauto_devops_enabled\033[1;00m: \033[1;92m{}\033[1;00m".format(project["auto_devops_enabled"]))
            print(" \033[1;94mauto_devops_deploy_strategy\033[1;00m: \033[1;92m{}\033[1;00m".format(project["auto_devops_deploy_strategy"]))
            print(" \033[1;94mautoclose_referenced_issues\033[1;00m: \033[1;92m{}\033[1;00m".format(project["autoclose_referenced_issues"]))
            print(" \033[1;94mrepository_storage\033[1;00m: \033[1;92m{}\033[1;00m".format(project["repository_storage"]))
            print(" \033[1;94mkeep_latest_artifact\033[1;00m: \033[1;92m{}\033[1;00m".format(project["keep_latest_artifact"]))
            print(" \033[1;94mrunner_token_expiration_interval\033[1;00m: \033[1;92m{}\033[1;00m".format(project["runner_token_expiration_interval"]))
            print(" \033[1;94mpermissions\033[1;00m: \033[1;92m\033[1;00m")
            print(" \033[1;94m   project_access\033[1;00m: \033[1;92m{}\033[1;00m".format(project["permissions"]["project_access"]))
            print(" \033[1;94m   group_access\033[1;00m: \033[1;92m{}\033[1;00m".format(project["permissions"]["group_access"]))
        except KeyError:
            pass
    except (InvalidURL, MissingSchema):
        print(" \033[1;93mCheck one's Gitlab server link in access_tokens.py is correct\033[1;00m")
    except KeyError:
        print("\033[1;93mCheck one's Gitlab access token in \033[1;95maccess_tokens.py \033[1;93mis correct\033[1;00m")
        print("\033[1;93mOr project ID is not correct\033[1;00m")
    except ConnectionError:
        print("\033[1;93mCheck network connection or Gitlab server status!\033[1;00m")
    except KeyboardInterrupt:
        pass
