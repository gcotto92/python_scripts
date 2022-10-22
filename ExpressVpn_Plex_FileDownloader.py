from urllib import request
import requests
import shutil

download_input = input('Is this for Plex or expressvpn?\nEnter P or E:\n')


file_url = 'https://www.expressvpn.works/clients/linux/expressvpn_3.34.1.0-1_amd64.deb'
plex_url = 'https://downloads.plex.tv/plex-media-server-new/1.29.0.6244-819d3678c/debian/plexmediaserver_1.29.0.6244-819d3678c_amd64.deb?_gl=1*1i4cc5c*_ga*NjE1MDg2ODY2LjE2NjYxMjE5MDY.*_ga_G6FQWNSENB*MTY2NjEyMTkwNi4xLjAuMTY2NjEyMTkwNi4wLjAuMA..'

if download_input == 'E':
    r = requests.get(file_url, stream = True)

    with open("expressvpn_install.deb",'wb') as deb:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                deb.write(chunk)

if download_input == 'P':
    r = requests.get(plex_url, stream = True)

    with open("plexmediaserver.deb",'wb') as deb:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                deb.write(chunk)

print('File has been downloaded')

move_file_input = input('Time to move the file locally.\nEnter Y to move the file:\n')

if move_file_input == 'Y':
    file_source = input('Enter the file source:\n')
    file_des = input('Enter file destination:\n')
    shutil.move(file_source, file_des)
    print('Verify that the file has been moved...')

print('File has been downloaded/moved.Verify the results...')
