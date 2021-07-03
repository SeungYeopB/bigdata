# 저장 file(02.crime_in_seoul_include_gu_name.csv) 을 읽어서
# 구별로 자료를 pivot_table 이용해서 값을 합쳐 주세요 , index : 구별 , np.sum 사용

import pandas as pd
import numpy as np

crime_data_org = pd.read_csv('./02.crime_in_seoul_include_gu_name.csv',encoding='utf-8')
crime_data_org
crime_data_org.info()
crime_dataN = pd.pivot_table(crime_data_org,index='구별',aggfunc=np.sum)
crime_dataN

# data 정리
# 검거율 을 계산 하세요 - 검거 / 발생 * 100
# 검거 자료(5가지)만 삭제 하세요, Unnamed: 0 항목도 삭제 해 주세요
# 삭제 : 열삭제 :   행삭제 :
# 검거율 을 계산 하세요 - 검거 / 발생 * 100
crime_dataN['강간검거율'] = crime_dataN['강간 검거']/crime_dataN['강간 발생']*100
crime_dataN['강도검거율'] = crime_dataN['강도 검거']/crime_dataN['강도 발생']*100
crime_dataN['살인검거율'] = crime_dataN['살인 검거']/crime_dataN['살인 발생']*100
crime_dataN['절도검거율'] = crime_dataN['절도 검거']/crime_dataN['절도 발생']*100
crime_dataN['폭력검거율'] = crime_dataN['폭력 검거']/crime_dataN['폭력 발생']*100
# 검거 자료(5가지)만 삭제 하세요, Unnamed: 0 항목도 삭제 해 주세요
del crime_dataN['강간 검거']
del crime_dataN['강도 검거']
del crime_dataN['살인 검거']
del crime_dataN['절도 검거']
del crime_dataN['폭력 검거']
del crime_dataN["Unnamed: 0"]
crime_dataN
pd.options.display.max_columns = 999
pd.options.display.max_rows = 999
# 검거율 100%  넘는것을 100%로 수정 하세요, 1:50분 까지
# 해당 칼럼만 읽어서 처리 하세요
crime_dataN["강간검거율"]
crime_dataN["강간검거율"] > 100
crime_dataN.loc[crime_dataN["강간검거율"] > 100]
crime_dataN.loc[crime_dataN["강간검거율"] > 100,"강간검거율"]
col_list = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
for col   in col_list:
    print(crime_dataN.loc[crime_dataN[col] > 100, col])
    crime_dataN.loc[crime_dataN[col] > 100, col] = 100

for col   in col_list:
    print(crime_dataN.loc[crime_dataN[col] > 100, col])

crime_dataN
# 강간 발생 -> 강간 변경 해주세요 , 5개 칼럼
# rename() 사용
crime_dataN.rename(columns={'강간 발생':'강간',
                            '강도 발생':'강도',
                            '살인 발생':'살인',
                            '절도 발생':'절도',
                            '폭력 발생':'폭력'
                            },inplace=True)
crime_dataN
# 정규화 - normalize -  강간  강도  살인    절도    폭력
# 편차 줄이는 작업
# sklearn 가지고 데이터 정규화
# pip install sklearn
from sklearn import preprocessing
col = ['강간','강도','살인','절도','폭력']
print(col)
x = crime_dataN[col].values
print(x)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x.astype(float))
print(x_scaled)
crime_data_no = pd.DataFrame(x_scaled,
                             columns = col,
                             index = crime_dataN.index)
print(crime_data_no)
# 뒤에 검거율 자료를 crime_data_no 에 붙여 주세요 2:50 까지
crime_dataN.columns
col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율','폭력검거율']
print(col2)
crime_data_no[col2] = crime_dataN[col2]
crime_data_no.head()

# cctv 데이터 - cctv result(01. CCTV_result.csv)자료 를 가져다가
# crime_data_no 에 인구수, 소계 칼럼을 -> 인구수, CCTV 칼럼으로 추가 하세요 3:15 까지
cctv_result = pd.read_csv('./01. CCTV_result.csv',encoding='utf-8',index_col='구별')
cctv_result
crime_data_no[['인구수','CCTV']] = cctv_result[['인구수','소계']]
crime_data_no

