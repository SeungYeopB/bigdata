import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://hotel.naver.com/hotels/item?hotelId=hotel:Shilla_Stay_Yeoksam&destination_kor=%EC%8B%A0%EB%9D%BC%EC%8A%A4%ED%85%8C%EC%9D%B4%20%EC%97%AD%EC%82%BC&rooms=2")
#time.sleep(random.uniform(1,3))
time.sleep(3)
review_list = []
# body > div > div > div.container.ng-scope > div.content > div.hotel_article_review.ng-isolate-scope > div.article_wrap > ul > li:nth-child(1)
#trip = driver.find_element_by_css_selector("body > div > div > div.container.ng-scope > div.content > div.hotel_article_review.ng-isolate-scope > div.article_wrap > ul")
trip = driver.find_element_by_css_selector("body > div > div > div.container.ng-scope > div.content > div.hotel_article_review.ng-isolate-scope > div.article_wrap > ul > li")
#trip.click()
cnt = 1
while True:
#body > div > div > div.container.ng-scope > div.content > div.hotel_article_review.ng-isolate-scope > div.article_wrap > ul > li:nth-child(5) > div.article_content > div > p
    for num in range(1,5):
        review = driver.find_elements_by_css_selector(".article_wrap > ul > li:nth-child(%d) > div.article_content > div > p"% cnt)
        cnt += 1
        print("count value :" , cnt)
        for i in review:
            print(i.text)
            review_list.append(i.text)
    islast = driver.find_elements_by_css_selector(\
        #"body > div > div > div.container.ng-scope > div.content > div.hotel_article_review.ng-isolate-scope > div.paginate.ng-scope > a.direction.next")
        "div.hotel_article_review.ng-isolate-scope > div.paginate.ng-scope > a.direction.next.disabled")
    len(islast)
    if not len(islast)==0:
        break
    else:
        next = driver.find_element_by_css_selector(\
          #  "body > div > div > div.container.ng-scope > div.content > div.hotel_article_review.ng-isolate-scope > div.paginate.ng-scope > a.direction.next")
        "div.hotel_article_review.ng-isolate-scope > div.paginate.ng-scope > a.direction.next")
        next.click()
        time.sleep(5)
print(review_list)
print(len(review_list))

f = open("./naverhotel.txt","w",encoding="utf-8")  ## w는 write모드로 오픈한다는 뜻  r은 read 모드입니다
f.write("\n".join(review_list))  ## 위에 w를 썻으니 write로 씁니다
f.close()