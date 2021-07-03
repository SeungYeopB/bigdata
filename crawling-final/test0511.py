import urllib.request
from bs4 import BeautifulSoup

url = "http://www.naver.com/index.html"

res = urllib.request.urlopen(url)
data = res.read()

src = data.decode("utf-8")
print(src)

html = BeautifulSoup(src, "html.parser")
print(html)

a = html.find("a")
print("a, tag :", a)
print(" a tag 내용 :", a.string)

b = html.find_all("a")
print("a, tag :", b)
print(type(b))
print(" a tag 내용 :", b.string)

file = open("./data/html01.html", mode="r", encoding="utf-8")
text = file.read()

html = BeautifulSoup(text, "html.parser")
h1 = html.html.body.h1
print("h1 : ", h1.string)

h2 = html.find("h2")
print("h2 :", h2.string)

lis = html.find_all("li")

for li in lis:
    print(li.string)

from bs4 import BeautifulSoup

file = open("./data/html02.html", mode="r", encoding="utf-8")
source = file.read()

html = BeautifulSoup(source, "html.parser")

links = html.find_all("a")
print("links size :", len(links))

for link in links :
    try:
        print(link.attrs["href"])
        print(link.attrs["target"])

    except Exception as e :
        print("예외발생 :", e)
import re
print("패턴 객체 이용 속성 찾기")
patt = re.compile("http://")
links = html.find_all(href = patt)
print(links)

from bs4 import BeautifulSoup
# (1) 로컬 파일 읽기
file = open("./data/html03.html", mode="r", encoding="utf-8")
source = file.read()
# (2) html 파싱
html = BeautifulSoup(source, "html.parser")
# (3) 선태가 이용 태그 내용 가져오기

# (3-1) id="tab" 선택자
print(">> table 선택자 <<")
table = html.select_one("#tab")  # <table id="tab">
print(table) # table 태그 전체 출력

# (3-2) id 선택자와 계층
print(">> 선택자 & 계층 <<")
ths = html.select("#tab > tr > th")
print(ths)  # list
# (3-3) class 선택자 : tr tag class="odd"
trs = html.select("#tab > .odd") # 홀수 행
print(">> class 선택자 <<")
print(trs)

trs = html.select("tr[class=odd]")

print(">> tr > td 출력 <<")
for tr in trs:
    tds = tr.find_all("td")
    for td in tds:
        print(td.string)

import urllib.request as req
from bs4 import BeautifulSoup

url = "http://media.daum.net"

res = req.urlopen(url)
source = res.read()

source = source.decode("utf-8")

html = BeautifulSoup(source, "html.parser")

atags = html.select("a[class=link_txt]")
print("a tag 수=", len(atags))

crawling_data = []

cnt=0
for atag in atags:
    cnt += 1
    atagStr = str(atag.string)
    crawling_data.append(atagStr.strip())
    '''
    string.strip() : 문단 끝 불용어(공백, tab,\n\r) 제거
    '''
print("수집한 자료 확인")
print(crawling_data)

import pickle
file = open("./data/data.pickle", mode="wb")
pickle.dump(crawling_data, file)

file = open("./data/data.pickle", mode="rb")
crawling_data = pickle.load(file)
print("pickle load")
print(crawling_data)


# naver TOP 뉴스 크롤링 - Beautifulsoup
import requests
import re
from bs4  import BeautifulSoup
URL = 'http://finance.naver.com/'
response = requests.get(URL)
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')
par = soup.tbody
print(par)
par2 = par.find_all('a')
print(par2)
nujuk = [] #  -> list에 저장 으로 변경
for child in par2:
    print(child)
    print(child.string)
    nujuk.append(child.string)
print(nujuk)

