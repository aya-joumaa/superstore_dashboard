from dash import callback, dcc, html, Input, Output, State
from dash import Dash, dash_table
from data import superstore_data

store_data = superstore_data

table_component = html.Section(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        dash_table.DataTable(
                            id="analytics_table",
                            data=store_data.to_dict("records"),
                            columns=[{"name": i, "id": i} for i in store_data.columns],
                            filter_action="native",
                            sort_action="native",
                            sort_mode="multi",
                            column_selectable="single",
                            selected_columns=[],
                            selected_rows=[],
                            page_current=0,
                            page_size=10,
                            style_data_conditional=[],
                            style_cell={
                                "textAlign": "left"
                            },
                            style_cell_conditional=(
                                    [
                                        {
                                            "if": {"column_id": "Product Name"},
                                            "minWidth": "100%", "width": "100%", "maxWidth": "100%",
                                        },
                                    ] +
                                    [
                                        {
                                            "if": {"column_id": c},
                                            "textAlign": "right"
                                        } for c in ["Postal Code", "Sales", "Quantity", "Discount", "Profit", ]
                                    ]
                            ),
                        ),
                    ],
                    className="analytics-table",
                ),
            ],
            className="section-wrapper",
        ),
    ],
    className="analytics-table-section"
)


@callback(
    Output("analytics_table", "data"),
    Input("ship_mode_dropdown", "value"),
    Input("segment_dropdown", "value"),
    Input("orders_date_filter", "start_date"),
    Input("orders_date_filter", "end_date"),
    Input("ships_date_filter", "start_date"),
    Input("ships_date_filter", "end_date"),
    Input("states_dropdown", "value"),
    Input("cities_dropdown", "value"),
    prevent_initial_call=True,
)
def update_table_dats(
        ship_mode_value, segment_value, orders_start_date,
        orders_end_date, ships_start_date, ships_end_date,
        selected_state, selected_city,
):
    dff = store_data.copy()

    if ship_mode_value:
        dff = dff[dff.get("Ship Mode").eq(ship_mode_value)]
    if segment_value:
        dff = dff[dff.get("Segment").eq(segment_value)]

    if orders_start_date:
        dff = dff[dff.get("Order Date") >= orders_start_date]
    if orders_end_date:
        dff = dff[dff.get("Order Date") <= orders_end_date]

    if ships_start_date:
        dff = dff[dff.get("Ship Date") >= ships_start_date]
    if ships_end_date:
        dff = dff[dff.get("Ship Date") <= ships_end_date]

    if selected_state:
        dff = dff[dff.get("State").eq(selected_state)]
    if selected_city:
        dff = dff[dff.get("City").eq(selected_city)]

    return dff.to_dict("records")
