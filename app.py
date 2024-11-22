from dash import Dash, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/MTA_Ridership_by_DATA_NY_GOV.csv")

# Create a dash application
app = Dash(__name__)
server = app.server

app.layout = [
    dcc.Dropdown(options=[{'label':'Subway %', 'value':'Subways: % of Comparable Pre-Pandemic Day'},
                          {'label':'Bus %', 'value': 'Buses: % of Comparable Pre-Pandemic Day'}],
                 value='Subways: % of Comparable Pre-Pandemic Day',
                 clearable=False,
                 id='column-selected'
                 ),
    dcc.Graph(id='my-graph')
]

@callback(
    Output('my-graph','figure'),
    Input('column-selected', 'value')
)
def update_graph(col_slctd):
    fig = px.bar(df, x="Date", y=col_slctd)
    fig.update_layout(xaxis_title=None)
    fig.update_traces(marker_color="green")
    fig.add_vline(x="03/11/2020", line_width=1, line_dash="dash", line_color="blue")
    fig.add_annotation(x="03/11/2020", y=100,
                       text="<--- World Health Organization declares a global COVID-19 pandemic.",
                       showarrow=False,
                       xshift=220)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)