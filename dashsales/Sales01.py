import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_table as dt

sales = pd.read_csv("train.csv")
sales
sales["Order Date"] = pd.to_datetime(sales["Order Date"])
sales["Year"] = sales["Order Date"].dt.year
sales["Month"] = sales["Order Date"].dt.month_name()
sales["Order Date"]
sales["Year"]
sales["Month"]


app = dash.Dash(__name__,\
                meta_tags=[{"name":"Viewport","content":"width=device-width"}])

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3("판매 현황", style={"margin-bottom":"0px", "color":"white"})

        ],  className="one-third column", id = "title1"),
        html.Div([
            html.P("년도", className="fix_label", style={"color":"white"}),
            dcc.Slider(id="select_years",
                       included=False,
                       updatemode="drag",
                       tooltip={"always_visible":True},
                       min=2015,
                       max=2018,
                       step=1,
                       value=2018,
                       marks={str(yr): str(yr) for yr in range(2015,2018)},
                       className="dcc_compon"),

        ], className="one-half column", id="title2"),

        html.Div([
            html.P("고객구분", className="fix_label", style={"color":"white"}),
            dcc.RadioItems(id="radio_items",
                       labelStyle={"display": "inline-block"},
                       value="Consumer",
                       options=[{"label": i, "value": i} for i in sales["Segment"].unique()],
                           style={"text-align": "center", "color":"white"},
                       className="dcc_compon"),


        ], className="one-third column", id="title3")

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),
], id="mainContainer", style={"display": "flex", "flex-direction": "column"})

if __name__ == "__main__":
    app.run_server(debug=False)