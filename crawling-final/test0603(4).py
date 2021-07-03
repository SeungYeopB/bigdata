from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
url = 'https://pjt3591oo.github.io/search'
driver.get(url)

driver.execute_script('alert("test")')

for i in range(0,100):
    print(i)