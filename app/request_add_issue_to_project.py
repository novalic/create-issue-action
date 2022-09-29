from request_generic_graphql import graphql_request


def add_issue_to_project_graphql(project_node_id: str, issue_node_id: str) -> str:
    query = f'mutation {{addProjectV2ItemById(input: {{projectId: "{project_node_id}" contentId: "{issue_node_id}"}})' \
            f' {{item {{id}}}}}}'

    response = graphql_request('POST', query)

    match response.status_code:
        case 200:
            response_data = response.json()
            try:
                node_id = response_data['data']['addProjectV2ItemById']['item']['id']
            except Exception as exc:
                raise Exception(
                    f'Could not add issue to project.\n'
                    f'Exception: {exc}\n'
                    f'Response: {response_data}'
                )
        case status_code:
            raise Exception(f'Could not issue to project. Status code: {status_code}')

    return node_id



