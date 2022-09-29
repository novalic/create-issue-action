import json
import requests

from typing import List, Optional

from constants import ACCESS_TOKEN, REPOSITORY_OWNER, PROJECT_NAME


def create_github_issue(
        title: str,
        labels: List[str],
        assignees: List[str],
        /,
        *,
        body: Optional[str] = None,
        milestone: Optional[int | str] = None) -> int:

    create_issue_url = f'https://api.github.com/repos/{REPOSITORY_OWNER}/{PROJECT_NAME}/issues'

    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Accept': 'application/vnd.github+json'
    }

    issue_data = {
        'title': title,
        'body': body,
        'assignees': assignees,
        'milestone': milestone,
        'labels': labels
    }

    payload = json.dumps(issue_data)

    response = requests.request(
        'POST',
        create_issue_url,
        data=payload,
        headers=headers
    )

    match response.status_code:
        case 201:
            return response.json()['number']
        case status_code:
            raise Exception(
                f'Could not create issue:\n'
                f'Status code: {status_code}\n'
                f'Response: {response.content}'
            )


