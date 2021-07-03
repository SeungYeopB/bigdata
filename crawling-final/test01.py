import requests
URL = 'https://www.segye.com'
response = requests.get(URL)
html_data = response.text
import re
temp_data = html_data.split('<li><i class="rank')
nujuk = ''   # list에 저장해라
for i in range(1,6):
    if i == 5 :
        temp_data1 = temp_data[i].split('</span></a></li>')
        body = re.search('<span class="txt">.*', temp_data1[0], re.I | re.S)
    else :
        body = re.search('<span class="txt">.*',temp_data[i],re.I|re.S)
    body = body.group()
    body = re.sub('<.+?>', '', body)  # tag 모두 제거
    nujuk += body
# 파일에 저장
f = open("crawling-segye.txt",'w',encoding='UTF-8')
f.write(nujuk)
f.close()