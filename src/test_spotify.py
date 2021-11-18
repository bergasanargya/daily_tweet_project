"""Import the special information we need to access the API"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

#client_id and client_secret were taken from the developer account
cid = 
secret = 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,10000,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

track_dataframe = pd.DataFrame(
    {'artist_name' : artist_name, 
     'track_name' : track_name, 
     'track_id' : track_id, 
     'popularity' : popularity
    }
)

print(track_dataframe.shape)
track_dataframe.head()