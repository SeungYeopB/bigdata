from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
url = 'https://pjt3591oo.github.io'
driver.get(url)

# mouse control - 마우스 제어용 써라. (페이지 이동용으로 사용 피해라)
selected_tags_a = driver.find_elements_by_css_selector("a")

for i in selected_tags_a:
    print(i.text, i.tag_name)
    i.click()
