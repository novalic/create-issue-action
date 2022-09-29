from helpers import split_input_parameter_list, get_environment_variable


ACCESS_TOKEN = get_environment_variable('INPUT_TOKEN')
REPOSITORY_OWNER, PROJECT_NAME = get_environment_variable('GITHUB_REPOSITORY').split('/')

ISSUE_LABELS = split_input_parameter_list(get_environment_variable('INPUT_LABELS'))
ISSUE_TITLE = get_environment_variable('INPUT_TITLE')
ISSUE_BODY = get_environment_variable('INPUT_BODY')
ISSUE_ASSIGNEES = split_input_parameter_list(get_environment_variable('INPUT_ASSIGNEES'))
ISSUE_MILESTONE = get_environment_variable('INPUT_MILESTONE')
PROJECT_ID = get_environment_variable('INPUT_PROJECT')
