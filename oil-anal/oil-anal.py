import pandas as pd
from glob import glob
import os

os.path.exists("./oil-data/지역_위치별(주유소).xls")
glob("./oil_data/*xls")
juyuso_file = glob("./oil-data/*xls")

work_data = []
for file_name in juyuso_file:
    #print(file_name)
    work = pd.read_excel(file_name, header=2)
    work_data.append(work)
work_data

juyuso_raw = pd.concat(work_data)   # 데이터 합쳣다
juyuso_raw.info()
juyuso_raw.head()

juyuso = pd.DataFrame({"주유소":juyuso_raw["상호"],
                       "주소":juyuso_raw["주소"],
                       "가격":juyuso_raw["휘발유"],
                       "셀프":juyuso_raw["셀프여부"],
                       "상표":juyuso_raw["상표"]})
juyuso.index
juyuso.columns

juyuso["구"] = [juso.split()[1] for juso in juyuso["주소"]]
for juso in juyuso["주소"]:
    print(juso)
    juso1 = juso.split()
    print(juso1[1])
juyuso.head()
juyuso["구"].unique()
juyuso.loc[juyuso["구"] == "서울특별시"]
juyuso.loc[juyuso["구"] == "서울특별시","구"] = "성동구"
juyuso.loc[juyuso["구"] == "서울특별시"]
juyuso["구"].unique()

juyuso.loc[juyuso["구"] == "특별시"]
juyuso.loc[juyuso["구"] == "특별시","구"] = "도봉구"
juyuso.loc[juyuso["구"] == "특별시"]

juyuso["가격"].unique()
print(type(juyuso["가격"]))

juyuso[juyuso["가격"]=="-"]
juyuso[juyuso["가격"]=="도봉구"]
juyuso[juyuso["가격"]=="성동구"]

juyuso = juyuso[juyuso["가격"] !="-"]
juyuso[juyuso["가격"] =="-"]
juyuso[juyuso["가격"] !="-"]
print(type(juyuso))

juyuso["가격"].unique()
juyuso["가격"] = [float(value) for value in juyuso["가격"]]
juyuso["가격"]
juyuso["가격"].unique()
juyuso.index
juyuso.head()
juyuso.reset_index(inplace=True)
juyuso.index
juyuso.head()
juyuso.columns
del juyuso["index"]
juyuso.columns
juyuso.info()

# boxplot 그리기
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
import seaborn as sns
# 한글 세팅
path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family=font_name)

# plt.rcParams['font.family'] = 'Malgun Gothic' - matplot lib 사용시
juyuso.boxplot(column='가격',by='셀프',figsize=(10,8))

plt.figure(figsize=(10,8))
sns.boxplot(x='상표',y='가격',hue='셀프',data=juyuso,palette='Set3')

##  하나의 데이터 프레임에 합치기 - glob()함수사용
##  oil-data 압축 파일 해당 프로젝트에 압축 풀기
##  for 사용
##  합쳐진 자료를 주유소 주소 가격(휘발유만) 셀프 상표의 구조로 새로 생성하시오
##  구정보를 추출하여 새로운 칼럼을 생성하시요
##  (구명이 잘들어 갔는지 검증하시오)
##  숫자 칼럼을 확인해서 자료가 자롬ㅅ 들어간 행은 제외하시오
##  2. boxplot으로 셀프 주유소 대비 가격을 그리시요
##  (셀프와 셀프가 아닌것을 구분하시오-hue)
##  상표 대비 가격을 그리시요.

##  3.구별 평균 휘발유 가격을 지도에 표시하시오
# 구별 평균 휘발유 가격 지도에 표시하기
import json
import folium
import googlemaps


juyuso.sort_values(by='가격',ascending=False).head() # 내림 차순
juyuso.sort_values(by='가격',ascending=True).head() # 오름 차순

import numpy as np
gu_data = pd.pivot_table(juyuso,index=['구'], values=['가격'],
                         aggfunc=np.mean)
gu_data.head()
gu_data.index
# 서울시 구별 경계좌표 가져 오기
geo_path ='./oil-data/02. skorea_municipalities_geo_simple.json'
geo_data = json.load(open(geo_path,encoding='utf-8'))
geo_data

map = folium.Map(location=[37.5664, 126.9778],zoom_start=12.5,tile='Stamen Toner')
map.choropleth(geo_data=geo_data,
               data= gu_data,
               columns=[gu_data.index,'가격'],
               fill_color='PuRd',
               key_on='feature.id')
map.save('./juyuso01.html')

# 서울시 주유 가격 상하위 10개 주유소 지도 표시

oil_top10 = juyuso.sort_values(by='가격',ascending=False).head(10)
oil_top10

oil_bot10 = juyuso.sort_values(by='가격',ascending=True).head(10)
oil_bot10

gmap_key = 'AIzaSyDF9WHBo8fdeAcNcNZL2qwyx3Lb8P9_Skk'  # <- 발행한 키값 넣으세요
gmaps = googlemaps.Client(key=gmap_key)

