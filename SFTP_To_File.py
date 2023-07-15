#from qbittorrent import Client
import shutil
import paramiko
import os


def sftp_function():
    #Host IP
    host = 'ip'
    #Host Port
    port = 22
    #Host Username
    username = 'username'
    #Host Password
    password = 'password'

    #Paramiko library connects via ssh to host parameters
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,username,password)
    sftp = ssh.open_sftp()

    print('Time for SFTP process')
    localpath = full_destination
    print(f'Pulling file from {full_destination}\n')
    sftp_path = '/media/ntfs/'+ filename
    print(f'File will be moved to directory of {sftp_path}\nPlease wait as the upload process completes...\n')
    sftp.put(localpath,sftp_path)

    print(f'File has been uploaded to {sftp_path}\nVerify the results')

    sftp.close()
    ssh.close()

#Takes user input for the full source path
ls_downloads = 'ls /home/gcotto/Downloads/'
os.system(ls_downloads)
ls_down_new = input(f'Enter the path in {ls_downloads} to run ls against:\n')
down_newpath = f'ls {ls_downloads}{ls_down_new}/'
os.system(down_newpath)
source_path = f'{ls_downloads}{ls_down_new}/'
source_input = input('Enter the media file source from the path above:\n')
source = f'{source_path}{source_input}'

#Takes user input for the full destination path
destination = '/home/gcotto/Downloads/temp/'
filename = input(f'\nFile will be moved to directory of {destination}\nEnter the new file name:\n')
full_destination = destination + filename

new_path = shutil.move(source,full_destination)
print(f'File has been moved to {full_destination}\n')

begin_sftp = input('Beginning the SFTP function.\nPlease wait as the process completes...\n')
sftp_function()


delete_input = input('Do you want to delete the torrent directory?\nEnter Y or N:\n')
if delete_input == 'Y':
    file_path = input('Enter the directory to delete:\n')
    try:
        shutil.rmtree(file_path)
    except OSError as e:
        print("Error: %s : %s" % (file_path, e.strerror))

print('Process has completed\nExiting the program...')