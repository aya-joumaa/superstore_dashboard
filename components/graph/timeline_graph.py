import math
from dash import callback, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

from data import superstore_data

store_data = superstore_data

timeline_graph = dbc.Col(
    [
        dcc.Graph(
            id="my-graph",
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


@callback(
    Output("my-graph", "figure"),
    Input("years_drop", "value"),
    Input("quarters_drop", "value"),
    Input("months_drop", "value"),
    Input("weeks_drop", "value"),
)
def set_graph_data_value(year, quarter, month, week):
    filtered_data = store_data
    filtered_data["Profit Ratio"] = filtered_data["Profit"] / filtered_data["Sales"]
    filtered_data["Order Week"] = filtered_data["Order Date"].dt.day.apply(lambda x: math.ceil(x / 7))

    grouped_data = store_data.groupby(store_data["Order Date"].dt.year)

    if year:
        filtered_data = filtered_data[filtered_data["Order Date"].dt.year == year]
        grouped_data = filtered_data.groupby(filtered_data["Order Date"].dt.month)

    if quarter:
        filtered_data = filtered_data[
            filtered_data["Order Date"].dt.quarter == quarter
            ]
        grouped_data = filtered_data.groupby(filtered_data["Order Date"].dt.month)

    if month:
        filtered_data = filtered_data[
            filtered_data["Order Date"].dt.month == month
            ]
        grouped_data = filtered_data.groupby(filtered_data["Order Week"])

    if week:
        filtered_data = filtered_data[
            filtered_data["Order Week"] == week
            ]
        grouped_data = filtered_data.groupby(filtered_data["Order Date"].dt.day)

    figure_data = grouped_data.agg({
        "Days to Ship": "mean",
        "Discount": "sum",
        "Profit": "sum",
        "Profit Ratio": "sum",
        "Quantity": "sum",
        "Returned": lambda x: x.eq('Yes').sum(),
        "Sales": "sum",
    }).reset_index()

    figure = px.line(
        data_frame=figure_data,
        x=figure_data.columns[0],
        y=figure_data.columns[1:8],
    )

    return figure