# 항목추가 - 범죄  = 강간  +강도 + 살인 + 절도  +폭력
# 항목추가 - 검거 = 강간검거율  +강도검거율 + 살인검거율 + 절도검거율  +폭력검거율
col = ['강간','강도','살인','절도','폭력']
crime_data_no['범죄'] = np.sum(crime_data_no[col],axis=1 )
crime_data_no
col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율','폭력검거율']
crime_data_no['검거'] = np.sum(crime_data_no[col2],axis=1 )
crime_data_no


# 범죄 시각화 하기  11:00 시까지
# matplotlib , seaborn import
# pairplot 그리세요, crime_data_no를 가져다 항목을 "강도", "살인", "폭력" , 회귀선도 포함
# size = 3 으로 해서 그래프를 그리세요
# x, y 축 내용 - 한글 출력 적용 해주세요

import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic'
sns.pairplot(crime_data_no, vars=["강도", "살인", "폭력"], kind = 'reg', size = 3)
plt.show()

# 인구수, CCTV(x축)  vs 살인  강도(y축)  pairplot을 만드세요 , 회귀선도 포함  11:15분 까지
# size = 3 으로 해서 그래프를 그리세요
# x, y 축 내용 - 한글 출력 적용 해주세요

sns.pairplot(crime_data_no, x_vars=["인구수","CCTV", ], \
             y_vars=["살인","강도", ], kind = 'reg', size = 3)
plt.show()

# 인구수, CCTV(x축)  vs 살인검거율  폭력검거율(y축)  pairplot을 만드세요 , 회귀선도 포함  11:15분 까지
# size = 3 으로 해서 그래프를 그리세요
# x, y 축 내용 - 한글 출력 적용 해주세요

sns.pairplot(crime_data_no, x_vars=["인구수","CCTV", ], \
             y_vars=["살인검거율","폭력검거율", ], kind = 'reg', size = 3)
plt.show()


crime_data_no['검거']  # 이값의 최고값을 100 으로 한정하고 그값으로 정렬
# 이값의 최고값 계산
work_tmp  = crime_data_no['검거'].max()
print(work_tmp)
# work_tmp를 100 으로 한정하고 , 검거에 값을 백분률로 계산
crime_data_no['검거'] = crime_data_no['검거'] / work_tmp * 100
# sort 작업
crime_data_no_sort = crime_data_no.sort_values(by='검거',ascending=False)
crime_data_no_sort.head()
display_col = ['강간검거율', '강도검거율', '살인검거율', '절도검거율','폭력검거율']
plt.figure(figsize= (10,10))
sns.heatmap(crime_data_no_sort[display_col],annot=True,fmt='f',linewidths=0.5)
plt.title("범죄 검거 비율(정규화된 검거 합으로 정렬)")
plt.show()
# 항목 col = ['강간','강도','살인','절도','폭력']  <- 발생 건수
# crime_data_no['범죄'] - > ['강간','강도','살인','절도','폭력']  합친 항목
# crime_data_no['범죄'] 평균값 - ['범죄'] / 5  계산 하고 , sort 하고 heatmap 그리기
# title( "범죄 발생 비율(정규화된 발생건수 으로 정렬)" )

col = ['강간','강도','살인','절도','폭력']
crime_data_no['범죄'] = crime_data_no['범죄'] / 5
crime_data_no_sort = crime_data_no.sort_values(by='범죄',ascending=False)
plt.figure(figsize= (10,10))
sns.heatmap(crime_data_no_sort[col],annot=True,fmt='f',linewidths=0.5)
plt.title("범죄 발생 비율(정규화된 발생건수 으로 정렬)")
plt.show()

# crime_data_no 자료를 저장 - csv  이름 02.crime_in_Seoul_final.csv 로 저장 하세요
crime_data_no.to_csv('./02.crime_in_Seoul_final.csv',sep=',',encoding='utf-8')


# 오후 지도에 표시하기 작업

import folium
import json
geo_path = './02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path,encoding='utf-8'))
geo_str

map = folium.Map(location=[37.5502,126.982],zoom_start=11,
                 tiles='Stamen Toner')
map.choropleth(geo_data=geo_str, data=crime_data_no['살인'],
               columns=[crime_data_no.index,crime_data_no['살인']],
               key_on='feature.id',
               fill_color='PuRd')
               #lengend_name='Unemployment Rate (%)')
