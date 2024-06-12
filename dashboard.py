import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from database import engine

QEURY = "SELECT * FROM humidity_temperature order by svr_dt desc limit 10000"

df_modules = pd.read_sql('SELECT distinct module FROM humidity_temperature', engine)
default_module = df_modules.module.unique()[0] if not df_modules.empty else '--'
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                requests_pathname_prefix='/dashboard/')

app.layout = [
    html.H1(children='Humidity(%) / Temperature(°C)', style={'textAlign':'center'}),
    dcc.Dropdown(df_modules.module.unique(), default_module, id='dropdown-selection'),
    dcc.Graph(id='graph-temperature'),
    dcc.Graph(id='graph-humidity'),
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
]

@callback(
    Output('graph-temperature', 'figure'),
    Input('dropdown-selection', 'value'),
    Input('interval-component', 'n_intervals')
)
def update_temperature_graph(value, n_intervals):
    df = pd.read_sql(QEURY, engine)

    dff = df[df.module==value]
    return px.line(dff, x='svr_dt', y='temperature',
                    title=f'Temperature(°C) for {value}',
                    labels={'svr_dt':'Date Time', 'temperature':'Temperature(°C)'})

@callback(
    Output('graph-humidity', 'figure'),
    Input('dropdown-selection', 'value'),
    Input('interval-component', 'n_intervals')
)
def update_temperature_graph(value, n_intervals):
    df = pd.read_sql(QEURY, engine)

    dff = df[df.module==value]
    return px.line(dff, x='svr_dt', y='humidity',
                    title=f'Humidity(%) for {value}',
                    labels={'svr_dt':'Date Time', 'humidity':'Humidity(%)'})

if __name__ == '__main__':
    app.run(debug=True)