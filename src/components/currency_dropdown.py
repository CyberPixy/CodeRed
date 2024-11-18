import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_currencies: list[str] = data[DataSchema.CURRENCY].tolist()
    unique_currencies: list[str] = sorted(set(all_currencies))

    @app.callback(
        Output(ids.CURRENCY_DROPDOWN, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_CURRENCIES_BUTTON, "n_clicks"),
        ],
    )
    def select_all_currencies(years: list[str], months: list[str], _: int) -> list[str]:
        # filtered_data = data.query("Year in @years and Month in @months")
        return sorted(set(data.CURRENCY.tolist()))

    return html.Div(
        children=[
            html.H6("Currency"),
            dcc.Dropdown(
                id=ids.CURRENCY_DROPDOWN,
                options=[
                    {"label": currency, "value": currency}
                    for currency in unique_currencies
                ],
                value= unique_currencies,
                multi=True,
                placeholder="Select",
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_CURRENCIES_BUTTON,
                n_clicks=0,
            ),
        ],
    )