import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids


def render(app:Dash, data)-> html.Div:
    '''User interface creator that will create currency dropdown lists for user to select currency pair:
    to sell and buy and pass them via placeholder for further use'''
    render
    unique_currencies = data["Currency"].unique().tolist()
    return html.Div(
        children=[
            html.H6("Select Currency to Sell"),
            dcc.Dropdown(
                id=ids.SELL_CURRENCY_DROPDOWN,
                options=[{"label": currency, "value": currency} for currency in unique_currencies],
                value=unique_currencies[0],
                multi=False,
                placeholder="Select a currency.."
            ),
        ]
    )
