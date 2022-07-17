import shutil
import paramiko
import shutil

#Takes user input for the full source path
source = input('Enter the full source directory:\n')
#Takes user input for the full destination path
destination = '/home/gcotto/Downloads/temp/'
filename = input(f'Enter the file name:\nFile will be moved to directory of {destination}\n')
full_destination = destination + filename

new_path = shutil.move(source,full_destination)
print(f'File has been moved to {full_destination}\n')

#Enter host IP below
host = ''
#Enter host port number below
port = 22
#Enter host username below
username = ''
#Enter host password below
password = ''

#Paramiko library connects via ssh to host parameters
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)
sftp = ssh.open_sftp()

localpath = full_destination
print(f'Pulling file from {full_destination}\n')
sftp_path = '/media/ntfs/'+ filename
print(f'File will be moved to directory of {sftp_path}\nPlease wait as the upload process completes...\n')
sftp.put(localpath,sftp_path)

print(f'File has been uploaded to {sftp_path}\nVerify the results')


sftp.close()
ssh.close()
