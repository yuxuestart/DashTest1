# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My first Dash App'),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', "gdpPercap"], value = 'lifeExp', id = 'controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    
    dcc.Graph(firgure = {}, id = 'controls-and-graph')
])

# add controls to build the interaction
@callback(
    Output(component_id)
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)