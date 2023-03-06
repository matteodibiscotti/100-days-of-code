from bs4 import BeautifulSoup
from requests_html import HTMLSession

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

if __name__ == "__main__":
    main()