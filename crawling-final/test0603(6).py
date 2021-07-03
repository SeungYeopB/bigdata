## 문제 - search - db 해서 서치한 내용중 ##
## "ul#search-results li" 을 beautiful soup로 select 하고
##  list 값을 print 하세요
##  출력 내용 : title, description  내용 2: 10 까지

from selenium import webdriver
## 특수 키값 처리 위한
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('chromedriver.exe')
url = 'https://pjt3591oo.github.io/search'
driver.get(url)
time.sleep(5) ### 5초동안 대기

driver.fullscreen_window()  ## 전체 화면으로 모드 변경
time.sleep(5)
driver.maximize_window()  ## 최대창으로 모드 변경
time.sleep(5)

driver.set_window_rect(100,100,500,500)  ## 좌표 x, y 폭, 높이 모드 변경

selected_tags_a = driver.find_element_by_css_selector("input#search-box")

selected_tags_a.click()
selected_tags_a.send_keys("db")
selected_tags_a.send_keys(Keys.ENTER)

soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup.select("ul#search-results li"))
items = soup.select("ul#search-results li")
for item in items:
    title = item.find("h3").text
    description = item.find("p").text
    print(title)
    print(description)