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