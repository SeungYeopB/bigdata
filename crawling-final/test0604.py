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


#  https://auto.naver.com/bike/mainList.nhn 시판모델의 모델명, 가격, 연료 정보 출력 하기

# "#_vendor_select_layer > div > div.maker_group > div:nth-child(2) > ul > li:nth-child(1) > a > img"
# "#content > div.model_group_new"
# "#content > div.model_group_new > ul > li:nth-child(1)"
selected_company_tags =  driver.find_elements_by_css_selector(\
           # "#content > div.model_group_new > ul")
            "#content > div.model_group_new > ul > li")
          #"#content > div.model_group_new > ul > li")
          #"#content > div.model_group_new > ul > li:nth-child(1)"

# selected_company_tags =  driver.find_elements_by_css_selector(\
#     "#content > div.model_group_new > ul > li:nth-child(1)")

for item in selected_company_tags:
    #print(item)
    # "#content > div.model_group_new > ul > li:nth-child(1) > div > div > a.model_name > span"
    # #content > div.model_group_new > ul > li:nth-child(1) > div > div > a.model_name > span > strong
    model = item.find_element_by_css_selector(".model_name > span").text
    print('model : ',model)
    # 가격
    ##content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.price.new > span.cont
    # #content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.price.new > span.cont
    # #content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.price.new > span.cont
    price = item.find_element_by_css_selector(".price.new > span.cont").text
    print('price: ' ,price)
    # 연료
    # #content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.mileage > span:nth-child(3)
    # #content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.mileage > span:nth-child(4) > span
    # content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.mileage > span:nth-child(4) > span
    fuel = item.find_elements_by_css_selector(".mileage > span")
    #print(len(fuel))
    print('fuel : ', fuel[3].text)

# page repeat print
selected_button =  driver.find_element_by_css_selector(\
    "#content > div.paginate2 > a.next")
    #"#content > div.paginate2 > a.next"
Next_page_flag =  selected_button.is_enabled()
#t = selected_button.get_attribute('disabled')
print(Next_page_flag)
time.sleep(5)
while Next_page_flag == True:
    print(" 계속 반복 ")
    #time.sleep(1)
    # button click
    try:
        selected_button = driver.find_element_by_css_selector( \
            "#content > div.paginate2 > a.next")
        time.sleep(1)
        #try:
        Next_page_flag = selected_button.is_enabled()
        selected_button.click()
        selected_company_tags = driver.find_elements_by_css_selector( \
            # "#content > div.model_group_new > ul")
            "#content > div.model_group_new > ul > li")
        for item in selected_company_tags:
            # print(item)
            # "#content > div.model_group_new > ul > li:nth-child(1) > div > div > a.model_name > span"
            model = item.find_element_by_css_selector(".model_name > span").text
            print('model : ', model)
            # 가격
            # #content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.price.new > span.cont
            # #content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.price.new > span.cont
            price = item.find_element_by_css_selector(".price.new > span.cont").text
            print('price: ', price)
            # 연료
            # #content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.mileage > span:nth-child(3)
            # #content > div.model_group_new > ul > li:nth-child(1) > div > ul > li.mileage > span:nth-child(4) > span
            fuel = item.find_elements_by_css_selector(".mileage > span")
            # print(len(fuel))
            print('fuel : ', fuel[3].text)
            time.sleep(1)
    except:
        print("error exit")
        break
        #time.sleep(1)