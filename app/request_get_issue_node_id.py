from constants import REPOSITORY_OWNER, PROJECT_NAME
from request_generic_graphql import graphql_request


def get_issue_node_id_graphql(issue_id: int) -> str:
    query = f'{{repository(name: "{PROJECT_NAME}", owner: "{REPOSITORY_OWNER}") ' \
            f'{{issue1: issue(number: {issue_id}) {{id}}}}}}'

    response = graphql_request('POST', query)

    match response.status_code:
        case 200:
            response_data = response.json()
            try:
                node_id = response_data['data']['repository']['issue1']['id']
            except Exception as exc:
                raise Exception(
                    f'Could not obtain issue node id.\n'
                    f'Exception: {exc}\n'
                    f'Response: {response_data}'
                )
        case status_code:
            raise Exception(f'Could not obtain issue node id. Status code: {status_code}')

    return node_id
