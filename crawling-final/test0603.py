from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
url = 'https://pjt3591oo.github.io'
driver.get(url)

selected_id = driver.find_element_by_id('nav-trigger')
print(selected_id)
print(selected_id.tag_name)
print(selected_id.text)

selected_tag_p = driver.find_element_by_tag_name('p')
print(selected_tag_p)
print(selected_tag_p.tag_name)
print(selected_tag_p.text)

selected_tags_p = driver.find_elements_by_tag_name('p')
print(selected_tags_p)
print(selected_tags_p.tag_name)  # list 라 실행안됨
print(selected_tags_p.text)    # list  라 실행안됨

# div tag 가져오기
selected_tags_p = driver.find_elements_by_tag_name('div')
print(selected_tags_p)

selected_name = driver.find_element_by_name('description')
print(selected_name)
print(selected_name.tag_name)
print(selected_name.text)

selected_names = driver.find_elements_by_name('description')
print(selected_names)

# a tag의 href를 이용해서 자료 수집시 사용 , query string부분만 찾음.
selected_link = driver.find_element_by_link_text('')
print(selected_link)
print(selected_link.tag_name)
print(selected_link.text)

selected_links = driver.find_elements_by_link_text('')
print(selected_links)

# path 이용 해서 찾을때
selected_linkp=  driver.find_element_by_partial_link_text('react')
print(selected_linkp)
print(selected_linkp.tag_name)
print(selected_linkp.text)

selected_linksp = driver.find_elements_by_partial_link_text('react')
print(selected_links)

selected_class = driver.find_element_by_class_name('p')
print(selected_class)
print(selected_class.tag_name)
print(selected_class.text)

selected_classes = driver.find_elements_by_class_name('p')
print(selected_classes)
#find_element_by_css_selector
selected_selector = driver.find_element_by_css_selector("div.home div.p")
print(selected_selector)
print(selected_selector.tag_name)
print(selected_selector.text)
selected_selectors = driver.find_element_by_css_selector("div.home div.p")
print(selected_selectors)

## 요소가 없는 경우는 error 출력
selected_selector_e = driver.find_element_by_css_selector(".a")
print(selected_selector_e)
print(selected_selector_e.tag_name)
print(selected_selector_e.text)

# mouse control -
selected_selector = driver.find_element_by_css_selector("div.home div.p a")
print(selected_selector)
print(selected_selector.tag_name)
print(selected_selector.text)
selected_selector.click()



