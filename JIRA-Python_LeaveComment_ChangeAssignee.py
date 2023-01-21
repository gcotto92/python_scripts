from jira import JIRA 
from jira.resources import User

process_function = True 

def jira_function():
    jiraOptions = {'server' : "https://rostermonster.atlassian.net/"}

    email_auth = input('Enter the email associated with the JIRA account:\n')
    api_token_auth = input('Enter the API token associated with the JIRA account:\n')
    jira = JIRA(options=jiraOptions, basic_auth=(f"{email_auth}",f"{api_token_auth}"))
    ticket_input = input('Enter the ticket number:\n')
    comment_input = input('Enter the comment to place on the ticket:\n')
    assignee_input = input('Enter the assignee username:\n')
    singleIssue = jira.issue(f'{ticket_input}')
    print('{}: {}:{}'.format(singleIssue.key,
                             singleIssue.fields.summary,
                             singleIssue.fields.reporter.displayName))
    comment_send = jira.add_comment(ticket_input,f"{comment_input}")


    #Change Assignee
    jira_connection = JIRA (
        basic_auth=(f'{email_auth}', f'{api_token_auth}'),
        server='https://rostermonster.atlassian.net/'
    )

    issue = singleIssue

    params = {
        "query": f"{assignee_input}@rostermonster.com",
        "includeActive": True,
        "includeInactive": False,
    }    

    list_search = jira_connection._fetch_pages(
        User, None, "user/search", params=params
    )

    jira_user_id = list_search[0].accountId

    fields = {"assignee": {"accountId": jira_user_id}}
    issue.update(assignee=fields["assignee"])


jira_function_input = input('Enter "Y" to begin the jira function process\nEnter "N" to exit:\n')

if jira_function_input == 'Y':
    jira_function()
    process_cont = input('Does the process need to be continued?\nEnter "Y" or "N":\n')
    if process_cont == 'Y':
        jira_function()

    else:
        print('Exiting the program...')

if jira_function_input == 'N':
    process_function = False
    print('Exiting the program:')