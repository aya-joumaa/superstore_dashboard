import dash
from dash import html
from components.tables.dropdowns import table_dropdowns
from components.tables.table import table_component
from components.tables.add_rows_form import add_rows_form

dash.register_page(__name__)

layout = html.Div(
    children=[
        table_dropdowns,
        table_component,
        add_rows_form,
    ],
    className="",
)
