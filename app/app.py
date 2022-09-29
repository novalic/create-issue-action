import logging

from request_add_issue_to_project import add_issue_to_project_graphql
from request_create_issue import create_github_issue
from request_get_issue_node_id import get_issue_node_id_graphql
from request_get_project_node_id import get_project_node_id_graphql

from constants import (
    ISSUE_ASSIGNEES,
    ISSUE_BODY,
    ISSUE_LABELS,
    ISSUE_MILESTONE,
    ISSUE_TITLE,
    PROJECT_ID
)

logger = logging.getLogger(__name__)


def main():
    issue_id = create_github_issue(
        ISSUE_TITLE,
        ISSUE_LABELS,
        ISSUE_ASSIGNEES,
        body=ISSUE_BODY,
        milestone=ISSUE_MILESTONE
    )
    logger.info(f'Successfully created issue {ISSUE_TITLE}.')

    if PROJECT_ID:
        project_node_id = get_project_node_id_graphql()
        logger.info(f'Successfully obtained the project node id for project {PROJECT_ID}.')

        issue_node_id = get_issue_node_id_graphql(issue_id)
        logger.info(f'Successfully obtained the issue node id for issue {issue_id}.')

        _ = add_issue_to_project_graphql(project_node_id, issue_node_id)
        logger.info(f'Successfully added issue {ISSUE_TITLE} to project #{PROJECT_ID}.')


if __name__ == "__main__":
    logger.info('Starting execution...')
    main()
    logger.info('Execution finished :)')
