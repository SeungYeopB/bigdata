import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# 자료 가져오기
terr = pd.read_csv('globalterror.csv')
terr
terr.index
terr.columns
# Create dictionary of list
terr_list = terr[['country_txt', 'latitude', 'longitude']]
terr_list
dict_of_locations = terr_list.set_index('country_txt')[['latitude', 'longitude']].T.to_dict('dict')
dict_of_locations
app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.H3('전 세계 테러 현황', style={'margin-bottom': '0px', 'color': 'white'}),
                html.H5('1970 - 2017', style={'margin-top': '0px', 'color': 'white'})
            ])
        ], className='six column', id = 'title')
    ], id = 'header', className='row flex-display', style={'margin-botttom': '25px'}),
    # map chart 구성
    html.Div([
        html.Div([
            dcc.Graph(id='map_chart', config={'displayModeBar': 'hover'})

        ], className='create_container twelve columns')

    ], className='row flex-display'),
    # 조건 선택 Dropdown box 구성
    html.Div([
        html.Div([
            html.P('대륙 선택', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_countries',
                         multi=False,
                         searchable=True,
                         value='South Asia',
                         placeholder='Select Region',
                         options=[{'label': c, 'value': c}
                                  for c in (terr['region_txt'].unique())], className='dcc_compon'),
            html.P('국가 선택', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_countries1',
                         multi=False,
                         searchable=True,
                         placeholder='Select Country',
                         options=[], className='dcc_compon'),
            html.P('년도 선택', className='fix_label', style={'color': 'white'}),
            dcc.RangeSlider(id='select_years',
                            min=1970,
                            max=2017,
                            dots=False,
                            value=[2010, 2017]),
        ], className='create_container three columns'),
        # 막대 & 선 그레프 그리기
        html.Div([
            dcc.Graph(id='bar_chart', config={'displayModeBar': 'hover'})

        ], className='create_container six columns'),

        # 파이 그래프 그리기
        html.Div([
            dcc.Graph(id='pie_chart', config={'displayModeBar': 'hover'})

        ], className='create_container three columns')

        # 종료 - 두번째 내용 - dropdown, bar& line, pie chart
    ], className='row flex-display')
        # 종료
], id = 'mainContainer', style={'display': 'flex', 'flex-direction': 'column'})
# map chart 구성
@app.callback(Output('map_chart', 'figure'),
              [Input('w_countries','value')],
              [Input('w_countries1','value')],
              [Input('select_years','value')])
def update_graph(w_countries, w_countries1, select_years):
    terr8 = terr.groupby(['region_txt', 'country_txt', 'provstate', 'city', 'iyear', 'latitude', 'longitude']) \
        [['nkill', 'nwound', 'attacktype1']].sum().reset_index()
    terr9 = terr8[(terr8['region_txt'] == w_countries) &
                 (terr8['country_txt'] == w_countries1) &
                 (terr8['iyear'] >= select_years[0]) & (terr8['iyear'] <= select_years[1])]
    if w_countries1:
        zoom=3
        zoom_lat = dict_of_locations[w_countries1]['latitude']
        zoom_long = dict_of_locations[w_countries1]['longitude']
    return {
        'data': [go.Scattermapbox(
            lon=terr9['longitude'],
            lat=terr9['latitude'],
            mode='markers',
            marker=go.scattermapbox.Marker(size=terr9['nwound'],
                                           color=terr9['nwound'],
                                           colorscale='HSV',
                                           showscale=False,
                                           sizemode='area',
                                           opacity=0.3),
            hoverinfo='text',
            hovertext=
            '<b>대륙</b>: ' + terr9['region_txt'].astype(str) + '<br>' +
            '<b>국가</b>: ' + terr9['country_txt'].astype(str) + '<br>' +
            '<b>지역</b>: ' + terr9['provstate'].astype(str) + '<br>' +
            '<b>도시</b>: ' + terr9['city'].astype(str) + '<br>' +
            '<b>년도</b>: ' + terr9['iyear'].astype(str) + '<br>' +
            '<b>사망</b>: ' + [f'{x:,.0f}' for x in terr9['nkill']] + '<br>' +
            '<b>부상</b>: ' + [f'{x:,.0f}' for x in terr9['nwound']] + '<br>' +
            '<b>공격격/b>: ' + [f'{x:,.0f}' for x in terr9['attacktype1']] + '<br>'
        )],

        'layout': go.Layout(
            hovermode='x',
            paper_bgcolor='#010915',
            plot_bgcolor='#010915',
            margin=dict(r=0, l =0, b = 0, t = 0),
            mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',
                center = go.layout.mapbox.Center(lat=zoom_lat, lon=zoom_long),
                style='dark',
                # style='open-street-map',
                zoom=zoom,
            ),
            autosize=True
        )
    }




# dropdown 메뉴 구성
@app.callback(Output('w_countries1', 'options'),
              [Input('w_countries','value')])
def update_country(w_countries):
    terr3 = terr[terr['region_txt'] == w_countries]
    return [{'label': i, 'value': i} for i in terr3['country_txt'].unique()]

@app.callback(Output('w_countries1', 'value'),
              [Input('w_countries1', 'options')])
def update_country(w_countries1):
    return [k['value'] for k in w_countries1][0]
# bar & line chart 그리기
@app.callback(Output('bar_chart', 'figure'),
              [Input('w_countries','value')],
              [Input('w_countries1','value')],
              [Input('select_years','value')])
