import dash
from dash import html
import dash_bootstrap_components as dbc

from components.graph.date_filters import date_filters
from components.graph.timeline_graph import timeline_graph
from components.graph.bubble_graph import bubble_graph
from components.graph.bubble_graph_filters import bubble_graph_filters

dash.register_page(__name__)

layout = html.Div(
    children=[
        date_filters,
        html.Section(
            children=[
                html.Div(
                    children=[
                        dbc.Row(
                            children=[
                                timeline_graph,
                                bubble_graph,
                                bubble_graph_filters,
                            ],
                            justify="left",
                        ),
                    ],
                    className="section-wrapper",
                ),
            ],
            className="graphs-section",
        ),
    ],
    className="graph-page-content",
)
