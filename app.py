from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd
from datetime import datetime

df = pd.read_csv("MTA_Ridership_by_DATA_NY_GOV.csv")

# Create a Dash application
app = Dash(__name__)
server = app.server

# App layout
app.layout = html.Div([
    dcc.Dropdown(
        options=[
            {'label': 'Subway %', 'value': 'Subways: % of Comparable Pre-Pandemic Day'},
            {'label': 'Bus %', 'value': 'Buses: % of Comparable Pre-Pandemic Day'}
        ],
        value='Subways: % of Comparable Pre-Pandemic Day',
        clearable=False,
        id='column-selected'
    ),
    dcc.Graph(id='my-graph')
])

# Callback to update the graph
@callback(
    Output('my-graph', 'figure'),
    Input('column-selected', 'value')
)
def update_graph(col_slctd):
    # Convert the "03/11/2020" string to a datetime object
    pandemic_date = datetime.strptime("03/11/2020", "%m/%d/%Y")

    fig = px.bar(df, x="Date", y=col_slctd)
    fig.update_layout(xaxis_title=None)
    fig.update_traces(marker_color="green")
    fig.add_vline(x=pandemic_date, line_width=1, line_dash="dash", line_color="blue")
    fig.add_annotation(
        x=pandemic_date, 
        y=100, 
        text="<--- World Health Organization declares a global COVID-19 pandemic.",
        showarrow=False,
        xshift=220
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')