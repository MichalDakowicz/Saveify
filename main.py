import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json

# Set up your Spotify API credentials
client_id = '285e04f8cce44447a0360aec861babf2'
client_secret = '7bec10d0cbf74fd0a775a455c10b9098'

# Set up the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for a song
song_name = 'Despacito'
results = sp.search(q=song_name, type='track', limit=1)

# Get the first track from the search results
track = results['tracks']['items'][0]

print(json.dumps(track, indent=4))
print()

# Get the track's preview URL
preview_url = track['preview_url']


# Download the song
# Add your code here to download the song using the preview_url
response = requests.get(preview_url)
if response.status_code == 200:
    with open('song.wav', 'wb') as file:
        file.write(response.content)
    print('Song downloaded successfully!')
else:
    print('Failed to download the song.')


# Add your code here to download the song using the preview_url

print('Song downloaded successfully!')
