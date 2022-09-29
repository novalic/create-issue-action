# Create Issue Action
This will let you create an issue and add it to a project based on user input from your GitHub Workflow

## Inputs

- title (**Required**) - Title of the issue
- token (**Required**) - Token of user that will create issue
- assignees (**Not Required**) - Assignes of the issue
- labels (**Not Required**) - Labels of the issue
- body (**Not Required**) - Body of the issue
- milestone (**Not Required**) - Id of the milestone to be assigned to the issue. The milestone must exist in the repository.
- project (**Not Required**) - Id of the project where you want to place the issue. The project must exist in the repository.




## Usages

For each issue you want to create, you can add the following in your workflow's step:

1. Create an issue that is assigned to a milestone and added to a project:
```yaml
- uses: novalic/app-action@v2.0
  name: Create Issue Action
  with:
    title: Deploy to production on {{ date | date('ddd, MMM Do, Y') }}
    token: ${{secrets.GITHUB_TOKEN}}
    assignees: ${{github.actor}}
    labels: Deployments
    body: Be careful.
    milestone: 1
    project: 1
```

2. Create an issue that will not be assigned to milestone nor added to a project:
```yaml
- uses: novalic/app-action@v2.0
  name: Create Issue Action
  with:
    title: Monitoring after deployment.
    token: ${{secrets.GITHUB_TOKEN}}
    assignees: ${{github.actor}}
    labels: Monitoring, Deployments
    body: Check for alarms, Sentry, logs.
```

3. You can of course add your issue to a project and do not assign it to a milestone and vice-versa.


4. A full worflow example:
```yaml
name: Create an issue everyday at 6 AM

on:
  schedule:
    - cron: '0 6 * * *'

jobs:
  create_issue:
    runs-on: ubuntu-latest
    steps:
    - uses: novalic/app-action@v2.0
      name: Create Issue Action
      with:
        title: Wake up!
        token: ${{secrets.GITHUB_TOKEN}}
        assignees: ${{github.actor}}
        labels: Morning Routine, High Priority, Difficulty Level Hard
        body: You should have gone to bed earlier.
        milestone: 1
        project: 1
```

