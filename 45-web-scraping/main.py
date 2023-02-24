from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

def main():
    response = requests.get(URL)
    website_html = response.text
    soup = BeautifulSoup(website_html, 'html.parser')

    movie_list = soup.find_all(name="h3", class_="title")

    for title in reversed(movie_list):
        with open('top100movies.txt', 'a', encoding="utf-8") as file:
            file.write(title.getText() + '\n')

if __name__ == "__main__":
    main()