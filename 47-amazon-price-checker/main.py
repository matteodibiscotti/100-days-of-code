from bs4 import BeautifulSoup
import requests
import lxml

URL = 'https://www.amazon.co.jp/-/en/KJ-65X80WK-Bravia-Compatible-Google-Recommended/dp/B0B3TFBQMW/ref=sr_1_8?crid=2L3RLT54U7E4&keywords=sony+tvx85k&qid=1677658067&sprefix=sony+tv+x85k%2Caps%2C171&sr=8-8'

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }

    response = requests.get(url=URL, headers=headers)
    website_html = response.text
    soup = BeautifulSoup(website_html, 'lxml')

    price = soup.find(class_="a-price-whole")
    print(f'{price.text}円')

if __name__ == "__main__":
    main()