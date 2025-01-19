import math
from dash import callback, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px

from data import superstore_data
from helpers.graph import prepare_the_bubbles_size_and_texts

store_data = superstore_data
store_data["Profit Ratio"] = store_data["Profit"] / store_data["Sales"]

bubble_graph = dbc.Col(
    [
        dcc.Graph(
            id="bubble_graph",
            figure={},
            clickData=None,
            hoverData=None,
            config={
                "staticPlot": False,
                "scrollZoom": True,
                "doubleClick": "reset",
                "doubleClickDelay": 1,
                "displayModeBar": True,
            },
        ),
    ],
    width=5,
)


# ---------------------------------------------------------------------------------------------------------------------
# This Section Is Allocated For Change the Bubble Graph Values When X-aix and Y-aix Filters are Changed
# And Categorize Graph Values when Attribute Filter is Changed
# ---------------------------------------------------------------------------------------------------------------------


@callback(
    Output("bubble_graph", "figure"),
    Input("x_axis_drop", "value"),
    Input("y_axis_drop", "value"),
    Input("category_drop", "value"),
)
def update_bubble_graph_values(x_axis_val, y_axis_val, category_val):
    fig = {}

    if x_axis_val and y_axis_val:
        fig = px.scatter(
            data_frame=store_data,
            x=x_axis_val,
            y=y_axis_val,
        )

    if category_val and x_axis_val and y_axis_val:
        store_data["text"] = prepare_the_bubbles_size_and_texts(
            store_data, x_axis_val, y_axis_val,
        )

        fig = go.Figure()
        category_values = sorted(store_data.get(category_val).unique())
        categorized_data = {
            category: store_data[store_data[category_val] == category]
            for category in category_values
        }

        for category_name, category in categorized_data.items():
            fig.add_trace(
                go.Scatter(
                    x=category[x_axis_val], y=category[y_axis_val],
                    name=category_name, text=category["text"],
                )
            )

        fig.update_traces(mode="markers", marker=dict(line_width=2))
        fig.update_layout(
            xaxis=dict(
                title=x_axis_val,
            ),
            yaxis=dict(
                title=y_axis_val,
            ),
        )

    return fig