map.save("./map_Soule01.html")

# '절도' 항목에 대해 지도를 그려보세요
# file명 :./map_Soule02.html"
map = folium.Map(location=[37.5502,126.982],zoom_start=11,
                 tiles='Stamen Toner')
map.choropleth(geo_data=geo_str, data=crime_data_no['절도'],
               columns=[crime_data_no.index,crime_data_no['절도']],
               key_on='feature.id',
               fill_color='PuRd')
               #lengend_name='Unemployment Rate (%)')
map.save("./map_Soule02.html")


# 인구대비 범죄('폭력')발생 비율 계산 해서 지도에 표시해 보세요
#   '폭력' / 인구 * ?

work_crime =  crime_data_no["폭력"] / crime_data_no["인구수"] * 1000000
work_crime
map = folium.Map(location=[37.5502,126.982],zoom_start=11,
                 tiles='Stamen Toner')
map.choropleth(geo_data=geo_str, data=work_crime,
               columns=[crime_data_no.index,work_crime],
               key_on='feature.id',
               fill_color='PuRd')
               #lengend_name='Unemployment Rate (%)')
map.save("./map_Soule03.html")


# 서울시 경찰서별 검거율과 구별 범죄 발생율 시각화

# seoul 범죄 정보 처리
# import
import numpy as np
import pandas as pd

crime_data = pd.read_csv('./02. crime_in_Seoul.csv', thousands=',',encoding='euc-kr')
crime_data.head()

crime_data.info()


#pip install googlemaps
import googlemaps

gmap_key = 'AIzaSyDF9WHBo8fdeAcNcNZL2qwyx3Lb8P9_Skk'  # <- 발행한 키값 넣으세요
gmaps = googlemaps.Client(key=gmap_key)

gmaps.geocode('서울중부경찰서',language='ko')
# 위도 경도 정보 가져옵니다.
# crimte data 가져다   관서명을 가져다가  -> "중부서" ->  '서울중부경찰서' 형식으로 data 가공 해서
# 반복문 사용해서 작성
# list에 저장 하세요.
police_name  = []
for name in crime_data['관서명']:
    #print('서울'+name[:-1]+'경찰서')
    police_name.append('서울'+name[:-1]+'경찰서')
print(police_name)
# 위도 경도 정보를 gmaps.geocode('서울중부경찰서',language='ko') 가져오세요.
# police_address =[] - 주소
# police_lat = []    - 위도
# police_lng = []    - 경도
police_address =[]
police_lat = []
police_lng = []
for name in police_name:
    #print(name)
    work = gmaps.geocode(name, language='ko')
    #print(work[0].get("formatted_address"))
    police_address.append(work[0].get("formatted_address"))
    work_loc = work[0].get("geometry")
    #print(work_loc)
    #print(work_loc['location']['lat'])
    police_lat.append(work_loc['location']['lat'])
    #print(work_loc['location']['lng'])
    police_lng.append(work_loc['location']['lng'])
police_address

# 경찰서 위치 정보
police_lat
police_lng

crime_data_org = pd.read_csv('./02.crime_in_seoul_include_gu_name.csv',encoding='utf-8')
crime_data_org.info()
crime_data_org['lat'] = police_lat
crime_data_org['lng'] = police_lng
crime_data_org
display_col = ['강간 검거', '강도 검거', '살인 검거', '절도 검거','폭력 검거']
work_tmp =  crime_data_org[display_col] / crime_data_org[display_col].max()
crime_data_org['검거'] = np.sum(work_tmp, axis=1)
crime_data_org.head()
# 경찰서 위치 표시
map = folium.Map(location=[37.5502,126.982],zoom_start=11)
for n in crime_data_org.index:
    #print(n)
    folium.Marker([crime_data_org['lat'][n],
                  crime_data_org['lng'][n]]).add_to(map)
map.save("./map_Soule04.html")
# 경찰서 검거율 표시
map = folium.Map(location=[37.5502,126.982],zoom_start=11)
for n in crime_data_org.index:
    #print(n)
    folium.CircleMarker([crime_data_org['lat'][n],
                        crime_data_org['lng'][n]],
                        radius = crime_data_org['검거'][n]*10,
                        color='#3186cc',fill_color="Red").add_to(map)
