from datetime import date, datetime
from dash import callback, dcc, html, Input, Output, State
from data import superstore_data

store_data = superstore_data
unique_cities = sorted(store_data.get("City").unique())

add_rows_form = html.Section(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H1(
                            "ADD NEW ORDER TO THE TABLE",
                            className="heading",
                        )
                    ],
                    className="analytics-header",
                ),

                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dcc.Input(
                                    id="order_id",
                                    type="text",
                                    value="",
                                    placeholder="Order ID",
                                    className="form-input",
                                ),

                                dcc.DatePickerSingle(
                                    id="order_date",
                                    clearable=True,
                                    date=None,
                                    placeholder="Order Date",
                                    min_date_allowed=date(2014, 1, 1),
                                    max_date_allowed=date(2030, 1, 1),
                                    initial_visible_month=date(2014, 1, 1),
                                ),

                                dcc.Input(
                                    id="customer_id",
                                    type="text",
                                    value="",
                                    placeholder="Customer ID",
                                    className="form-input",
                                ),

                                dcc.Dropdown(
                                    options=[
                                        {"label": x, "value": x} for x in unique_cities
                                    ],
                                    id="city",
                                    value="",
                                    placeholder="City",
                                    searchable=True,
                                ),

                                dcc.Input(
                                    id="product_id",
                                    type="text",
                                    value="",
                                    placeholder="Product ID",
                                    className="form-input",
                                ),

                                html.Div(
                                    children=[
                                        html.Button(
                                            "ADD DATA",
                                            id="add_order_data",
                                            n_clicks=0,
                                            className="add-row-btn"
                                        ),
                                    ],
                                    className="add-row-div",
                                ),
                            ],
                            className="form-group",
                        ),
                    ],
                    className="add-row-form"
                ),
            ],
            className="section-wrapper"
        )
    ],
    className="add-row-form-section",
)


@callback(
    Output("analytics_table", "data", allow_duplicate=True),
    Input("add_order_data", "n_clicks"),
    State("analytics_table", "data"),
    State("order_id", "value"),
    State("order_date", "date"),
    State("customer_id", "value"),
    State("city", "value"),
    State("product_id", "value"),
    prevent_initial_call=True,
)
def add_data_to_table(
        n_clicks, table_data, order_id_val,
        order_date_val, customer_id_val, city_val,
        product_id_val
):
    dict = {
        "Row ID": len(table_data) + 1,
        "Order ID": order_id_val,
        "Order Date": order_date_val,
        "Customer ID": customer_id_val,
        "Country": "United States",
        "City": city_val,
        "Product ID": product_id_val,
    }

    orders_info = [
        (row["Order ID"], row["Product ID"]) for row in table_data
    ]

    if n_clicks > 0:
        if (order_id_val, product_id_val) not in orders_info:
            table_data.append(dict)

    return table_data


@callback(
    Output("analytics_table", "page_current"),
    Output("analytics_table", "style_data_conditional"),
    Input("add_order_data", "n_clicks"),
    State("analytics_table", "page_current"),
    State("analytics_table", "data"),
    State("analytics_table", "style_data_conditional"),
)
def update_pagination(n_clicks, current_page, data, style_data_conditional):
    if n_clicks > 0:
        page_size = 10
        total_rows = len(data)
        last_page_index = total_rows // page_size

        new_row_index = len(data) + 1
        style_data_conditional.extend(
            [
                {
                    "if": {
                        "filter_query": "{Row ID} = " + str(new_row_index),
                    },
                    "backgroundColor": "#96d5a4",
                },

            ]

        )
        return last_page_index, style_data_conditional

    return current_page, style_data_conditional
