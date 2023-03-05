from bs4 import BeautifulSoup
from requests_html import HTMLSession

def main():
    # date = input('Which year do you want to travel to?  Enter the date in the format YYYY-MM-DD:')
    # url = f'https://www.billboard.com/charts/hot-100/{date}/'
    url = f'https://www.billboard.com/charts/hot-100/1990-01-06/'

    session = HTMLSession()
    r = session.get(url)
    r.html.render(timeout=20, sleep=3)
    soup = BeautifulSoup(r.text, 'html.parser')

    song_html = soup.select('li ul li h3')
    song_list = [song.getText().strip('\t\n') for song in song_html]
    # print(song_list)

    for i in range(5):
        print(song_list[i])
    #     # print(artist_list[i].getText())
    #     print('\n')

if __name__ == "__main__":
    main()