import numpy as np
import pandas as pd
import googlemaps
import folium
import matplotlib.pyplot as plt
import seaborn as sns

##data = pd.read_excel("2016_middle_shcool_graduates_report.xlsx")  # 이것도 되지만 변수 만들어서 하는게 정석적인느낌
file_path ="2016_middle_shcool_graduates_report.xlsx"

data = pd.read_excel(file_path, header=0)
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 100)

print(data.index)
data.columns
data.index
data.describe()
print(type(data))
data.head()
data.loc[0,:].unique()
# 구별 진학율
data.columns
jinhak = data['일반고']+data['특성화고']+data['과학고']+data['외고_국제고']+data['예고_체고']\
         +data['마이스터고']+data['자사고']+data['자공고']+data['기타진학']
jinhak
jinhak.unique()
data["진학율"]=jinhak
data.columns
data["특성화고"]

jinhak_on_special = data['특성화고']+data['과학고']+data['외고_국제고']
jinhak_on_special
data["특수고 진학율"]=jinhak_on_special
data.columns
data.info()
data.describe()

## 구별 진학율
data.head()
gu_jinhak = pd.pivot_table(data, index=["지역"], values=["진학율"], aggfunc=np.mean)
gu_jinhak.head()

gu_list = data['지역'].unique()
gu_list
gu_jinhak_rate = []
for gu in gu_list:
    filter = data['지역'] == gu
    data_gu = data[filter]
    print(data_gu)
    total_student = 0;
    total_jinhak = 0;
    for i in range(len(data_gu)):
        total_student += data_gu.iloc[i]['남학생수']+data_gu.iloc[i]['여학생수']
        total_jinhak += (data_gu.iloc[i]['남학생수']+data_gu.iloc[i]['여학생수']) * data_gu.iloc[i]['진학율']
    gu_jinhak_rate.append({
      '구': gu,
    '진학률':  int(total_jinhak) / total_student
    })



gu_jinhak_rate
#지도에 표시
map = folium.Map(location=[37.5664,126.9779], tiles="Stamen Terrain", zoom_start=12)
map.save("./seoul_school01.html")

## 좌표 정보 가져오기
gmap_key = 'AIzaSyDF9WHBo8fdeAcNcNZL2qwyx3Lb8P9_Skk'  # <- 발행한 키값 넣으세요
gmaps = googlemaps.Client(key=gmap_key)

gmaps.geocode("서울대학교사범대학부설중학교",language="ko")

school_name = []
for name in data["학교명"]:
    #print()
    school_name.append(name)
school_name

school_lat = []
school_lng = []
school_loc = []  ## 서울 특별시면 "T", 아니면 "F"
for name in school_name:
    # gmaps.geocode(name, language="ko")
    work = gmaps.geocode(name, language="ko")
    work_loc = work[0].get("geometry")
    school_lat.append(work_loc["location"]["lat"])
    school_lng.append(work_loc["location"]["lng"])
    work_addr = work[0].get("formatted_address")
    #print(work_addr.split()[1])
    print("running")
    if work_addr.split()[1] == "서울특별시":
            school_loc.append("T")
    else:
            school_loc.append("F")
school_lat
school_lng
school_loc
data["위도"]=school_lat
data["경도"]=school_lng
data["서울"]=school_loc
data.head()
data[data["서울"] == "T"].count()
data[data["서울"] == "F"].count()
map = folium.Map(location=[37.5664,126.9779], tiles="Stamen Terrain", zoom_start=12)
for name, lat, lng in zip(data.학교명,data.위도,data.경도):
    folium.CircleMarker([lat, lng],
                        radius=5,
                        color="brown",
                        fill=True,
                        fill_color="coral",
                        fill_opacity=8.7,
                        popup=name
                        ).add_to(map)
map.save("./seoul_school02.html")


#서울 아닌곳 뺴기
map = folium.Map(location=[37.5664,126.9779], tiles="Stamen Terrain", zoom_start=12)
for name, lat, lng,seoul_tf in zip(data.학교명, data.위도, data.경도, data.서울):
    if seoul_tf == "T":
        folium.CircleMarker([lat, lng],
                            radius=5,
                            color="brown",
                            fill=True,
                            fill_color="coral",
                            fill_opacity=8.7,
                            popup=name
                            ).add_to(map)
map.save("./seoul_school03.html")

## 구별로 진학율 표시
data["진학율"]
gu_jinhak
import json
geo_path = "./02. skorea_municipalities_geo_simple.json"
geo_str = json.load(open(geo_path, encoding="utf-8"))
geo_str

map = folium.Map(location=[37.5664,126.9779], tiles="Stamen Terrain", zoom_start=12)
map.choropleth(geo_data=geo_str,
               data = gu_jinhak,
               columns=[gu_jinhak.index, "진학율"],
               fil_color="PuRd",
               key_on="feature.id")
map.save("./seoul_school04.html")

## 특수 학교 진학율 상위 10, 하위 10 - 값이 0 인것
jinhak_top = data.sort_values(by="특수고 진학율", ascending=False).head(10)
jinhak_top

## 진학율이 0 인것 골라내서 삭제 하위 10개 선정
data1_d_index = data[data["특수고 진학율"] == 0].index
data1_d_index
data1 = data.drop(data1_d_index)
data1["특수고 진학율"].unique()
jinhak_bot = data1.sort_values(by="특수고 진학율", ascending=True).head(10)
jinhak_bot


map = folium.Map(location=[37.5664, 126.9779],tiles='Stamen Terrain',zoom_start=12)
for n in jinhak_top.index:
        if pd.notnull(jinhak_top['위도'][n]):
                folium.CircleMarker([jinhak_top['위도'][n],jinhak_top['경도'][n]],
                                    popup=("<div style='white-space:nowrap;'> 🏪 " + n + "</div>").add_to(map),
                                    radius=5,
                                    color='#CD3181',
                                    fill=True,
                                    fill_color='#CD3181',
                                    fill_opacity=8.7,
                                    #popup=name
                                    ).add_to(map)
for n in jinhak_bot.index:
        if pd.notnull(jinhak_bot['위도'][n]):
                folium.CircleMarker([jinhak_bot['위도'][n],jinhak_bot['경도'][n]],
                                    radius=5,
                                    color='#3186cc',
                                    fill=True,
                                    fill_color='#3186cc',
                                    fill_opacity=8.7,
                                    #popup=name
                                    ).add_to(map)
map.save('./seoul_school05.html')


