import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from data import superstore_data

store_data = superstore_data


def calculate_latest_year_analytics():
    store_data["Days to Ship"] = (
            store_data["Ship Date"] - store_data["Order Date"]
    ).dt.days

    latest_year = store_data["Order Date"].max().year
    yearly_data = store_data[
        store_data["Order Date"].dt.year == latest_year
        ]

    latest_data = [
        {
            "img_path": "assets/images/landing_page/order_icon.png",
            "title": "Number of New Orders",
            "value": yearly_data["Order ID"].nunique(),
        },

        {
            "img_path": "assets/images/landing_page/sales_icon.png",
            "title": "Accumulated Sales",
            "value": format(float(yearly_data["Sales"].sum()), ".3f")
        },

        {
            "img_path": "assets/images/landing_page/profit_icon.png",
            "title": "Accumulated Profits",
            "value": format(float(yearly_data["Profit"].sum()), ".3f")
        },

        {
            "img_path": "assets/images/landing_page/profit_ratio_icon.png",
            "title": "Profit Ratio",
            "value": format(float((yearly_data["Profit"] / yearly_data["Sales"]).sum()), ".3f")
        },

        {
            "img_path": "assets/images/landing_page/calendar_icon.png",
            "title": "Days Of Ships",
            "value": format(float(yearly_data["Days to Ship"].mean()), ".3f"),
        },

        {
            "img_path": "assets/images/landing_page/person_icon.png",
            "title": "Customers who benefit from the services",
            "value": yearly_data["Customer ID"].nunique(),
        },

        {
            "img_path": "assets/images/landing_page/state_icon.png",
            "title": "Number of states shipped to",
            "value": yearly_data["State"].nunique(),
        },

        {
            "img_path": "assets/images/landing_page/city_icon.png",
            "title": "Number of cities shipped to",
            "value": yearly_data["City"].nunique(),
        },
    ]

    return latest_data
