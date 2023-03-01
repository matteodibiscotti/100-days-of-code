from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('/Users/matthewlowman/Coding/development/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://karat.com/')

link = driver.find_element(By.XPATH, '/html/body/nav/div[4]/div[1]/ul[2]/li[1]/a')

print(link.text)

driver.quit()