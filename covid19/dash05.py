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
#print(covid_data)
print("=================================data 정리 ok========================")
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

        html.Div([
            html.Div([
                html.H3("코로나 - 19", style={"margin-bottom":"0px","color":"white"}),
                html.H5("코로나 - 19 추적현황", style={"margin-bottom":"0px","color":"white"})
            ])
        ], className="one-half column", id="title"),

        html.Div([
            html.H6("Last Updated: " + str(covid_data["date"].iloc[-1].strftime("%B %d, %Y")) + " 00:01 (UTC)",
                    style={"color":"orange"})

        ], className="one-third column", id="title1")

    ], id="header", className="row flex-display",\
        style={"margin-bottom":"25px"}),

    html.Div([
        html.Div([
            html.H6(children="Global Cases",
                    style={"textAlign":"center",
                       "color":"white"}),
            html.P(f"{covid_data_1['death'].iloc[-1]:,.0f}",
                    style={"textAlign":"center",
                      "color":"orange",
                      "fontSize":40}),
            html.P("new:" + f"{covid_data_1['confirmed'].iloc[-1] - covid_data_1['confirmed'].iloc[-2]:,.0f}"
                    + "(" + str(round(((covid_data_1['confirmed'].iloc[-1] - covid_data_1['confirmed'].iloc[-2])/
                                        covid_data_1['confirmed'].iloc[-1]) * 100, 2)) + "%)",
                    style={"textAlign":"center",
                      "color":"orange",
                      "fontSize":15,
                      "margin-top":"-18px"})
        ], className="card_container three columns"),

        html.Div([
            html.H6(children="Global Deaths",
                    style={"textAlign":"center",
                           "color":"white"}),
            html.P(f"{covid_data_1['death'].iloc[-1]:,.0f}",
                    style={"textAlign":"center",
                           "color":"#dd1e35",
                           "fontSize":40}),
            html.P("new:" + f"{covid_data_1['death'].iloc[-1] - covid_data_1['death'].iloc[-2]:,.0f}"
                    + "(" + str(round(((covid_data_1['death'].iloc[-1] - covid_data_1['death'].iloc[-2])/
                                        covid_data_1['death'].iloc[-1]) * 100, 2)) + "%)",
                    style={"textAlign":"center",
                      "color":"#dd1e35",
                      "fontSize":15,
                      "margin-top":"-18px"})

        ], className="card_container three columns"),

    html.Div([
            html.H6(children="Global Recovered",
                    style={"textAlign":"center",
                           "color":"white"}),
            html.P(f"{covid_data_1['recovered'].iloc[-1]:,.0f}",
                    style={"textAlign":"center",
                           "color":"green",
                           "fontSize":40}),
            html.P("new:" + f"{covid_data_1['recovered'].iloc[-1] - covid_data_1['recovered'].iloc[-2]:,.0f}"
                    + "(" + str(round(((covid_data_1['recovered'].iloc[-1] - covid_data_1['recovered'].iloc[-2])/
                                        covid_data_1['recovered'].iloc[-1]) * 100, 2)) + "%)",
                    style={"textAlign":"center",
                      "color":"green",
                      "fontSize":15,
                      "margin-top":"-18px"})

        ], className="card_container three columns"),

    html.Div([
            html.H6(children="Global Active",
                    style={"textAlign":"center",
                           "color":"white"}),
            html.P(f"{covid_data_1['active'].iloc[-1]:,.0f}",
                    style={"textAlign":"center",
                           "color":"#e55467",
                           "fontSize":40}),
            html.P("new:" + f"{covid_data_1['active'].iloc[-1] - covid_data_1['active'].iloc[-2]:,.0f}"
                    + "(" + str(round(((covid_data_1['active'].iloc[-1] - covid_data_1['active'].iloc[-2])/
                                        covid_data_1['active'].iloc[-1]) * 100, 2)) + "%)",
                    style={"textAlign":"center",
                            "color":"#e55467",
                            "fontSize":15,
                            "margin-top":"-18px"})

        ], className="card_container three columns"),

    ], className="row flex display"),

    html.Div([
        html.Div([
            html.P("Select Country:", className="fix_label", style={"color":"white"}),
            dcc.Dropdown(id="w_countries",
                         multi = False,
                         searchable= True,
                         value="US",
                         placeholder="Select Countries",
                         options=[{"label": c, "value": c}
                                  for c in (covid_data["Country/Region"].unique())], className="dcc_compon"),
            html.P("New Cases:" + " " + str(covid_data["date"].iloc[-1].strftime("%B %d, %Y")),
                   className="fix_label", style={"text-align":"center","color":"white"}),

            dcc.Graph(id="confirmed", config={"displayModeBar":True}, className="dcc_compon",
                      style={"margin-top":"20px"}),
            dcc.Graph(id="death", config={"displayModeBar":False}, className="dcc_compon",
                      style={"margin-top":"20px"}),
            dcc.Graph(id="recovered", config={"displayModeBar":False}, className="dcc_compon",
                      style={"margin-top":"20px"}),
            dcc.Graph(id="active", config={"displayModeBar":False}, className="dcc_compon",
                      style={"margin-top":"20px"}),

        ], className="card_container three columns"),

    ], className="row flex display"),

