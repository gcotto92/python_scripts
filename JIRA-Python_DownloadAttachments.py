from jira import JIRA

def download_attachment():
    #Enter JIRA Username
    username = ''
    #Enter JIRA UserAPIToken
    apitoken = ''
    download_folder = input('Enter the folder to download the attachments to:\n')
    #Enter JIRA URL
    server = 'https://rostermonster.atlassian.net/'
    #issue_key = 'CO-4359'
    issue_key = input('Enter the ticket number:\n')

    jira = JIRA(basic_auth=(username,apitoken),options={'server':server})
    issue = jira.issue(issue_key,fields='summary,comment,attachment')

    for attachment in issue.fields.attachment:
        with open(download_folder + '%s' % (attachment.filename), 'wb') as file:
            file.write(attachment.get())

process = True 
begin_input = input('Enter "Y" to begin the process:\n')

while process == True:
    if begin_input == 'Y':
        download_attachment()
    process_input = input('Need to process the script again?\nEnter "Y" or "N":\n')
    if process_input == 'Y':
        download_attachment()

    else:
        process = False

else:
    print('"Y" was not selected\nExiting the script...')

