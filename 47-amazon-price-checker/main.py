from bs4 import BeautifulSoup
import requests
import lxml

URL = 'https://www.amazon.co.jp/-/en/KJ-65X80WK-Bravia-Compatible-Google-Recommended/dp/B0B3TFBQMW/ref=sr_1_8?crid=2L3RLT54U7E4&keywords=sony+tvx85k&qid=1677658067&sprefix=sony+tv+x85k%2Caps%2C171&sr=8-8'

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