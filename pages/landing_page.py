import dash
from dash import html
from components.landing.recent_data import recent_data_analytics
from components.landing.nav_cards import nav_pages_cards

dash.register_page(__name__, path="/")

layout = html.Div(
    children=[
        recent_data_analytics,
        nav_pages_cards,
    ],
    className="",
)
