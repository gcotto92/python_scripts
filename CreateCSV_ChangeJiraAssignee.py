import pandas as pd
import glob
from jira import JIRA 
from jira.resources import User

#Takes the path for the folder that contains the excel files to combine
tickets_path = 'C:/Users/GCotto/Documents/Notes/Tickets/'
print(f'Current path is {tickets_path}\n')
folder_name = input('Enter the folder that contains the excel files e.g.(Ticket-123/):\n')
path = (tickets_path + folder_name)
print(f'Entered path for the excel file is {path}\n')
#path = input('Enter the path for the folder that contains the excel files:\n')

#CSV Files in the path
file_list = glob.glob(path + "/*.xlsx")

#List of excel files to merge
excl_list = []

for file in file_list:
    excl_list.append(pd.read_excel(file, dtype={"employee #":"string"}))

#Concatenate all dfs in the list into a single df
excl_merged = pd.concat(excl_list, ignore_index=True)

#Exports the dataframe into excel file
excel_path = path
new_excel_path = 'ExcelFileName.xlsx'
comb_excel = (f'{excel_path}/{new_excel_path}') 
xcl_merged.to_excel(f'{comb_excel}' , index=False)

#Read excel file
#Takes user input for the excel file location
excel_input = comb_excel
read_file = pd.read_excel(excel_input, dtype={"employee #":"string"})

#Convert excel to csv
#Takes user input for csv file location
csv_file = 'CSVFileName.csv'
csv_input = (f'{excel_path}/{csv_file}')
#csv_input = (path + input(f'Enter the csv file to save to in {path}:\n'))
#csv_input = input('Enter the full path for the csv file to save to:\n')
read_file.to_csv(f'{csv_input}', index=False)
print('CSV has been created from the Excel file.\n')

#Adding column names
dataframe_new = pd.read_csv(f'{csv_input}', names=['Column1','Column2','Column3','Column4'])
print('Printing new dataframe...\n')
print(dataframe_new)

print('Row header\n')
print(list(dataframe_new.columns))

#Creates a new csv file from the new dataframe with headers
#Takes user input for the new csv created from the dataframe with headers
new_csv_input = csv_input
#new_csv_input = input('Enter the full path for the updated csv file created from the dataframe:\nFile name should be HawaiianVacationBidsDATA.csv\n')
dataframe_new.to_csv(f'{new_csv_input}', index=False)
print(f'New CSV has been created in {new_csv_input}, verify the results.\n')


def jira_function():
    jiraOptions = {'server' : "jiraurlgoeshere"}

    #email_auth = input('Enter the email associated with the JIRA account:\n')
    #api_token_auth = input('Enter the API token associated with the JIRA account:\n')
    #Enter email/apikey
    jira = JIRA(options=jiraOptions, basic_auth=("jirausername@domain.com","jiratokengoeshere"))
    comment_input = 'The attached file(s) have been executed against the production database.\n'
    singleIssue = jira.issue(f'{folder_name}')
    print('{}: {}:{}'.format(singleIssue.key,
                             singleIssue.fields.summary,
                             singleIssue.fields.reporter.displayName))
    comment_send = jira.add_comment(folder_name,f"{comment_input}")

    #Change Assignee
    jira_connection = JIRA (
        basic_auth=("jirausername@domain.com","jiratokengoeshere"),
        server='jiraurlgoeshere'
    )

    issue = singleIssue

    params = {
        "query": "newassignee_email@domain.com",
        "includeActive": True,
        "includeInactive": False,
    }    

    list_search = jira_connection._fetch_pages(
        User, None, "user/search", params=params
    )

    jira_user_id = list_search[0].accountId

    fields = {"assignee": {"accountId": jira_user_id}}
    issue.update(assignee=fields["assignee"])

jira_input = input('Leave a comment and change the assignee?\nEnter "Y" or "N":\n').upper()

if jira_input == 'Y':
    jira_function()
    process_cont = input('Does the process need to be continued?\nEnter "Y" or "N":\n')
    
    if process_cont == 'Y':
        jira_function()

    else:
        print('Exiting the program...')

elif jira_input == 'N':
    print('Exiting the program...')
    exit()

else:
    print('Exiting the program...')