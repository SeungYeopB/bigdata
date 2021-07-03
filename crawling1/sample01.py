import urllib.request
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'

res = urllib.request.urlopen(url)
data = res.read()
html = data.decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

print(soup)
h1 = soup.html.body.h1
print('h1:', h1.string)