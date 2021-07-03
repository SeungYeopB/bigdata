# seoul 범죄 정보 처리
# import
import numpy as np
import pandas as pd

crime_data = pd.read_csv("./02. crime_in_Seoul.csv", thousands=",", encoding="euc-kr")
crime_data.head()
crime_data.info()

import googlemaps
gmap_key = "AIzaSyDF9WHBo8fdeAcNcNZL2qwyx3Lb8P9_Skk"
gmaps = googlemaps.Client(key=gmap_key)

gmaps.geocode("서울중부경찰서", language="ko")
# 위도 경도 정보 가져옵니다.
# crime_data 가져다 "중부서"->  "서울중부경찰서" 형식으로 data 가공 해서


# 위도 경도 정보를 gmaps.geocode("서울중부경찰서",language="ko") 가져오세요
# 반복문 사용해서 작성
# list 에 저장하세요
police_name = []
for name in crime_data["관서명"]:
    print("서울" + name[:-1]+"경찰서")
    police_name.append("서울"+name[:-1]+"경찰서")
print(police_name)
# 위도 경도 정보를 gmaps.geocode("서울중부경찰서",language="ko") 가져오세요
##police_address = []  -- 주소
##police_lat = []      -- 위도
##police_lng = []      -- 경도
police_address = []
police_lat = []
police_lng = []
for name in police_name:
    print(name)
    work = gmaps.geocode(name, language="ko")
    police_address.append(work[0].get("formatted_address"))
    work_loc = work[0].get("geometry")
    police_lat.append(work_loc["location"]["lat"])
    police_lng.append(work_loc["location"]["lng"])
police_address
police_lat
police_lng
crime_data.columns  # 맨끝에 구별 칼럼을 만들고 구정보를 집어 넣으세요.
# police_address 정보에서 구별 정보를 발췌해서 칼럼에 추가
# hint split()
# 구로 끝나는것을 찾아 list에 추가, "구별 " 이란 칼럼으로 추가 하세요
gu_list = []
for juso in police_address:
    #print(juso)
    work = juso.split()
    #print(work)
    work_gu = [gu for gu in work if gu[-1] == "구"][0]
    #print(work_gu)
    gu_list.append(work_gu)
print(gu_list)
crime_data["구별"] = gu_list
crime_data.head()
crime_data.[구별["금천구"]]
crime_data[crime_data["구별"] == "중구"]

# data 저장 현재 디렉터리에 "02.crime_in_seoul_include_gu_name.csv"로 저장하세요.
# to_csv() 로 저장
crime_data.to_csv("./02.crime_in_seoul_include_gu_name.csv", sep=",", encoding="utf-8")
crime_data.to_csv("./02.crime_in_seoul_include_gu_name.csv", encoding="utf-8")
crime_data_new = pd.read_csv("./02.crime_in_seoul_include_gu_name.csv", thousands=",", encoding="utf-8")
crime_data_new.head()




work = ['대한민국', '서울특별시', '중구', '을지로동', '수표로', '27']
print(type(work))
for gu in work:
    #print(gu)
    #print(type(gu))
    if gu[-1] == "구":
        print(gu)