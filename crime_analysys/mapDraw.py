import folium


# pycharm, spyder - 지도가 바로 안그려진다.
# jupeter notebook - 지도가 바로 그려진다.

map_osm = folium.Map(location=[37.59073, 126.97817])   # pycharm, spyder - 지도가 바로 안그려진다.
map_osm.save("./map_osm01.html")


# 인천시 - 중앙 위도 경도값 가져다 지도 그려보세요
# opnion zoom start = 13
map_osm = folium.Map(location=[37.45625816028772, 126.70595612320191],
                     tiles="stamen Terrain",zoom_start=18)     # pycharm, spyder - 지도가 바로 안그려진다.
map_osm.save("./map_osm02.html")
 # option tiles = "Stamen Terrain", "Stamen Toner"

map_osm = folium.Map(location=[37.45625816028772, 126.70595612320191],
                     tiles="stamen Toner",zoom_start=18)
map_osm.save("./map_osm03.html")

map_osm = folium.Map(location=[37.45625816028772, 126.70595612320191],
                     tiles="stamen Toner",zoom_start=15)
folium.Marker([37.4564, 126.7057], popup="incheon").add_to(map_osm)
folium.CircleMarker([37.4563, 126.7058], radius=50,  # radius = 범위
                    popup="incheon", color="#3186cc",  # popup = 마커이름
                    fill_color="red").add_to(map_osm)  #fill_color = 마커에 채워질 색
map_osm.save("./map_osm04.html")

# 02. folium_US_Unemployment_Oct2012.csv 를 state_data로 읽어 들이세요
# import pandas as pd
import pandas as pd
state_data = pd.read_csv("./02. folium_US_Unemployment_Oct2012.csv")
state_data
state_geo = './02. folium_us-states.json'

map = folium.Map(location=[40,-98], zoom_start=4)
map.choropleth(geo_data=state_geo, data=state_data,
               columns=['State','Unemployment'],
               key_on='feature.id',
               fill_color='YlGn',
               lengend_name='Unemployment Rate (%)')
map.save("./map_osm05.html")

## https://github.com/southkorea/southkorea-maps 우리나라 행정구역 위치 정보
#  https://github.com/PinkWink/DataScience/tree/master/data


