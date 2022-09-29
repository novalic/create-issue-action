import json
import requests

from constants import ACCESS_TOKEN


GITHUB_GRAPHQL_API_URL = 'https://api.github.com/graphql'


def graphql_request(http_verb, query) -> requests.Response:
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Accept': 'application/vnd.github+json'
    }
    project_data = {
        'query': query
    }
    payload = json.dumps(project_data)

    response = requests.request(
        http_verb,
        GITHUB_GRAPHQL_API_URL,
        data=payload,
        headers=headers
    )
    return response
