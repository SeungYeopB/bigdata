# url : https://auto.naver.com/bike/mainList.nhn
# 전체 제조사 element 찾아서 마우스 클릭
# 제조사 정보 크롤링     ---->>>>> 3시 40분
# 다음 페이지 버튼 눌러서 정보 크롤링
# 위사항을 반복,정보 크롤링   다음 페이지 버튼 비활성화 될때까지
from selenium import webdriver
# 특수 키값 처리 위한
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('chromedriver.exe')
url = 'https://auto.naver.com/bike/mainList.nhn'
driver.get(url)


selected_tags_a =  driver.find_element_by_css_selector("#container > div.spot_main > div.spot_aside > div.tit > a")
selected_tags_a.click()

selected_company_tags =  driver.find_elements_by_css_selector(\
    "#_vendor_select_layer > div > div.maker_group div.emblem_area > ul > li")

for item in selected_company_tags:
    name = item.find_element_by_tag_name("span").text
    print(name)
    if name != '':
        link = item.find_element_by_tag_name("a").get_attribute('href')
        print(link)


selected_button =  driver.find_element_by_css_selector(\
    "#_vendor_select_layer > div > div.maker_group > div.rolling_btn > button.next")

Next_page_flag = selected_button.is_enabled()
print(Next_page_flag)

## 다음 페이지 버튼 눌러서 정보 크롤링
## 위사항을 반복 . 정보 크롤링  다음 페이지 버튼 비활성화 될때까지
## 조건이 True 이명 계속 반복

while Next_page_flag == True:
    print(" 계속 반복 ")
    selected_button.click()
    Next_page_flag = selected_button.is_enabled()
    selected_company_tags = driver.find_elements_by_css_selector( \
        "#_vendor_select_layer > div > div.maker_group div.emblem_area > ul > li")

    for item in selected_company_tags:
        name = item.find_element_by_tag_name("span").text
        print(name)
        if name != '':
            link = item.find_element_by_tag_name("a").get_attribute('href')
            print(link)