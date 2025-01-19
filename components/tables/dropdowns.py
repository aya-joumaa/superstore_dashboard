from datetime import date, datetime
from dash import callback, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from data import superstore_data

store_data = superstore_data
unique_ship_modes = sorted(store_data.get("Ship Mode").unique())
unique_segments = sorted(store_data.get("Segment").unique())
unique_states = sorted(store_data.get("State").unique())
unique_cities = sorted(store_data.get("City").unique())

table_dropdowns = html.Section(
    children=[
        html.Div(
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Dropdown(
                                    options=[
                                        {"label": x, "value": x} for x in unique_ship_modes
                                    ],
                                    value="",
                                    placeholder="Select Ship Mode",
                                    id="ship_mode_dropdown",
                                    className="table-dropdowns",
                                ),
                            ],
                            width=3,
                        ),

                        dbc.Col(
                            [
                                dcc.Dropdown(
                                    [
                                        {"label": x, "value": x} for x in unique_segments
                                    ],
                                    value="",
                                    placeholder="Select Segment",
                                    id="segment_dropdown",
                                    className="table-dropdowns",
                                ),
                            ],
                            width=3,
                        ),

                        dbc.Col(
                            [
                                dcc.Dropdown(
                                    [
                                        {"label": x, "value": x} for x in unique_states
                                    ],
                                    value="",
                                    placeholder="Select State",
                                    id="states_dropdown",
                                    className="table-dropdowns",
                                    searchable=True,
                                ),
                            ],
                            width=3,
                        ),
                        dbc.Col(
                            [
                                dcc.Dropdown(
                                    [
                                        {"label": x, "value": x} for x in unique_cities
                                    ],
                                    value="",
                                    placeholder="Select City",
                                    id="cities_dropdown",
                                    className="table-dropdowns",
                                    searchable=True,
                                ),
                            ],
                            width=3,
                        ),
                    ],
                    justify="between",
                    className="mt-3 mb-4",
                ),

                dbc.Row(
                    [
                        dbc.Col(
                            children=[
                                dcc.DatePickerRange(
                                    id="orders_date_filter",
                                    clearable=True,
                                    min_date_allowed=date(2014, 1, 1),
                                    max_date_allowed=date(2017, 12, 31),
                                    initial_visible_month=date(2014, 1, 1),
                                    start_date_placeholder_text="Orders Form Date",
                                    end_date_placeholder_text="Orders To Date",
                                ),
                            ],
                            width=3,
                            className="table-date-filters",
                        ),

                        dbc.Col(
                            children=[
                                dcc.DatePickerRange(
                                    id="ships_date_filter",
                                    clearable=True,
                                    min_date_allowed=date(2014, 1, 1),
                                    max_date_allowed=date(2017, 12, 31),
                                    initial_visible_month=date(2014, 1, 1),
                                    start_date_placeholder_text="Ships Form Date",
                                    end_date_placeholder_text="Ships To Date",
                                ),
                            ],
                            width=3,
                            className="table-date-filters",
                        ),
                    ],
                    justify="left",
                    className="mt-3 mb-4",
                ),
            ],
            className="section-wrapper",
        ),
    ],
    className="table-filters",
)


@callback(
    Output("cities_dropdown", "options"),
    Input("states_dropdown", "value")
)
def set_cities_options(selected_state):
    copy_data = store_data.copy()
    if selected_state:
        copy_data = copy_data[
            copy_data.get("State") == selected_state
            ]
    return [
        {
            "label": x, "value": x
        } for x in sorted(copy_data.get("City").unique())
    ]
