import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import random

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Button("create random number",
                id="button1",
                style={"display":"block", "background-color":"#aabbcc"}),
    html.Label("label",
               id="label1",
               style={"display":"inline-block", "margin":"10"}
               )
])

@app.callback(
    Output(component_id="label1",component_property="children"),
    [Input(component_id="button1", component_property="n_clicks")]
)
def update_output(input_value):
    return random.random()


if __name__ == "__main__":
    app.run_server(debug=False, port=8080, host="127.0.0.1")
