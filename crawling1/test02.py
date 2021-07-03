import requests
url = 'http://hrdi.koreatech.ac.kr'
response = requests.get(url)
print(response.status_code)
print(response.text)

URL = 'http://search.naver.com/search.naver'
params = {'query' : 'aa'}
response = requests.get(URL,params=params)
print(response.status_code)
print(response.text)

import requests
url = 'https://www.naver.com'
response = requests.get(url)
print(response.status_code)
print(response.text)

import requests
url = 'https://search.naver.com/search.naver'
params = {'query' : 'aa'}
response = requests.get(url,params=params)
print(response.status_code)
print(response.text)

import requests
url = 'https://comic.naver.com/webtoon/list.nhn'
params = {'titleId' : '769802','no' : '5'}
response = requests.get(url,params=params)
print(response.status_code)
print(response.text)

# https://raw.githubusercontent.com/naver
# /naver-openapi-guide/draft/naver-openapi-swagger.json
import requests
response = requests.get('https://raw.githubusercontent.com/naver/naver-openapi-guide/draft/naver-openapi-swagger.json')
result = response.json()
print(type(result))
print(result.text)
print(result.items())
print(dict.items())
print(result['swagger'])

text = "    <title>한국기술교육대학교 능력개발원</title>   "
text2 = ";"
print(text.strip()+text2)

text = "    <title>한국기술교육대학교 능력개발원</title>   "
text2 = ";"
print(text.lstrip()+text2)

text = "    <title>한국기술교육대학교 능력개발원</title>   "
text2 = ";"
print(text.rstrip()+text2)

text = "    <title>한국기술교육대학교 능력개발원</title>   "
text2 = ";"
print(text.replace('<title>','<div>'))
print(text.replace('<title>',''))



import re
text = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>', text)
body = body.group()
print(body)


import re
text = ('11<head>안녕하세요</head>22/')
body = re.search('<head.*/head>',text)
print(body)
body = body.group()
print(body)

import re
text = ('<head>안녕하세요......<title> 한국기술교육 대학교 능력 개발원 </title> 반갑습니다...<head>/')
body = re.search('<title.*/title>',text)
print(body)
body = body.group()
print(body)

body = re.sub('<.+?>','', body)
print(body)

import requests
URL = 'https://www.naver.co.kr'
response = requests.get(URL)
html_data = response.text
print(html_data)
f = open("crawling-naver.txt",'w',encoding='UTF-8')
f.write(response.text)
#f.writelines(t)
#f.writelines(l)
f.close()

import requests
URL = 'http://www.segye.com'
response = requests.get(URL)
html_data = response.text
print(html_data)
print(html_data.find('div id="wps_layout1_box4" data-desc"'))

print(html_data.find('<li><i class="rank'))
arr1 = html_data.split('<li><i class="rank')
arr1[0]
arr1[1]
arr1[2]
arr1[3]
arr1[4]
arr1[5]
arr1[6]
arr1[7]
#====================================
import re
temp = html_data.split('<li><i class="rank')[1]
print(temp)
body = re.search('<span class="txt">.*', temp, re.I | re.S)
print(body)
# re.IGNORECASE 또는 re.I 옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션
# re.S or DOTALL(S) -. 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
body = re.search('<span class="txt">.*',temp,re.I|re.S)
print(body)
body = body.group()
print(body)
body = re.sub('<.+?>','',body)  # tag 모두 제거
print(body)

# 과제 - 1.내용 잘라내는것을 반복문으로 변경
#       2. 잘라진 값에 문자열에 저장
#       3. 파일에 내용 저장 - world.txt 저장하세요

print(html_data.split('<li><i class="rank'[1]))

import requests
URL = 'http://www.segye.com'
response = requests.get(URL)
html_data = response.text
print(html_data)
print(html_data.find('div id="wps_layout1_box4" data-desc"'))

import re
temp = html_data.split('<li><i class="rank')[1]
print(temp)
temp_data = html_data.split('<li><i class="rank')
print(type(temp_data))
print(temp_data[1])
print(temp_data[2])
print(temp_data[3])
print(temp_data[4])
print(temp_data[5])
print('-----------------------------------------')
nujuk = ""
for i in range(1, 6):
    if i == 5:
        rank_vale = temp_data[i][0]
        temp_data1 = temp_data[i].split("</span></a></li>")
        body = re.search('<span class="txt">.*', temp_data1[0], re.I | re.S)
        body = body.group()
        body = re.sub('<.+?>', '', body)  # tag 모두 제거
        nujuk += body

    else:
        rank_vale = temp_data[i][0]
        body = re.search('<span class="txt">.*', temp_data[i], re.I | re.S)
        body = body.group()
        body = re.sub('<.+?>', '', body)  # tag 모두 제거
        nujuk += body

f = open("crawling-segye.txt",'w',encoding='UTF-8')
f.write(response.text)
f.close()

nujuk = ""
for i in range(5,6):
    print(i)
    rank_vale = temp_data[i][0]
    print(rank_vale)
    temp_data1 = temp_data[i].split("</span></a></li>")
    print(temp_data1[0])
    body = re.search('<span class="txt">.*', temp_data1[0], re.I | re.S)
    body = body.group()
    body = re.sub('<.+?>', '', body)  # tag 모두 제거
    print(body)
    nujuk += body
print(nujuk)
f = open("crawling-segye.txt",'w',encoding='UTF-8')
f.write(response.text)
#f.writelines(t)
#f.writelines(l)
f.close()

