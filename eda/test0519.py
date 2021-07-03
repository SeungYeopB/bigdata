import requests
from bs4 import BeautifulSoup

result = []
for i in range(1, 137, 15):
    res = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC&research_url=&sm=tab_pge&start={start}&where=web'.format(start=i))
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('a.link_tit')
    print((i+14)/15, "page", end="")
    for title in titles:
        result.append(title.get_text())

print()
print(result)



for i in range(5):
    for j in range(i):
        print(" ", end=" ")
    for j in range(5-i):
        print("*", end=" ")
    print("")

for i in range(2,10):

    for j in range(i):
        print(j)
  #      print(i, "*",j,"=", i*j)


import requests
from bs4 import BeautifulSoup

result = []
for i in range(1, 137, 15):
    res = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC&research_url=&sm=tab_pge&start={start}&where=web'.format(start=i))
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select("div.api_txt_lines dsc_txt")
    print(titles)
    print(i, "page", end="")
    for title in titles:
        print(title.get_text())
        result.append(title.get_text())


print(result)