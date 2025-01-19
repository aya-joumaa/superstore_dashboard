from dash import callback, dcc, html, Input, Output
import dash_bootstrap_components as dbc

main_axis_options = [
    "Ship Date", "Discount", "Profit",
    "Profit Ratio", "Quantity", "Returned",
    "Sales",
]

bubble_graph_filters = dbc.Col(
    [
        html.Div(
            children=[
                dcc.Dropdown(
                    main_axis_options,
                    placeholder="X-Axis", value="", id="x_axis_drop",
                    searchable=True,
                ),
                html.Br(),
                dcc.Dropdown(
                    main_axis_options,
                    placeholder="Y-Axis", value="", id="y_axis_drop",
                ),
                html.Br(),
                dcc.Dropdown(
                    [
                        "Segment", "Ship Mode", "Customer Name",
                        "Category", "Sub-Category", "Product Name",
                    ],
                    searchable=True,
                    placeholder="Categorize By", value="", id="category_drop",
                ),
            ],
        ),
    ],
    width=2,
)


@callback(
    Output("y_axis_drop", "options"),
    Input("x_axis_drop", "value"),
)
def update_y_axis_drop(x_axis_val):
    options = main_axis_options

    if x_axis_val:
        options = [option for option in options if option != x_axis_val]

    return options


@callback(
    Output("x_axis_drop", "options"),
    Input("y_axis_drop", "value"),
)
def update_x_axis_drop(y_axis_val):
    options = main_axis_options

    if y_axis_val:
        options = [option for option in options if option != y_axis_val]

    return options