map.save("./map_Soule05.html")

# 경찰서 검거율 표시,구별 범죄율
map = folium.Map(location=[37.5502,126.982],zoom_start=11)
map.choropleth(geo_data=geo_str, data=crime_data_no['범죄'],
               columns=[crime_data_no.index,crime_data_no['범죄']],
               key_on='feature.id',
               fill_color='PuRd')
for n in crime_data_org.index:
    #print(n)
    folium.CircleMarker([crime_data_org['lat'][n],
                        crime_data_org['lng'][n]],
                        radius = crime_data_org['검거'][n]*10,
                        color='#3186cc',fill_color="Red").add_to(map)
map.save("./map_Soule06.html")

## 복습 인천시 초중고등학교를 지도에 위치를 표시하고 학교명을 표시해주세요
## 자료 찾기 인천시 초중고등학교 정보찾기
# 알아서 찾으세요
# 자료 가공 - 인천시 학교 정보 , 위치정보 추출
# 지도에 표시 - 마크에 누르면 학교명 나오게 해주세요

import folium

data = pd.read_csv("./korea_school_information_2021.csv", encoding="utf-8")
data.info()
data[("특성화고")]
data.head()
data = data.drop(["학교ID","설립일자","데이터기준일자","설립형태","본교분교구분","생성일자","변경일자","운영상태","교육지원청명","교육지원청코드",
                  "소재지도로명주소","시도교육청코드","시도교육청명"], axis=1)
filter = data["소재지지번주소"].str.contains("인천광역시")
filter
data
incheon_school_df = data[filter]
incheon_school_df
incheon_school_df.set_index('학교명', inplace=True)
print(type(incheon_school_df))
map = folium.Map(location=[37.47526,126.661492],zoom_start=12)
for index, row in incheon_school_df.iterrows():
    folium.Marker([row['위도'], row['경도']], popup="<div style='white-space:nowrap;'> 🏪 "+index+"</div>").add_to(map)

map.save("./map_Incheon1.html")

import numpy as np
import folium

data1 = pd.read_csv("./서울특별시 고등학교 기본정보.csv", encoding="utf-8")
data1.info()
data1.head()


data1 = data1.drop(["표준학교코드","영문학교명","관할조직명","도로명우편번호","도로명상세주소",
                   "전화번호","홈페이지주소","팩스번호","고등학교구분명","산업체특별학급존재여부",
                   "고등학교일반실업구분명","특수목적고등학교계열명","입시전후기구분명","주야구분명","설립일자",
                   "개교기념일","시도교육청코드","시도교육청명","소재지명","적재일시"], axis=1)
filter1 = data1["남녀공학구분명"].str.contains("남")
filter1
data1
seoul_school_data = data1[filter1]
seoul_school_data
seoul_school_data.set_index("학교종류명", inplace=True)
seoul_school_data
map1 = folium.Map(location=[37.5626, 126.9878],zoom_start=12)
for index, row in seoul_school_data.iterrows():
    print(row)
    folium.Marker([row['도로명주소']],
                  popup="<div style='white-space:nowrap;'> 🏪 " + row["남녀공학구분명"] + "</div>").add_to(map)
map.save("./map_Seoul13.html")

data2 = pd.read_csv("./전국초중등학교위치표준데이터.csv", encoding="utf-8")
data2
data["특성화고"]
data2.info()
data2.head()
data2[]
data2[["학교명","시도교육청코드"]]
data2[data2["시도교육청코드"] == 7310000]
filter2 = data2[data2["시도교육청코드"] == 7310000]
filter2
school_data = filter2[["학교명","위도","경도"]]
school_data.set_index("학교명", inplace=True)
school_data
map = folium.Map(location=[37.4564,126.7056], zoom_start=13)
for index, row in school_data.iterrows():
    folium.Marker([row['위도'], row['경도']], popup="<div style='white-space:nowrap;'> 🏪 " + index + "</div>").add_to(map)
map.save("./map_incheon1234.html")
school_data["경도"] > 126.743
sd = school_data[school_data["경도"] > 126.743]
sd
school_data2 = school_data.drop(sd)
school_data2
