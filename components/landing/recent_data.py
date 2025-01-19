from dash import html
from helpers.landing import calculate_latest_year_analytics

analytics_data = calculate_latest_year_analytics()

recent_data_analytics = html.Section(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H1(
                                    "LATEST YEAR DATA ANALYTICS",
                                    className="heading",
                                )
                            ],
                            className="analytics-header",
                        ),

                        html.Div(
                            children=[
                                html.Article(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Img(
                                                    src=data.get("img_path"),
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            html.P(
                                                data.get("title"),
                                            ),
                                            className="attribute-name",
                                        ),
                                        html.Div(
                                            html.P(
                                                data.get("value"),
                                            ),
                                            className="attribute-value",
                                        ),
                                    ],
                                    className="analytics-card",
                                ) for data in analytics_data
                            ],
                            className="analytics-cards",
                        ),
                    ],
                    className="analytics-container",
                ),
            ],
            className="section-wrapper",
        ),
    ],
    className="recent-data",
)
