from dash import html

header = html.Div(
    children=[
        html.Img(
            src="assets/images/common/store.svg",
            className="header-emoji",
        ),
        html.H1(
            children="Superstore Dashboard",
            className="header-title",
        ),
        html.P(
            children=(
                "ANALYZE THE PROFITS, SALES, and LOSSES FOR "
                "OUR STORE IN THE US BETWEEN 2014 AND 2017"
            ),
            className="header-description",
        ),
    ],
    className="header",
)
