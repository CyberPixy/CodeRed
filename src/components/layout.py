import pandas as pd
from dash import Dash, html, dcc
from . import ids
from src.components import sell_currency_dropdown, buy_currency_dropdown

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    """
    Tworzy layout dla aplikacji Dash z podziałem na kolumny i miejsce na wykresy.

    Args:
        app (dash.Dash): Instancja aplikacji Dash.
        data (pd.DataFrame): Dane FX rate

    Returns:
        html.Div: Layout aplikacji.
    """
    return html.Div([
        # Header
        html.Div([
            html.H1(app.title, className="title"),  # Tytuł aplikacji
            html.Hr(className="custom-hr")         # Pozioma linia
        ], className="header-container"),

        # Ddropdowny (1/3 strony  split by half )
        html.Div([
            # Left column with 4 Dropdowns to User Select parameters for Calculation  
            html.Div([
                html.H5("Select All Parameters", className="subtitle"),
                html.Div([
                    html.H6("Sell Currency"),
                    dcc.Dropdown(
                        id=ids.SELL_CURRENCY,
                        options=[{"label": currency, "value": currency} for currency in data["Currency"].unique()],
                        placeholder="Select selling currency(e.g. , USD)."
                    )
                ], className="dropdown-item"),
                html.Div([
                    html.H6("Buy Currency"),
                    dcc.Dropdown(
                        id=ids.BUY_CURRENCY,
                        options=[{"label": currency, "value": currency} for currency in data["Currency"].unique()],
                        placeholder="Select a currency to buy..."
                    )
                ], className="dropdown-item"),
                # Input windows - Amount to conver
                html.Div([
                    html.H6("Amount to Sell:"),
                    dcc.Input(
                        id=ids.AMOUNT_TO_SELL,
                        type="number", 
                        step=0.01,
                        value='', 
                        placeholder="Type amount to Sell"
                    )
                ], className="dcc-input-container",),
                # Date selector 
                html.Div([
                    html.H6("Select Date"),
                    dcc.Dropdown(
                        id= ids.SELECT_DATE, 
                        options=[{"label": date, "value": date} for date in data["Date"].unique()],
                        placeholder="Select a date..."
                    )
                ], className="dropdown-item"),
            ], className="left-container"),  # Lewa kolumna


            # Right Container to display Currency Calcular Result and info to User
            html.Div([
                html.Div([
                    html.H5("Currency Conversion Results", className="title-raight-container"),
                ], className="title-raight-container"),
                html.Div([
                    html.H6("Right Container Placeholder", className="placeholder-title"),  # Tytuł kontenera
                    html.Div([], className="right-content")
                ], className="right-inside-container"),  # Obszar na przyszłe komponenty
            ], className="right-container"), 
                

        ], className="main-container"),  # Sekcja na dropdowny

        # Sekcja na wykresy
        html.Div([
            dcc.Graph(
                id="example-graph-1",
                style={"width": "48%", "display": "inline-block"}
            ),
            dcc.Graph(
                id="example-graph-2",
                style={"width": "48%", "display": "inline-block", "marginLeft": "4%"}
            )
        ], className="graph-container")  # Kontener na wykresy
    ], className="app-div")  # Padding dla całego layoutu

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        
        # html.Hr(),

            # # Graph for selected currencies trend
            # dcc.Graph(id=ids.SELECTED_CURRENCIES_TREND_CHART),
            # # Summary section
            # html.Div(id=ids.FX_RATE_SUMMARY, className="summary-container"),
    #     ],
    #     className="app-div"
    # )
                # className="dropdown-item"),

                    # Tabs for time range selection
            # html.Div(
            #     children=[
            #         dcc.Tabs(
            #             id=ids.TIME_RANGE_TABS,
            #             value="1D",
            #             children=[
            #                 dcc.Tab(label="1 Day", value="1D"),
            #                 dcc.Tab(label="1 Week", value="1W"),
            #                 dcc.Tab(label="1 Month", value="1M"),
            #                 dcc.Tab(label="6 Months", value="6M"),
            #                 dcc.Tab(label="1 Year", value="1Y"),
            #             ],
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
#     """
#     Creates the layout for the Dash app, with split for 

#     :param app: Dash application instance.
#     :param data: DataFrame containing the currency fx data.
#     :return: A Dash HTML Div element representing the layout with its children
#     """
#     return html.Div([
#         html.Div([
#             html.H1(app.title, className="title"),
#             html.Hr(className="custom-hr"),
#              # Dropdown containers for currency selection
#             html.Div([
#                 html.Div([
#                     html.H6("Select Sell Currency"),
#                     dcc.Dropdown(
#                     id='sell_currency',
#                     options=[{"label": currency, "value": currency} for currency in data["Currency"].unique()],
#                     placeholder="Select a currency to sell..."
#                     )
#                     ],
#                     className="dropdown-item"),
#                     html.Div([
#                     html.H6("Select to Buy"),
#                     dcc.Dropdown(
#                     id='buy_currency',
#                     options=[{"label": currency, "value": currency} for currency in data["Currency"].unique()],
#                     placeholder="Select a currency to buy..."
#                     )
#                     ],
#                     className="dropdown-item"),
#                 ],
#                 className="dropdown-container"),
#             ],
#             className="app-div"),
#         ],)