import dash
from dash import html

table_page_url = dash.page_registry.get("pages.analytics_table").get("path")
graph_page_url = dash.page_registry.get("pages.analytics_graph").get("path")

nav_pages_cards = html.Section(
    children=[
        html.Div(
            children=[
                html.H1(
                    "ANALYTICS DETAILS",
                    className="heading",
                ),

                html.Div(
                    children=[
                        html.Article(
                            children=[
                                html.A(
                                    children=[
                                        html.H2(
                                            "Table Analytics",
                                            className="page-card__heading",
                                        ),
                                    ],
                                    href=table_page_url,
                                ),
                            ],
                            className="page-card",
                        ),
                        html.Article(
                            children=[
                                html.A(
                                    children=[
                                        html.H2(
                                            "Graph Analytics",
                                            className="page-card__heading",
                                        ),
                                    ],
                                    href=graph_page_url,
                                ),
                            ],
                            className="page-card",
                        ),
                    ],
                    className="pages-cards",
                ),
            ],
            className="section-wrapper",
        ),
    ],
    className="pages-nav",
)