juyuso_lat = []
juyuso_lng = []
for n  in oil_top10.index:
    #print(n)
    work = str(oil_top10['주소'][n]).split('(')[0]
    #print(work)
    work_map = gmaps.geocode(work)
    #print(work_map)
    work_loc = work_map[0].get("geometry")
    juyuso_lat.append(work_loc['location']['lat'])
    juyuso_lng.append(work_loc['location']['lng'])

print(juyuso_lat)
print(juyuso_lng)
oil_top10['lat'] = juyuso_lat
oil_top10['lng'] = juyuso_lng
oil_top10

juyuso_lat = []
juyuso_lng = []
for n  in oil_bot10.index:
    #print(n)
    work = str(oil_bot10['주소'][n]).split('(')[0]
    #print(work)
    work_map = gmaps.geocode(work)
    #print(work_map)
    work_loc = work_map[0].get("geometry")
    juyuso_lat.append(work_loc['location']['lat'])
    juyuso_lng.append(work_loc['location']['lng'])

print(juyuso_lat)
print(juyuso_lng)
oil_bot10['lat'] = juyuso_lat
oil_bot10['lng'] = juyuso_lng
oil_bot10

map = folium.Map(location=[37.5664, 126.9778],zoom_start=12.5,tile='Stamen Toner')
for n in  oil_top10.index:
    folium.CircleMarker([oil_top10['lat'][n],oil_top10['lng'][n]],
                        radius=15, color="#CD3181",
                        fill_color="#CD3181").add_to(map)
for n in  oil_bot10.index:
    folium.CircleMarker([oil_bot10['lat'][n],oil_bot10['lng'][n]],
                        radius=15, color="#3186cc",
                        fill_color="#3186cc").add_to(map)
map.save('./juyuso-top10.html')

### 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#[Step 1] 데이터 준비 -  자동차 연비 데이터셋 가져오기
data = pd.read_csv('./auto-mpg.csv', header=None)
data
# 열이름 지정
data.columns = ['mpg','cylinders','displacement','horsepower','weight',
                'acceleration','model year','origin','name']
data.info()
data.index
data.columns

#[Step 2] 데이터 탐색
# 데이터 자료형 확인
data.info()
# 데이터 통계 요약정보 확인  - 수치형 자료
data.describe()
data['mpg'].describe()
data['horsepower'].describe()
data['horsepower'].unique()
data[data['horsepower'] == '?']   # ->  horsepower 내용 보는 방법?
# column 조정
pd.set_option('display.max_columns',100)
data[data['horsepower'] == '?']
# 찾은 자료중 horsepower 항목만 보기
data[data['horsepower'] == '?']['horsepower']
# horsepower -  "?" 된자료는 삭제
# "?" 자료는 non 값으로 변경후 삭제
data['horsepower'].replace("?",np.nan, inplace=True)
data['horsepower'].unique()
data.dropna(subset=['horsepower'],axis=0,inplace=True)
data['horsepower'].unique()
# horsepower -  수치형 자료 변환
data['horsepower'] = data['horsepower'].astype('float')
data['horsepower'].unique()
#[Step 3] 속성(feature 또는 variable) 선택
# 분석에 활용할 열(속성)을 선택 ndata로 만들기
# (연비, 실린더, 출력, 중량)-'mpg', 'cylinders', 'horsepower', 'weight'
ndata = data[['mpg','cylinders','horsepower','weight']]
ndata

### 종속 변수 Y인 "연비(mpg)"와
#x='cylinders', 'horsepower','weight', y='mpg' 변수 만들기
# x 독립 변수 만들기
x= ndata[['cylinders','horsepower','weight']]
x
# y 종속변수 만들기
y = data[['mpg']]
y

# 자료분리 - train(학습용) 7 , test(검증용) 3
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=10)

print('학습데이터 :',x_train.shape )
print('검증데이터 :',x_test.shape )

# 회귀 분석 모형 적용
from sklearn.linear_model import LinearRegression
# 모형   객체 생성
lr = LinearRegression()
# train data를 가지고 학습
lr.fit(x_train, y_train)
# 학습된 모형  에 test data 적용 결정계수 계산
r_score = lr.score(x_test, y_test)
print(r_score)

#  회귀식의 기울기
# lr.coef_
print('x의 변수의 계수 a :' , lr.coef_)

# 회귀식의 절편
# lr.intercept_
print('상수값 b :' , lr.intercept_)

# 회귀선 그래프 출력 비교
# y_test 와 x_test를 가지고 예측한값을 산출 비교 그래프 그리기
y_hat = lr.predict(x_test)

plt.figure(figsize=(10,5))
ax1 = sns.distplot(y_test, hist=False, label='y_test')
ax2 = sns.distplot(y_hat, hist=False, label='y_hat',ax=ax1)
plt.show()
plt.close()

