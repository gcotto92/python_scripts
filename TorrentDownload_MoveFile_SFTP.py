from qbittorrent import Client
import shutil
import paramiko

qb = Client('http://127.0.0.1:8080/')

qb.login('','')

def sftp_function():
        #Host IP
    host = '192.168.50.248'
    #Host Port
    port = 22
    #Host Username
    username = ''
    #Host Password
    password = ''

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

torrent_path = input('Enter the torrent path:\n')
torrent_file = open(f'{torrent_path}', 'rb')

qb.download_from_file(torrent_file)

print('Time to move the files over.\nVerify the torrent progress is at 100%.\n')
status_progress= input('Is progress at 100%?\nEnter Y when ready:\n')

if status_progress == 'Y':
    #Takes user input for the full source path
    source = input('Enter the full source directory:\n')
    #Takes user input for the full destination path
    destination = '/home/gcotto/Downloads/temp/'
    filename = input(f'\nFile will be moved to directory of {destination}\nEnter the new file name:\n')
    full_destination = destination + filename

    new_path = shutil.move(source,full_destination)
    print(f'File has been moved to {full_destination}\n')

    begin_sftp = input('Ready to begin the SFTP process?\nEnter "Y" to continue:\n')
    if begin_sftp == 'Y':
        sftp_function()


delete_input = input('Do you want to delete the torrent directory?\nEnter Y or N:\n')
if delete_input == 'Y':
    file_path = input('Enter the directory to delete:\n')
    try:
        shutil.rmtree(file_path)
    except OSError as e:
        print("Error: %s : %s" % (file_path, e.strerror))

print('Process has completed\nExiting the program...')