import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import base64

# Create a sample dataset
df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5]})

# Read an image file and encode it as a base64 string
with open(r"C:\Users\user\PycharmProjects\pythonProject\image.png.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

# Initialize the Dash app
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div([
    html.Div(
        dcc.Graph(
            id='scatterplot',
            figure={
                'data': [px.scatter(df, x='x', y='y')],
                'layout': {
                    'images': [dict(
                        source=encoded_string,
                        xref="paper", yref="paper",
                        x=1, y=1,
                        sizex=1, sizey=1,
                        sizing="stretch",
                        opacity=0.5,
                        layer="below")],
                     'title': 'Scatterplot with Image Overlay',
                'xaxis': {'range': [0, 6]},
                'yaxis': {'range': [0, 6]}
                }
            }
        ),
        style={'display': 'inline-block', 'width': '50%'}
    ),
    html.Div(
        html.Img(
            src='data:image/png;base64,{}'.format(encoded_string),
            style={'height': '500px'}
        ),
        style={'display': 'inline-block', 'width': '50%'}
    )
])

#test comment
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)