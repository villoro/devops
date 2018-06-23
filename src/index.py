"""
    Dash app
"""


import dash
import dash_core_components as dcc
import dash_html_components as html


VAUES = ['MTL', 'BCN', 'QUE']

APP = dash.Dash(__name__)
SERVER = APP.server

# TODO: change url
APP.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

APP.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in VAUES],
        value='LA'
    ),
    html.Div(id='display-value')
])


@APP.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    """ Update value selected """
    return 'You have selected "{}"'.format(value)



if __name__ == '__main__':
    APP.run_server(debug=True)