def update_graph(w_countries, w_countries1, select_years):
    terr5 = terr.groupby(['region_txt', 'country_txt', 'iyear'])[['nkill', 'nwound', 'attacktype1']].sum().reset_index()
    terr6 = terr5[(terr5['region_txt'] == w_countries) &
                 (terr5['country_txt'] == w_countries1) &
                 (terr5['iyear'] >= select_years[0]) & (terr5['iyear'] <= select_years[1])]
    return {
        'data': [go.Scatter( # 선그래프 그리기 - 사망자
            x=terr6['iyear'],
            y=terr6['nkill'],
            mode = 'markers+lines',
            name='사망',
            line=dict(shape = 'spline', smoothing = 1.3, width = 3, color = '#FF00FF'),
            marker=dict(color='white', size = 10, symbol = 'circle',
                        line=dict(color = '#FF00FF', width = 2)),
            hoverinfo='text',
            hovertext=
            '<b>대륙</b>: ' + terr6['region_txt'].astype(str) + '<br>' +
            '<b>나라</b>: ' + terr6['country_txt'].astype(str) + '<br>' +
            '<b>년도</b>: ' + terr6['iyear'].astype(str) + '<br>' +
            '<b>사망</b>: ' + [f'{x:,.0f}' for x in terr6['nkill']] + '<br>'
        ),
            go.Bar(  # 막대 그래프 그리기 - 부상자
                x=terr6['iyear'],
                y=terr6['nwound'],
                text = terr6['nwound'],
                texttemplate='%{text:,.0f}',
                textposition='auto',
                name='부상',
                marker=dict(color='#9C0C38'),
                hoverinfo='text',
                hovertext=
                '<b>대륙</b>: ' + terr6['region_txt'].astype(str) + '<br>' +
                '<b>나라</b>: ' + terr6['country_txt'].astype(str) + '<br>' +
                '<b>년도</b>: ' + terr6['iyear'].astype(str) + '<br>' +
                '<b>부상</b>: ' + [f'{x:,.0f}' for x in terr6['nwound']] + '<br>'
            ),
            go.Bar( # 막대 그래프 그리기 - 공격
                x=terr6['iyear'],
                y=terr6['attacktype1'],
                text=terr6['attacktype1'],
                texttemplate='%{text:,.0f}',
                textposition='auto',
                name='공격',
                marker=dict(color='orange'),
                hoverinfo='text',
                hovertext=
                '<b>대륙</b>: ' + terr6['region_txt'].astype(str) + '<br>' +
                '<b>나라</b>: ' + terr6['country_txt'].astype(str) + '<br>' +
                '<b>년도</b>: ' + terr6['iyear'].astype(str) + '<br>' +
                '<b>공격</b>: ' + [f'{x:,.0f}' for x in terr6['attacktype1']] + '<br>'
            )
        ],
        'layout': go.Layout(
            barmode = 'stack',
            title={'text': '사망, 부상 , 공격 : ' + (w_countries1) + ' ' + '<br>'
                   + ' - ' .join([str(y) for y in select_years]) + '</br>',
                   'y': 0.93,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={'color': 'white',
                       'size': 20},
            font=dict(family='sans-serif',
                      color='white',
                      size=12),
            hovermode='closest',
            paper_bgcolor='#010915',
            plot_bgcolor='#010915',
            legend={'orientation': 'h',
                    'bgcolor': '#010915',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
            margin=dict(r=0),
            xaxis=dict(title='<b>년도</b>',
                       tick0 = 0,
                       dtick = 1,
                       color = 'white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Aerial',
                           color='white',
                           size=12
                       )),
            yaxis=dict(title='<b>사망, 부상, 공격 </b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Aerial',
                           color='white',
                           size=12
                       )
                       )
        )
    }
# 파이 챠트 그리기
@app.callback(Output('pie_chart', 'figure'),
              [Input('w_countries','value')],
              [Input('w_countries1','value')],
              [Input('select_years','value')])
def update_graph(w_countries, w_countries1, select_years):
    terr7 = terr.groupby(['region_txt', 'country_txt', 'iyear'])[['nkill', 'nwound', 'attacktype1']].sum().reset_index()
    death = terr7[(terr7['region_txt'] == w_countries) & # 사망
                  (terr7['country_txt'] == w_countries1) &
                  (terr7['iyear'] >= select_years[0]) & (terr7['iyear'] <= select_years[1])]['nkill'].sum()
    injured = terr7[(terr7['region_txt'] == w_countries) & # 부상
                  (terr7['country_txt'] == w_countries1) &
                  (terr7['iyear'] >= select_years[0]) & (terr7['iyear'] <= select_years[1])]['nwound'].sum()
    attack = terr7[(terr7['region_txt'] == w_countries) & # 공격
                    (terr7['country_txt'] == w_countries1) &
                    (terr7['iyear'] >= select_years[0]) & (terr7['iyear'] <= select_years[1])]['attacktype1'].sum()
    colors = ['#FF00FF', '#9C0C38', 'orange']

    return {
        'data': [go.Pie( # 파이 챠트
            labels=['사망 총계', '부상 총계', '공격 총계'],
            values=[death, injured, attack],
            marker=dict(colors=colors),
            hoverinfo='label+value+percent',
            textinfo='label+value',
            # hole=.7,
            rotation=45,
            # insidetextorientation= 'radial'

        )],

        'layout': go.Layout(
            title={'text': '사망, 부상, 공격: ' + '<br>' + (w_countries1) + '</br>' + ' ' +
                   ' - ' .join([str(y) for y in select_years]) ,
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
            paper_bgcolor='#010915',
            plot_bgcolor='#010915',
            legend={'orientation': 'h',
                    'bgcolor': '#010915',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7}


        )
    }


# 화면에 보여주기
if __name__ == '__main__':
    app.run_server(debug=False)