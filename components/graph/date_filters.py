from datetime import date, datetime
from dash import callback, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from data import superstore_data

store_data = superstore_data
years = sorted(store_data.get("Order Date").dt.year.unique())

date_filters = html.Section(
    children=[
        html.Div(
            children=[
                dbc.Row(
                    children=[
                        dbc.Col(
                            children=[
                                dcc.Dropdown(
                                    [year for year in years],
                                    value="",
                                    id="years_drop"
                                ),
                            ],
                            width=3,
                        ),

                        dbc.Col(
                            children=[
                                dcc.Dropdown(
                                    [],
                                    value="",
                                    id="quarters_drop"
                                ),
                            ],
                            width=3,
                        ),

                        dbc.Col(
                            children=[
                                dcc.Dropdown(
                                    [],
                                    value="",
                                    id="months_drop"
                                ),
                            ],
                            width=3,
                        ),

                        dbc.Col(
                            children=[
                                dcc.Dropdown(
                                    [],
                                    value="",
                                    id="weeks_drop"
                                ),
                            ],
                            width=3,
                        ),

                    ],
                    justify="between",
                    className="mt-3 mb-4",
                ),
            ],
            className="section-wrapper"
        ),
    ],
    className="filters-section",
)

# --------------------------------------------------------------------------------------------------------------------
# This Section For Prepare Data For the Date Filters
# --------------------------------------------------------------------------------------------------------------------
months_list = {
    1: [
        {"label": "January", "value": 1},
        {"label": "February", "value": 2},
        {"label": "March", "value": 3},
    ],
    2: [
        {"label": "April", "value": 4},
        {"label": "May", "value": 5},
        {"label": "June", "value": 6},
    ],
    3: [
        {"label": "July", "value": 7},
        {"label": "August", "value": 8},
        {"label": "September", "value": 9},
    ],
    4: [
        {"label": "October", "value": 10},
        {"label": "November", "value": 11},
        {"label": "December", "value": 12},
    ],
}


@callback(
    Output("quarters_drop", "options"),
    Output("months_drop", "options", allow_duplicate=True),
    Output("weeks_drop", "options", allow_duplicate=True),

    Output("quarters_drop", "value"),
    Output("months_drop", "value", allow_duplicate=True),
    Output("weeks_drop", "value", allow_duplicate=True),
    Input("years_drop", "value"),
    prevent_initial_call=True,
)
def set_year_quarter_options(selected_year):
    if selected_year:
        quarter_options = [
            {"label": "First Quarter", "value": 1},
            {"label": "Second Quarter", "value": 2},
            {"label": "Third Quarter", "value": 3},
            {"label": "Forth Quarter", "value": 4},
        ]
        return quarter_options, [], [], "", "", ""
    return [], [], [], "", "", ""


@callback(
    Output("months_drop", "options"),
    Output("weeks_drop", "options", allow_duplicate=True),

    Output("months_drop", "value", ),
    Output("weeks_drop", "value", allow_duplicate=True),

    Input("quarters_drop", "value"),
    prevent_initial_call=True,

)
def set_quarter_months_options(selected_quarter):
    if selected_quarter:
        return months_list[selected_quarter], [], "", ""
    return [], [], "", ""


@callback(
    Output("weeks_drop", "options"),
    Output("weeks_drop", "value"),

    Input("months_drop", "value"),
    prevent_initial_call=True,
)
def set_year_weeks_options(selected_months):
    if selected_months:
        weeks_options = [
            {"label": "First Week", "value": 1},
            {"label": "Second Week", "value": 2},
            {"label": "Third Week", "value": 3},
            {"label": "Forth Week", "value": 4},
            {"label": "Fifth Week", "value": 5},
        ]
        return weeks_options, ""
    return [], ""
