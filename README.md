# JiraIntegration
## General information
Application written in Python, creating issues in Jira, from a variety of sources.
### Projekty
1. Creating an issue in Jira, based on the received json from the url link
2. They will appear as needed

## Documentation
The application uses Jiry's REST API.
[Description of Jira REST API v3](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/),
[v2](https://docs.atlassian.com/software/jira/docs/api/REST/latest/)
### Requirements
Python 3.6 with packets *requirements.txt* 
### */conf/** - configuration files
Every proper configuration file is invisible for obvious reasons.
Instead, there are sample files with the note *_example* e.g:
* */jira_integration/jira_conf.py* - the file contains the connection configuration to Jira
