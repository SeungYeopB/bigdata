from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
url = 'https://pjt3591oo.github.io'
driver.get(url)

# mouse control -
selected_selector = driver.find_element_by_css_selector("div.home div.p a")
print(selected_selector)
print(selected_selector.tag_name)
print(selected_selector.text)
selected_selector.click()
