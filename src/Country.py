import os
import random
import spotify.sync as spotify

CLIENT = os.getenv('FF_SPOTIFY_CLIENT')
SECRET = os.getenv('FF_SPOTIFY_CLIENT_SECRET')

client = spotify.Client(CLIENT, SECRET)
result = client.search('Hot Country', types=['playlist'])

for playlist in result.playlists:
    tracks = playlist.get_all_tracks()
    track = random.choice(tracks)
    print(track.popularity)
    print(f"This weekend, listen to {track.name} by {track.artist.name}. It's good.")

client.close()

# This is the Country Playlist File 
# This will get the a random song from the Hot Country playlist in Spotify