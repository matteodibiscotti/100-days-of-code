from bs4 import BeautifulSoup
import requests
import lxml
import re
from email_function import send_email

URL = 'https://www.amazon.co.jp/-/en/KJ-65X80WK-Bravia-Compatible-Google-Recommended/dp/B0B3TFBQMW/ref=sr_1_8?crid=2L3RLT54U7E4&keywords=sony+tvx85k&qid=1677658067&sprefix=sony+tv+x85k%2Caps%2C171&sr=8-8'

def main():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }

    response = requests.get(url=URL, headers=headers)
    website_html = response.text
    soup = BeautifulSoup(website_html, 'lxml')

    with open('price.txt', 'r') as file:
        original_price = int(file.readline())

    price = int("".join((soup.find(class_="a-price-whole").text).split(",")))

    product_details = soup.find_all(class_='a-size-base prodDetAttrValue')
    model = re.findall("[A-Z]{2}-[0-9A-Z]{7}", product_details[7].getText())[0]

    if price != original_price:

        if price > original_price:
            price_direction = "increased"

        if price < original_price:
            price_direction = "decreased"

        send_email(price=price, item=model, price_direction=price_direction)

        with open('price.txt', 'w') as file:
            file.write(str(price))

if __name__ == "__main__":
    main()