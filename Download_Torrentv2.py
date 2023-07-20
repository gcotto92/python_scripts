from qbittorrent import Client

qb = Client('http://127.0.0.1:8080/')

qb.login('admin','passwordgoeshere')

torrent_path = input('Enter the torrent path:\n')
torrent_file = open(f'{torrent_path}', 'rb')

qb.download_from_file(torrent_file)