import pandas as pd
CCTV_Seoul = pd.read_csv('./01.CCTV_in_Seoul.csv', encoding='utf-8')
CCTV_Seoul.head()
CCTV_Seoul.columns
CCTV_Seoul.columns[0]
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
CCTV_Seoul.head()
# ## 2-2. 엑셀파일 읽기 - 서울시 인구현황
#pop_Seoul = pd.read_excel('./data/01.population_in_Seoul.xls', encoding='utf-8')
pop_Seoul = pd.read_excel('./01.population_in_Seoul.xls')
pop_Seoul.head()
pop_Seoul = pd.read_excel('./01.population_in_Seoul.xls',
                        header = 2,
                        usecols = 'B, D, G, J, N')
#                       encoding='utf-8')
pop_Seoul.head()
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',
                    pop_Seoul.columns[1] : '인구수',
                    pop_Seoul.columns[2] : '한국인',
                    pop_Seoul.columns[3] : '외국인',
                    pop_Seoul.columns[4] : '고령자'},
                    inplace=True)
pop_Seoul.head()



import pandas as pd
import numpy as np
s = pd.Series([1,3,5,np.nan,6,8])
s
dates = pd.date_range('20130101', periods=6)
dates
print(type(dates))
df = pd.DataFrame(np.random.randn(6,4), index=dates,
                    columns=['A','B','C','D'])
df
df.head()
df.head(3)
df.index
df.columns
df.values
df.info()
df.describe()
df.sort_values(by='B', ascending=False)
df
df['A']
df[0:3]
df['20130102':'20130104']
df.loc[dates[0]]
df.loc[:,['A','B']]
df.loc['20130102':'20130104',['A','B']]
df.loc['20130102',['A','B']]
df.loc[dates[0],'A']
df.iloc[3]
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
df.iloc[:,1:3]
df
df[df.A > 0]
df[df > 0]
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2
df2['E'].isin(['two','four'])
df2[df2['E'].isin(['two','four'])]
df
df.apply(np.cumsum)
df.apply(lambda x: x.max() - x.min())


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])
df1
df2
df3
result = pd.concat([df1, df2, df3])
result
result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
result
result.indexresult.index.get_level_values(0)
result.index.get_level_values(1)
result
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                    index=[2, 3, 6, 7])
result = pd.concat([df1, df4], axis=1)
df1
df4
result
result = pd.concat([df1, df4], axis=1, join='inner')
result
result = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
result
result = pd.concat([df1, df4], ignore_index=True)
result

left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
left
right
pd.merge(left, right, on='key')
pd.merge(left, right, how='left', on='key')pd.merge(left, right, how='right', on='key')
pd.merge(left, right, how='outer', on='key')
pd.merge(left, right, how='inner', on='key')

import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
plt.figure()
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()

import numpy as np
t = np.arange(0,12,0.01)
y = np.sin(t)
plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.show()

plt.figure(fogsize=(10,6))
plt.plot(t,y)
plt.grid()   # 그리드 적용하기
plt.show()

plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.grid()
plt.xiabel("time")
plt.ylabel("Amplitude")
plt.show()

plt.figure(figsize=(10,6))
plt.plot(t, y)
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t))
plt.plot(t, np.cos(t))
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()
plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t), label='sin')
plt.plot(t, np.cos(t), label='cos')
plt.grid()

plt.figure(figsize=(10,6))
plt.plot(t, y)
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t))
plt.plot(t, np.cos(t))
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()
plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t), label='sin')
plt.plot(t, np.cos(t), label='cos')
plt.grid()



import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name =\
    font_manager.FontProperties(fname=path).get_name()
 rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

data_result.head()

plt.figure()
data_result['소계'].plot(kind='barh', grid=True, figsize=(10,10))
plt.show()
data_result['소계'].sort_values().plot(kind='barh',
 grid=True, figsize=(10,10))
plt.show()
data_result['CCTV비율'] = data_result['소계'] /
data_result['인구수'] * 100
data_result['CCTV비율'].sort_values().plot(kind='barh',
 grid=True,
figsize=(10,10))
plt.show()
plt.figure(figsize=(6,6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

fp1 = np.polyfit(data_result['인구수'], data_result['소계'],
1)
fp1

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)
plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()


import urllib.request as req
from bs4 import BeautifulSoup
======================================
# 원본
import requests
#import re
#from bs4 import BeautifulSoup
#URL = 'http://movie.naver.com/movie/point/af/list.nhn?&page=1'
#response = req.get(URL)
#html_data = response.text
#print(html_data)

import urllib.request as req
import re
from bs4 import BeautifulSoup

URL = 'http://movie.naver.com/movie/point/af/list.nhn?&page=1'

res = req.urlopen(URL)
#response = requests.get(URL)
source = res.read()
#html_data = response.text
#print(html_data)

#soup = BeautifulSoup(html_data, 'html.parser')
soup = BeautifulSoup(source, 'html.parser')

soup.prettify()
body  = soup.select('tbody')
print(body)
title = soup.select('.title')
print(title)
titles = soup.select('.movie')
print(titles)
points = soup.select('td.title > div > em')
print(points)
reviews = soup.select('td.title')
print(reviews)
movie_title= []
movie_point = []
movie_review = []


for titl_txt in titles:
    #print(titl_txt.text)
    movie_title.append(titl_txt.text)
for point_txt in points:
    #print(point_txt.text)
    movie_point.append(point_txt.text)
for review_txt in reviews:
    #print(type(review_txt.contents[0]))
    #print(review_txt.contents[6])

    review_data = review_txt.contents[6]
    print(review_data)
    review_data = re.sub("신고","",review_data)
    print(review_data)
    review_data = re.sub("[\n\t]", "", review_data)
    movie_review.append(review_data)

count = len(movie_title)
print(count)

for i in range(count):
    print("영화 제목 :" + movie_title[i])
    print("영화 평점 :" + movie_point[i])
    print("영화 리뷰 :" + movie_review[i])
    print("-------------------------------")
