import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

#Client ID and Token from file
C_ID = config['main'].get('C_ID')
SECRET = config['main'].get('SECRET')


#create auth
client_cred_manager = SpotifyClientCredentials(C_ID,SECRET)
#Create Session with Authentication
spotify = spotipy.Spotify(client_credentials_manager=client_cred_manager)

def getPlayList(playlist_id):
    artist = []
    album = []
    track_name = []
    track_id = []
    print(f'Got Playlist: {playlist_id}')
    results = spotify.playlist_tracks(playlist_id)['items']
    for track in results:
        artist.append(track["track"]["album"]["artists"][0]["name"])
        album.append(track["track"]["album"]["name"])
        track_name.append(track["track"]["name"])
        track_id.append(track["track"]["id"])
    #print(len(track_name))
    print("Proccessing Completed!\nDownloading Songs...")
    DownloadFromYoutube(artist, album, track_name, track_id)
    
#results = spotify.playlist_tracks()

def parsePlaylist(url):
    url = str(url)
    chunks = url.split('/')
    id = str(chunks[-1:])
    return id.split('?')[0][2:]


def DownloadFromYoutube(artist, album, track_name, track_id):
    #use somethig to search and download video from youtube 
    print("Downloading...")



#Take URL passed in and parse to get playlist ID
if len(sys.argv) == 2:
    getPlayList(parsePlaylist(sys.argv[1]))

else:
    print("Add the url as an argument and try again.")
