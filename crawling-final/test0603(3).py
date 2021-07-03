from selenium import webdriver
## 특수 키값 처리 위한
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('chromedriver.exe')
url = 'https://pjt3591oo.github.io/search'
driver.get(url)

selected_tags_a = driver.find_element_by_css_selector("input#search-box")

selected_tags_a.click()
selected_tags_a.send_keys("test")
selected_tags_a.send_keys(Keys.ENTER)

## NULL, CANCEL, BACKSPACE, RETURN, SPACE 등등
driver.get(url)
