import pandas as pd
from dash import Dash, html, dcc
from . import ids
from src.components import (
    sell_currency_dropdown,
    buy_currency_dropdown,
    eur_graph,
    pair_rate_graph
    )

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
                # Input windows - Amount to convert
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
                        # display_format="DD.MM.YYYY ..Viola :) przenies to do daneych bo tu nnie dziala",
                        placeholder="Select a date..."
                    )
                ], className="dropdown-item"),
            ], className="left-container"),  # Lewa kolumna
            # Right Container to display Currency Calcular Result and info to User
            html.Div([
                html.Div([
                    html.H5("Currency Conversion Results", className="title-raight-container"),
                ], className="title-raight-container"),
                    html.Button("Convert", id="convert_button", n_clicks=0, style={"marginRight": "500px"}),
                html.Div([
                    html.Div(id=ids.CONVERSTION_RESULT, className="result", style={"marginTop": "20px"}),
                    html.H6("Converstion Results and trend analysis commentaries, (Placeholder)", className="placeholder-title"),  # Tytuł kontenera
                    html.Div([], className="right-content")
                ], className="right-inside-container"),  # Obszar na przyszłe komponenty
            ], className="right-container"), 

        ], className="main-container"),  # Sekcja na dropdowny
        html.Hr(className="custom-hr"),
        # GRAPH section
        html.Div([
            html.Div([
                html.H3("EUR Rate Trend Plot for Selected Buy and Sell Currency", style={"text-align": "center", "font-size": "18px", "color": "#3a5486"}),  # Graph_1 title
                dcc.Tabs(id="time_range_tabs", value="1W", children=[
                    # dcc.Tab(label="1D", value="1D"),
                    dcc.Tab(label="1W", value="1W"),
                    dcc.Tab(label="1M", value="1M"),
                    dcc.Tab(label="6M", value="6M"),
                    dcc.Tab(label="1Y", value="1Y"),
                ], className="tabs-container"),
                eur_graph.render_eur_base_graph(app, data)
              
            ], style={"flex": "1", "padding": "5px"}),  # Dodajemy padding, aby przestrzeń wokół wykresu była estetyczna
            html.Div([
                html.H3("Sell to Buy Currency FX Rate Trend", style={"color": "#3a5486", "text-align": "center", "font-size": "18px"}),
                dcc.Tabs(id=ids.SELL_BUY_TIME_RANGE_TABS, value="1W", children=[
                    # dcc.Tab(label="1D", value="1D"),
                    dcc.Tab(label="1W", value="1W"),
                    dcc.Tab(label="1M", value="1M"),
                    dcc.Tab(label="6M", value="6M"),
                    dcc.Tab(label="1Y", value="1Y"),
                ], className="tabs-container"),
                pair_rate_graph.render_eur_base_graph(app, data),
                # dcc.Graph(
                #     id="sell-to-Buy-graph",
                #     style={"width": "100%"}
                # ),
            ], style={"flex": "1", "padding": "5px"}),  # Padding dla wykresu 2
        ], className="graph-container"),  # Kontener na wykresy
        html.Hr(className="custom-hr"),
    ], className="app-div")  # Padding dla całego layoutu
