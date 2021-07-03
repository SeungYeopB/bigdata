from selenium import webdriver
## 특수 키값 처리 위한
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(10)  ## 대기명령 10초

## 페이지 가져오기
driver.get("http://www.google.co.kr")
driver.get("http://www.naver.com")
driver.get("http://www.daum.net")

driver.back()
time.sleep(3)
driver.back()

driver.forward()
time.sleep(3)
driver.forward()

time.sleep(3)
driver.quit()