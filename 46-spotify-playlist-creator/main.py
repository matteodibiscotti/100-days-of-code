from bs4 import BeautifulSoup
from requests_html import HTMLSession
import spotipy
import os

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

def main():
    # date = input('Which year do you want to travel to?  Enter the date in the format YYYY-MM-DD:')
    # year = date[:4]
    year = 1990
    # url = f'https://www.billboard.com/charts/hot-100/{date}/'
    url = f'https://www.billboard.com/charts/hot-100/1990-01-06/'

    session = HTMLSession()
    r = session.get(url)
    r.html.render(timeout=20, sleep=3) # All page data wasn't loading so this renders the entire page
    soup = BeautifulSoup(r.text, 'html.parser')

    song_html = soup.select('li ul li h3')
    song_list = [song.getText().strip('\t\n') for song in song_html]

    artist_html = soup.select('li ul li span')
    artist_list = [artist.getText().strip('\t\n') for artist in artist_html[0::7]]

    # ================SPOTIFY===================
    # ================AUTH======================

    # Authenticate with spotify (creates an auth object that can be passed to the API client)
    auth = spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

    # Creates a spotify API client
    client = spotipy.client.Spotify(oauth_manager=auth)

    # ================SONG-URI======================
    song_uri_list = []

    for i, j in zip(song_list, artist_list):
        track, artist = i, j
        # query = f'track:{track} year:{year}'
        query = f'track:{track} artist:{artist}'
        response = (client.search(q=query, type='track', market='JP'))
        # need to loop through the results to find the song where the song name and artist match their respective fields
        for item in range(len(response['tracks']['items'])):
            spotify_artist_list = []
            uri = ""
            for item_artist in range(len(response['tracks']['items'][item]['artists'])):
                spotify_artist_list.append(response['tracks']['items'][item]['artists'][item_artist]['name'].lower())
                if artist.lower() in spotify_artist_list:
                    uri = response['tracks']['items'][item]['uri']
                    song_uri_list.append(uri)
                    print(f'track:{track} artist:{artist} ========= {uri}')
    
    print(len(song_uri_list))
    # print(song_uri_list[:5])
    templist = []
    [templist.append(x) for x in song_uri_list if x not in templist]
    print('List after removing dups')
    print(len(templist))

    

if __name__ == "__main__":
    main()