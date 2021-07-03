import dash
import dash_html_components as html

app = dash.Dash(__name__)
app.layout = html.H1("Hello dashboard")

if __name__ == "__main__":
    app.run_server(debug=False, port=8080, host="127.0.0.1")
