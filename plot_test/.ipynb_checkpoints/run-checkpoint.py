import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from funcs import init_csv, update_csv, read_points

import random

# Initialize the Dash app
app = dash.Dash(__name__)
file_name = 'points.csv'
wait = 3 # second of wait -- change to 0.1 when not testing

# Layout of the app
app.layout = html.Div([
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=wait*1000,
        n_intervals=0
    ),
    html.Button('Add Random Point', id='add-point-button', n_clicks=0)
])

# Callback to update the graph
@app.callback(
    Output('live-update-graph', 'figure'),
    [Input('interval-component', 'n_intervals'),
     Input('add-point-button', 'n_clicks')]
)
def update_graph(n_intervals, n_clicks):
    # Add a random point when the button is clicked
    if n_clicks > 0:
        new_point = {
            'x': random.randint(1, 10),
            'y': random.randint(1, 10),
            'z': random.randint(1, 10)
        }
        update_csv(file_name, [new_point])  # Update the CSV file

    # Read points from the CSV for plotting
    points = read_points(file_name)
    x, y, z = zip(*points) if points else ([], [], [])

    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines+markers', name='Points'))
    fig.update_layout(title='-',
                      scene=dict(
                          xaxis_title='X',
                          yaxis_title='Y',
                          zaxis_title='Z'
                      ))
    return fig

if __name__ == '__main__':
    init_csv(file_name)
    app.run_server(debug=True)
    
# use similar code to add new points and it will update properly
new_point = {
            'x': random.randint(1, 10),
            'y': random.randint(1, 10),
            'z': random.randint(1, 10)
        }
update_csv(file_name, [new_point])