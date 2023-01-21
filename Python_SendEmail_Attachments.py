import win32com.client as win32
import os

# Construct Outlook application instance
olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

email_subject = input('Enter the email subject:\n')
email_address = input('Enter the email address of the user:\n')
username = input('Enter the name of the user to be used in the email body:\n')
email_body = input('Enter the body of the email to send:\n')
filepath = input('Enter the full file path for the attachment to send:\n')

# Construct the email item object
mailItem = olApp.CreateItem(0)
mailItem.Subject = f'{email_subject}'
mailItem.BodyFormat = 1

#Lines below are for sending the email body to the entered email address
mailItem.Body = f'{email_body}'
mailItem.To = f'{email_address}'

process_script = True

while process_script == True:
    #Print username/email to ensure values are entered correctly
    print(f'Username is {username}\nEmail is {email_address}\n')
    confirmation = input("Verify that the name\email entered looks correct...\n Enter 'Y' to send the email.\n Enter 'N' to re-enter the name of the user & email...\n")

    if confirmation == 'Y':
        #Send the email to the user based on user input
        mailItem.Attachments.Add(os.path.join(os.getcwd(),filepath))
        mailItem.Display()
        mailItem.Save()
        mailItem.Send()
        print("\nEmail has been sent. Check your 'Sent' folder in Outlook to verify everything is correct.")

    elif confirmation == 'N':
        username = input("Enter the name of the user:\n")
        # Enter the email address for the user
        email = input("Enter the email address of the user:\n")
        print(f'Username is {username}\nEmail is {email}\n')
        # Enter the file location of the spreadsheet with the list of usernames
        mailItem.Attachments.Add(os.path.join(os.getcwd(),filepath))
        mailItem.Display()
        mailItem.Save()
        mailItem.Send()
        print("\nEmail has been sent. Check your 'Sent' folder in Outlook to verify everything is correct.")

    else:
        print('"Y" or "N" were not selected...Exiting the program.')

    process_again = input('Need to repeat the process?\nEnter "Y" or "N":\n')

    if process_again == 'N':
        process_script = False
        print('Exiting the program...')