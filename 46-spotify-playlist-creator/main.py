from bs4 import BeautifulSoup
from requests_html import HTMLSession
import spotipy
import os

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

def main():
    # date = input('Which year do you want to travel to?  Enter the date in the format YYYY-MM-DD:')
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

    # Authenticate with spotify (creates an auth object that can be passed to the API client)
    auth = spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

    # Creates a spotify API client
    client = spotipy.client.Spotify(oauth_manager=auth)

    print(client.current_user())

if __name__ == "__main__":
    main()