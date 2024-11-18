import pandas as pd
from dash import Dash, html
from src.components import (
    trend_chart,
    currency_dropdown,
    month_dropdown,
    year_dropdown,
)


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            # html.Div(
            #     className="dropdown-container",
            #     children=[
            #         year_dropdown.render(app, data),
            #         month_dropdown.render(app, data),
            #         currency_dropdown.render(app, data),
            #     ],
            # ),
            html.Div(
                className="dropdown-container",
                children=[
                    currency_dropdown.render(app, data),
                ],
            ),

            trend_chart.render(app, data),
        ],
    )