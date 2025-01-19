import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

from components.common.sidebar import sidebar
from components.common.header import header

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
]

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=external_stylesheets,
)

app.layout = html.Div(
    children=[
        sidebar,
        html.Div(
            children=[
                html.Main(
                    children=[
                        header,
                        dash.page_container,
                    ],
                    className="",
                )
            ],
            className="wrapper main-content",
        )
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
