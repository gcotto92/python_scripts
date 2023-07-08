from boto3.session import Session
import boto3
import os 
import shutil 

aws_profile_name = 'aws-profile-name-goes-here'
build_version_input = input('Enter the release build version (ex. 23.26):\n')
build_version = f'v{build_version_input}-release'
print(f'Build version entered is {build_version}')
underscore_version = input('Enter the release build version with underscore in between (23_26):\n')
version_folder = f'C:/Users/UserName/{underscore_version}/'
mode = 0o755
os.mkdir( version_folder, mode)

def download_repo1():
    repo1_folder = f'{version_folder}{underscore_version}_repo1/'
    wb_mode = 0o755
    os.mkdir( repo1_folder, wb_mode)
    print(f'Created new folder located in {repo1_folder}.\n')
    aws_s3_cp = f'aws s3 cp s3://s3_bucket/repo1/{build_version}/latest/ {repo1_folder} --recursive --profile {aws_profile_name}'
    os.system(aws_s3_cp)
    print(f'repo1 build has been downloaded to {repo1_folder}.\nVerify the results\n')
    shutil.make_archive(repo1_folder, 'zip', repo1_folder)
    print(f'zip file created from {repo1_folder}.\n')

    try:
        shutil.rmtree(repo1_folder)
    except OSError as e:
        print('Error: %s : %s' % (repo1_folder, e.strerror))

def download_repo2():
    repo2_folder = f'{version_folder}{underscore_version}_repo2/'
    repo2_mode = 0o755
    os.mkdir( repo2_folder, repo2_mode)
    print(f'Created new folder located in {repo2_folder}.\n')
    aws_s3_cp = f'aws s3 cp s3://s3_bucket/repo2/{build_version}/latest/ {repo2_folder} --recursive --profile {aws_profile_name}'
    os.system(aws_s3_cp)
    print(f'repo2 build has been downloaded to {repo2_folder}.\nVerify the results.\n')
    shutil.make_archive(repo2_folder, 'zip', repo2_folder)
    print(f'zip file created from {repo2_folder}.\n')
    
    repo2_path = f'{repo2_folder}'

    try:
       shutil.rmtree(repo2_path)
    except OSError as e:
        print('Error: %s : %s' % (repo2_path, e.strerror))
        
def repo3Mobile():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3Mobile/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3Mobile_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

    
def repo3WebSvc():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.WebSvc/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3WebSvc_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def repo3PData():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.PData/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3PData_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def ProcService():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.ProcService/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3ProcService_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def PayProcService():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.PayProcService/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3PayProcService_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def AKronInt():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.Scheduled.AKronInt/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3AKronInt_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def FailEmails():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.Scheduled.FailEmails/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3FailEmails_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def EmpStatInt():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.Scheduled.EmpStatInt/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3EmpStatInt_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def ExpSvc():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.Scheduled.ExpSvc/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3ExpSvc_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def AccSync():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.Scheduled.AccSync/{build_version}/latest.zip'
    download_name = f'{repo3_folder}AccSync_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def MissingPunches():
    #Downloads .zip 
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.Scheduled.MissingPunches/{build_version}/latest.zip'
    download_name = f'{repo3_folder}MissingPunches_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')


def SchedvsActu():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.Scheduled.SchedvsActuhiftsReport/{build_version}/latest.zip'
    download_name = f'{repo3_folder}SchedvsActuhiftsReport_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def SysNotif():
    #Downloads. zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.Scheduled.SysNotif/{build_version}/latest.zip'
    download_name = f'{repo3_folder}SysNotif_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def SeniorityFiles():
    #Downloads .zip 
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3.Windows.SeniorityFiles/{build_version}/latest.zip'
    download_name = f'{repo3_folder}SeniorityFiles_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def AuthAPI():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3AuthAPI/{build_version}/latest.zip'
    download_name = f'{repo3_folder}AuthAPI_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def ConfigDB():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3Configuration.Database/{build_version}/latest.zip'
    download_name = f'{repo3_folder}ConfigurationDatabase_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def DB():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3Database/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3Database_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def MangAPI():
    #Downloads .zip 
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3MangAPI/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3MangAPI_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def Reports():
    #Downloads .zip 
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3Reports/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3Reports_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def RAWeb():
    #Downloads .zip
    bucket_name = 's3_bucket'
    file_name = f'repo3/repo3Web/{build_version}/latest.zip'
    download_name = f'{repo3_folder}repo3Web_{build_version}_latest.zip'
    s3 = boto3.resource("s3")
    session = Session(aws_access_key_id="access-key-goes-here",
                  aws_secret_access_key="secret-key-goes-here",
                  region_name="us-east-2")  
    session.resource('s3').Bucket(f'{bucket_name}').download_file(Key=f'{file_name}', Filename=f'{download_name}')

