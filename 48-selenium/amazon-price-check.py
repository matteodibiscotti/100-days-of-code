from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('/Users/matthewlowman/Coding/development/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.co.jp/-/en/KJ-65X80WK-Bravia-Compatible-Google-Recommended/dp/B0B3TFBQMW/ref=sr_1_8?crid=2L3RLT54U7E4&keywords=sony+tvx85k&qid=1677658067&sprefix=sony+tv+x85k%2Caps%2C171&sr=8-8')

price = driver.find_element(By.CLASS_NAME, "a-price-whole")

print(f'{price.text}円')

driver.quit()