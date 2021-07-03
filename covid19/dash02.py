import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

confirmed = pd.read_csv(url_confirmed)
print(confirmed.index)
print(confirmed.columns)
print(confirmed.head())
deaths = pd.read_csv(url_deaths)
print(deaths.index)
print(deaths.columns)
print(deaths.head())
recovered = pd.read_csv(url_recovered)
print(recovered.index)
print(recovered.columns)
print(recovered.head())
print(recovered.info())

# 날짜 column 들을  date라는 column에 집어 넣는다.
date1 = confirmed.columns[4:]
date1
total_confirmed = confirmed.melt(\
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],\
    value_vars=date1, var_name='date', value_name='confirmed')
total_confirmed.head()
total_confirmed.tail()
date2 = deaths.columns[4:]
date2
total_deaths = deaths.melt(\
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],\
    value_vars=date2, var_name='date', value_name='death')
total_deaths.head()
total_deaths.tail()
date3 = recovered.columns[4:]
date3
total_recovered = recovered.melt(\
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],\
    value_vars=date3, var_name='date', value_name='recovered')
total_recovered.head()
total_recovered.tail()

# 합치기
covid_data = total_confirmed.merge(\
    right = total_deaths, how = 'left', \
    on = ['Province/State', 'Country/Region', 'date', 'Lat', 'Long'])
covid_data.head()
covid_data.tail()
covid_data = covid_data.merge(\
    right = total_recovered, how = 'left',\
    on = ['Province/State', 'Country/Region', 'date', 'Lat', 'Long'])
covid_data.head()
covid_data.tail()
covid_data['date'] = pd.to_datetime(covid_data['date'])
covid_data['date']

# nan check
covid_data.isna().sum()

# nan 값 0으로 채우기
covid_data['recovered'] = covid_data['recovered'].fillna(0)
covid_data.isna().sum()
# 새 칼럼 생성 - active(코로나 환자) = 확진 -  사망 - 회복
covid_data["active"] = covid_data["confirmed"] \
                     - covid_data["death"] - covid_data["recovered"]
print(covid_data)
## 집계 자료 만들기 - 일자별로 확진자, 사망자. 완치자, 코로나 환자를 집계하여 covid_data_1으로 만든다다
covid_data_1=covid_data.groupby(\
    ["date"])[["confirmed","death","recovered","active"]].sum().reset_index()
covid_data_1
## Country/Region 별 위도 경도 list 만들기
covid_data.columns
covid_data_list = covid_data[["Country/Region", "Lat", "Long"]]
covid_data_list
##covid_data_list를 Country/Region로 인덱스를 만들고 딕셔너리 타입으로 변환 (.T.) 작업 - 이유:
##unique 하지 않는 다는 내용이 나온다, 그걸 찾는 방법 찾아 보세요
dict_of_locations = covid_data_list.set_index("Country/Region")\
    [["Lat","Long"]].T.to_dict("dict")
print(dict_of_locations)

app = dash.Dash(__name__,\
                meta_tags=[{"name":"Viewport","content":"width=device-width"}])
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url("corona-logo-1.jpg"),
                     id = "corona-image",
                     style={"height":"60px",
                            "width":"auto",
                            "margin-bottom":"25px"})
        ],  className="one-third column"),
    ], id="header", className="row flex-display",\
        style={"margin-bottom":"25px"}),
], id= "mainContainer", \
    style={"display":"flex", "flex-direction":"column"})

if __name__ == "__main__":
    app.run_server(debug=False, port=8080,host="127.0.0.1")