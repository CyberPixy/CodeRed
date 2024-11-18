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
            html.P("Select currency or currencies to display on the plot:"),
            # html.Div(
            #     className="dropdown-cont1",
            #     children=[
            #         year_dropdown.render(app, data),
            #         month_dropdown.render(app, data),
                    
            #     ],
            #     ),
            html.Div(
                className="dropdown-container",
                children=[
                    currency_dropdown.render(app, data),
                ],
            ),
            html.Div(
                        className="chart-container",
                        children=[
                            trend_chart.render(app, data),
                        ],
                    ),
                ],
            )