#], id = "mainContainer")
], id= "mainContainer", \
    style={"display":"flex", "flex-direction":"column"})
@app.callback(Output("confirmed","figure"),
             [Input("w_countries", "value")])
def update_confirmed(w_countries):
    covid_data_2 = covid_data.groupby(["date", "Country/Region"]) \
        [["confirmed", "death", "recovered", "active"]].sum().reset_index()
    value_confirmed = covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["confirmed"].iloc[-1] - covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["confirmed"].iloc[-2]
    delta_confirmed = covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["confirmed"].iloc[-2] - covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["confirmed"].iloc[-3]
    return {
        "data": [go.Indicator(
                mode="number+delta",
                value=value_confirmed,
                delta = {"reference": delta_confirmed,
                        "position": "right",
                        "valueformat": ",g",
                        "relative": False,
                        "font": {"size": 15}},
                number={"valueformat": ",",
                        "font": {"size": 20}},
                domain={"y": [0,1], "x": [0,1]}
        )],
        "layout": go.Layout(
            title={"text": "New Confirmed",
                   "y": 1,
                   "x": 0.5,
                   "xanchor": "center",
                   "yanchor": "top"},
            font=dict(color="orange"),
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            height = 50,
        )
    }
@app.callback(Output("death","figure"),
             [Input("w_countries", "value")])
def update_confirmed(w_countries):
    covid_data_2 = covid_data.groupby(["date", "Country/Region"]) \
        [["confirmed", "death", "recovered", "active"]].sum().reset_index()
    value_death = covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["death"].iloc[-1] - covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["death"].iloc[-2]
    delta_death = covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["death"].iloc[-2] - covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["death"].iloc[-3]
    return {
        "data": [go.Indicator(
                mode="number+delta",
                value=value_death,
                delta = {"reference": delta_death,
                        "position": "right",
                        "valueformat": ",g",
                        "relative": False,
                        "font": {"size": 15}},
                number={"valueformat": ",",
                        "font": {"size": 20}},
                domain={"y": [0,1], "x": [0,1]}
        )],
        "layout": go.Layout(
            title={"text": "New Death",
                   "y": 1,
                   "x": 0.5,
                   "xanchor": "center",
                   "yanchor": "top"},
            font=dict(color="#dd1e35"),
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            height = 50,
        )
    }
@app.callback(Output("recovered","figure"),
             [Input("w_countries", "value")])
def update_confirmed(w_countries):
    covid_data_2 = covid_data.groupby(["date", "Country/Region"]) \
        [["confirmed", "death", "recovered", "active"]].sum().reset_index()
    value_recovered = covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["recovered"].iloc[-1] - covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["recovered"].iloc[-2]
    delta_recovered = covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["recovered"].iloc[-2] - covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["recovered"].iloc[-3]
    return {
        "data": [go.Indicator(
                mode="number+delta",
                value=value_recovered,
                delta = {"reference": delta_recovered,
                        "position": "right",
                        "valueformat": ",g",
                        "relative": False,
                        "font": {"size": 15}},
                number={"valueformat": ",",
                        "font": {"size": 20}},
                domain={"y": [0,1], "x": [0,1]}
        )],
        "layout": go.Layout(
            title={"text": "New Recovered",
                   "y": 1,
                   "x": 0.5,
                   "xanchor": "center",
                   "yanchor": "top"},
            font=dict(color="green"),
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            height = 50,
        )
    }
@app.callback(Output("active","figure"),
             [Input("w_countries", "value")])
def update_confirmed(w_countries):
    covid_data_2 = covid_data.groupby(["date", "Country/Region"]) \
        [["confirmed", "death", "recovered", "active"]].sum().reset_index()
    value_active = covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["active"].iloc[-1] - covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["active"].iloc[-2]
    delta_active = covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["active"].iloc[-2] - covid_data_2[covid_data_2["Country/Region"] \
        == w_countries]["active"].iloc[-3]
    return {
        "data": [go.Indicator(
                mode="number+delta",
                value=value_active,
                delta = {"reference": delta_active,
                        "position": "right",
                        "valueformat": ",g",
                        "relative": False,
                        "font": {"size": 15}},
                number={"valueformat": ",",
                        "font": {"size": 20}},
                domain={"y": [0,1], "x": [0,1]}
        )],
        "layout": go.Layout(
            title={"text": "New Active",
                   "y": 1,
                   "x": 0.5,
                   "xanchor": "center",
                   "yanchor": "top"},
            font=dict(color="orange"),
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            height = 50,
        )
    }


if __name__ == "__main__":
    app.run_server(debug=False, port=8080,host="127.0.0.1")