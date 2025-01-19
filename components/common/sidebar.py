import dash_bootstrap_components as dbc
from dash import Dash, html

sidebar = dbc.Nav(
    children=[
        html.Ul(
            children=[
                html.Li(
                    children=[
                        html.Img(
                            src="assets/images/common/home_icon.svg",
                        ),

                        html.A(
                            "HOME",
                            href="/",
                            className="",
                        )
                    ],
                    className="nav__items",
                ),

                html.Li(
                    children=[
                        html.Img(
                            src="assets/images/common/table_icon.svg",
                        ),

                        html.A(
                            "TABLE",
                            href="/analytics-table",
                            className="",
                        )
                    ],
                    className="nav__items",
                ),

                html.Li(
                    children=[
                        html.Img(
                            src="assets/images/common/graph_icon.svg",
                        ),

                        html.A(
                            "GRAPH",
                            href="/analytics-graph",
                            className="",
                        )
                    ],
                    className="nav__items",
                ),
            ],
            className="nav",
        )

    ],
    className="nav__cont",
)
