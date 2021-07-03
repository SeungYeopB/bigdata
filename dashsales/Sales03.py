import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_table as dt

sales = pd.read_csv('train.csv')
sales['Order Date'] = pd.to_datetime(sales['Order Date'])
sales['Year'] = sales['Order Date'].dt.year
sales['Month'] = sales['Order Date'].dt.month_name()
sales['Order Date']
sales['Year']
sales['Month']

sales1 = sales.groupby(['Year', 'Sub-Category', 'Segment'])['Sales'].sum().reset_index()
sales2 = sales1[(sales1['Year'] == 2018) & (sales1['Segment'] == 'Consumer')].sort_values(by = ['Sales'], \
                                                                   ascending = False).nlargest(5, columns = ['Sales'])
sales3 = sales.groupby(['Year', 'Region', 'Segment'])['Sales'].sum().reset_index()
sales4 = sales3[(sales3['Year'] == 2018) & (sales3['Segment'] == 'Consumer')].sort_values(by=['Sales'],ascending=False)


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3('판매현황', style={'margin-bottom': '0px', 'color': 'white'})

        ], className='one-third column', id = 'title1'),

        html.Div([
            html.P('년도', className='fix_label', style={'color': 'white'}),
            dcc.Slider(id='select_years',
                       included=False,
                       updatemode='drag',
                       tooltip={'always_visible': True},
                       min=2015,
                       max=2018,
                       step=1,
                       value=2018,
                       marks={str(yr): str(yr) for yr in range(2015, 2018)},
                       className='dcc_compon'),

        ], className='one-half column', id='title2'),





        html.Div([
            html.P('고객 구분', className='fix_label', style={'color': 'white'}),
            dcc.RadioItems(id='radio_items',
                           labelStyle={'display': 'inline-block'},
                           value='Consumer',
                           options=[{'label': i, 'value': i} for i in sales['Segment'].unique()],
                           style={'text-align': 'center', 'color': 'white'},
                           className='dcc_compon'),

        ], className='one-third column', id='title3'),

    ], id='header', className='row flex-display', style={'margin-bottom': '25px'}),

    # header 종료
    #  2번째단 시작
    #  Horizontal bar chart 작성
    html.Div([
        # 수평 막대 그래프
        html.Div([
            dcc.RadioItems(id='radio_items1',
                           labelStyle={'display': 'inline-block'},
                           value='Sub-Category',
                           options=[{'label': 'Sub-Category', 'value': 'Sub-Category'},
                                    {'label': 'Region', 'value': 'Region'}],
                           style={'text-align': 'center', 'color': 'white'},
                           className='dcc_compon'),

            dcc.Graph(id='bar_chart_1', config={'displayModeBar': 'hover'},
                      style={'height': '350px'}),

        ], className='create_container2 three columns', style={'height': '400px'}),

        # 도넛 챠트
        html.Div([

            dcc.Graph(id='donut_chart', config={'displayModeBar': 'hover'},
                      style={'height': '350px'})

        ], className='create_container2 three columns', style={'height': '400px'}),

        #
    ], className='row flex-display'),
    #  2번째 단 종료






], id = 'mainContainer', style={'display': 'flex', 'flex-direction': 'column'})
@app.callback(Output('bar_chart_1', 'figure'),
              [Input('select_years','value')],
              [Input('radio_items','value')],
              [Input('radio_items1','value')])