def create_zip():
    shutil.make_archive(version_folder, 'zip', version_folder)
    print(f'zip file created from {version_folder}.\n')

def delete_folder():
    delete_path = f'{version_folder}'
    try:
        shutil.rmtree(delete_path)
    except OSError as e:
        print('Error: %s : %s' % (delete_path, e.strerror))
    print(f'Path of {version_folder} has been deleted.\n')

process_script = True 

while process_script == True:

    product_build = input('What product is this for?\nEnter "repo1" or "repo2" or "repo3":\n').lower()

    if product_build == 'repo1':
        download_wb()
        select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
        if select_again == 'N':
            process_script = False

    elif product_build == 'repo2':
        download_repo2()
        select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
        if select_again == 'N':
            process_script = False

    elif product_build == 'repo3':
        
        repo3_folder = f'{version_folder}{underscore_version}_repo3/'
        rapps_mode = 0o755
        os.mkdir( repo3_folder, rapps_mode)
        print(f'Created new folder located in {repo3_folder}.\n')
        
        rapps_array = ['repo3Mobile','repo3WebSvc','repo3PData','ProcService','PayProcService','AKronInt','FailEmails','EmpStatInt',
             'ExpSvc','AccSync','MissingPunches','SchedvsActu','SysNotif','SeniorityFiles','AuthAPI','ConfigDB','DB','MangAPI','Reports','RAWeb','all']
        print(rapps_array)
        rapps_selection = input('Enter the repo3 build to download from the list above or enter "all" to download all builds:\n')

        if rapps_selection == 'all':
            print('Executing against all the listed repos...\n')
            repo3Mobile()
            repo3WebSvc()
            repo3PData()
            ProcService()
            PayProcService()
            AKronInt()
            FailEmails()
            EmpStatInt()
            ExpSvc()
            AccSync()
            MissingPunches()
            SchedvsActu()
            SysNotif()
            SeniorityFiles()
            AuthAPI()
            ConfigDB()
            DB()
            MangAPI()
            Reports()
            RAWeb()
           

            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False
                shutil.make_archive(repo3_folder, 'zip', repo3_folder)
                print(f'zip file created from {repo3_folder}.\n')
                
                delete_path = f'{repo3_folder}'
                try:
                    shutil.rmtree(delete_path)
                except OSError as e:
                    print('Error: %s : %s' % (delete_path, e.strerror))
                    print(f'Path of {repo3_folder} has been deleted.\n')
 

        elif rapps_selection == 'repo3Mobile':
            print('Executing against Mobile...\n')
            repo3Mobile()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'repo3WebSvc':
            print('Executing against WebSvc...\n')
            repo3WebSvc()
            create_zip()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'repo3PData':
            print('Executing against PData...\n')
            repo3PData()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'ProcService':
            print('Executing against ProcService...\n')
            ProcService()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'PayProcService':
            print('Executing against PayProcService...\n')
            PayProcService()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'AKronInt':
            print('Executing against AKronInt...\n')
            AKronInt()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'FailEmails':
            print('Executing against FailEmails...\n')
            FailEmails()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'EmpStatInt':
            print('Executing against EmpStatInt...\n')
            EmpStatInt()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'ExpSvc':
            print('Executing against ExpSvc...\n')
            ExpSvc()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'AccSync':
            print('Executing against AccSync...\n')
            AccSync()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'MissingPunches':
            print('Executing against MissingPunches...\n')
            MissingPunches()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'SchedvsActu':
            print('Executing against SchedvsActu...\n')
            SchedvsActu()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'SysNotif':
            print('Executing against SysNotif...\n')
            SysNotif()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'SeniorityFiles':
            print('Executing against SeniorityFiles...\n')
            SeniorityFiles()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'AuthAPI':
            print('Executing against AuthAPI...\n')
            AuthAPI()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'ConfigDB':
            print('Executing against ConfigurationDatabase...\n')
            ConfigDB()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'DB':
            print('Executing against repo3Database...\n')
            DB()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False
 
        elif rapps_selection == 'MangAPI':
            print('Executing against MangAPI...\n')
            MangAPI()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'Reports':
            print('Executing against repo3Reports...\n')
            Reports()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        elif rapps_selection == 'RAWeb':
            print('Executing against repo3Web...\n')
            RAWeb()
            select_again = input('Enter "N" to end the script or press ENTER key to continue:\n').upper()
            if select_again == 'N':
                process_script = False

        else: 
            print('Correct selection was not entered.\n')
            exit()
        
    else:
        print('Correct selection was not entered.\n')
        exit()