from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver.exe')
url = 'https://pjt3591oo.github.io/search'
driver.get(url)

print(driver.page_source)

soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup.select("div"))