def update_graph(select_years, radio_items, radio_items1):
    sales1 = sales.groupby(['Year', 'Sub-Category', 'Segment'])['Sales'].sum().reset_index()
    sales2 = sales1[(sales1['Year'] == select_years) & (sales1['Segment'] == radio_items)].sort_values(by = ['Sales'], \
                                                                       ascending = False).nlargest(5, columns = ['Sales'])
    sales3 = sales.groupby(['Year', 'Region', 'Segment'])['Sales'].sum().reset_index()
    sales4 = sales3[(sales3['Year'] == select_years) & (sales3['Segment'] == radio_items)].sort_values(by=['Sales'],ascending=False)

    if radio_items1 == 'Sub-Category':
     return {
        'data': [
            go.Bar(
                x=sales2['Sales'],
                y=sales2['Sub-Category'],
                text = sales2['Sales'],
                texttemplate= '$' + '%{text:,.2s}',
                textposition='auto',
                orientation= 'h',
                marker=dict(color='#19AAE1'),
                hoverinfo='text',
                hovertext=
                '<b>판매년도</b>: ' + sales2['Year'].astype(str) + '<br>' +
                '<b>고객구분</b>: ' + sales2['Segment'].astype(str) + '<br>' +
                '<b>Sub-Category</b>: ' + sales2['Sub-Category'].astype(str) + '<br>' +
                '<b>판매금액</b>: $' + [f'{x:,.0f}' for x in sales2['Sales']] + '<br>'
            ),
        ],

        'layout': go.Layout(
            title={'text': '카테고리별 판매 in year' + ' ' + str((select_years)),
                   'y': 0.99,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={'color': 'white',
                       'size': 12},
            font=dict(family='sans-serif',
                      color='white',
                      size=15),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation': 'h',
                    'bgcolor': '#010915',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
            margin=dict(t = 40, r=0),
            xaxis=dict(title='<b></b>',
                       color = 'orange',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='orange',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Aerial',
                           color='orange',
                           size=12
                       )),
            yaxis=dict(title='<b></b>',
                       color='orange',
                       autorange = 'reversed',
                       showline=False,
                       showgrid=False,
                       showticklabels=True,
                       linecolor='orange',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Aerial',
                           color='orange',
                           size=12
                       ))
        )
    }
    elif radio_items1 == 'Region':
     return {
        'data': [
            go.Bar(
                x=sales4['Sales'],
                y=sales4['Region'],
                text = sales4['Sales'],
                texttemplate= '$' + '%{text:,.2s}',
                textposition='auto',
                orientation= 'h',
                marker=dict(color='#19AAE1'),
                hoverinfo='text',
                hovertext=
                '<b>판매년도</b>: ' + sales4['Year'].astype(str) + '<br>' +
                '<b>고객구분</b>: ' + sales4['Segment'].astype(str) + '<br>' +
                '<b>지역</b>: ' + sales4['Region'].astype(str) + '<br>' +
                '<b>판매금액</b>: $' + [f'{x:,.0f}' for x in sales4['Sales']] + '<br>'
            ),
        ],
        'layout': go.Layout(
            title={'text': '지역별 판매 in year' + ' ' + str((select_years)),
                   'y': 0.99,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={'color': 'white',
                       'size': 12},
            font=dict(family='sans-serif',
                      color='white',
                      size=15),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation': 'h',
                    'bgcolor': '#010915',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
            margin=dict(t = 40, r=0),
            xaxis=dict(title='<b></b>',
                       color = 'orange',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='orange',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Aerial',
                           color='orange',
                           size=12
                       )),
            yaxis=dict(title='<b></b>',
                       color='orange',
                       autorange = 'reversed',
                       showline=False,
                       showgrid=False,
                       showticklabels=True,
                       linecolor='orange',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Aerial',
                           color='orange',
                           size=12
                       ))
        )
    }
# 도넛 챠트
@app.callback(Output('donut_chart', 'figure'),
              [Input('select_years','value')],
              [Input('radio_items','value')])
def update_graph(select_years, radio_items):
    sales5 = sales.groupby(['Year', 'Category', 'Segment'])['Sales'].sum().reset_index()
    sales_furniture = sales5[(sales5['Year'] == select_years) & (sales5['Segment'] == \
                     radio_items) & (sales5['Category'] == 'Furniture')]['Sales'].sum()
    sales_Office = sales5[(sales5['Year'] == select_years) & (sales5['Segment'] == \
                    radio_items) & (sales5['Category'] == 'Office Supplies')]['Sales'].sum()
    sales_Technology = sales5[(sales5['Year'] == select_years) & (sales5['Segment'] == \
                    radio_items) & (sales5['Category'] == 'Technology')]['Sales'].sum()
    colors = ['#30C9C7', '#7A45D1', 'orange']
    return {
            'data': [go.Pie(
                labels=['가구', '사무 용품', 'IT 용품'],
                values=[sales_furniture, sales_Office, sales_Technology],
                marker=dict(colors=colors),
                hoverinfo='label+value+percent',
                textinfo='label+value',
                texttemplate='%{label} <br>$%{value:,.2f}',
                textposition='auto',
                textfont=dict(size=13),
                hole=.7,
                rotation=160,
                # insidetextorientation= 'radial'
            )],
            'layout': go.Layout(
                title={'text': '카테고리별 판매 in year' + ' ' + str((select_years)),
                       'y': 0.93,
                       'x': 0.5,
                       'xanchor': 'center',
                       'yanchor': 'top'},
                titlefont={'color': 'white',
                           'size': 15},
                font=dict(family='sans-serif',
                          color='white',
                          size=12),
                hovermode='closest',
                paper_bgcolor='#1f2c56',
                plot_bgcolor='#1f2c56',
                legend={'orientation': 'h',
                        'bgcolor': '#1f2c56',
                        'xanchor': 'center', 'x': 0.5, 'y': -0.7}
            )
        }


if __name__ == '__main__':
    app.run_server(debug=False)