import paramiko

#Enter host IP below
host = ''
#Enter host port number below
port = 22
#Enter host username below
username = ''
#Enter host password below
password = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

sftp = ssh.open_sftp()

#User input for the file name
localpath = input("Pulling file from /home/gcotto/Downloads/temp/\nPlease enter the filepath location:\n")
#File path location where the file from line above exists
localpath2 = ('/home/user/Downloads/temp/'+localpath)
#Enter the full destination path on the remote host
path = input("File will be uploaded to media/ntfs\nPlease enter the media file name:\n")
sftp.put(localpath2,path)

print(f"File has been uploaded to {path}")

sftp.close()
ssh.close()
