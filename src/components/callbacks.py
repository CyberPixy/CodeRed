
# import pandas as pd
# import plotly.graph_objects as go
# from dash import Dash, html, dcc
# from dash.dependencies import Input, Output
# from datetime import datetime, timedelta
# from . import ids

# def update_chart_callbacks(app: Dash, data: pd.DataFrame):

#     @app.callback(
#         [
#             Output(ids.SELECTED_CURRENCIES_TREND_CHART, "figure"),
#             Output(ids.SELECTED_CURRENCIES, "children"),
#             Output(ids.FX_RATE_SUMMARY,"childern")
#         ],
#         [
#             Input(ids.SELL_CURRENCY_DROPDOWN, "value"),
#             Input(ids.BUY_CURRENCY_DROPDOWN, "value"),
#             Input(ids.TIME_RANGE_TABS, "value")
#         ],
#     )
#     def update_chart(sell_currency, buy_currency, time_range_tabs, data=data):
#         if not sell_currency or not buy_currency:
#             return {}, "Please select both currencies."
        
#         # Currencies selected by the User, sourced from placeholder selected-currency_pair aluty wejściowe od użytkownika
#         currency_input = sell_currency  
#         currency_base = buy_currency   
#         # Filtruj dane dla wybranych walut
#         df_input = data[data["Currency"].isin([currency_input ])]
#         df_base = data[data["Currency"].isin([currency_base])]
#         merged_df = pd.merge(
#         df_input,
#         df_base,
#         on=["Date", "Year", "Month"],
#         suffixes=("_input", "_base"),
#         )
#         merged_df[f'{sell_currency}/{buy_currency}'] = ((1/merged_df["Rate_input"])/(1/merged_df["Rate_base"]))

#         if merged_df.empty:
#             return {}, "No data available for the selected currencies."
        
#         # Finalny DataFrame z wybranymi kolumnami
#         enriched_df = merged_df[[
#         "Date",
#         "Currency_input",
#         "Rate_input",
#         "Currency_base",
#         "Rate_base",
#         "Year",
#         "Month",
#         "User_base_rate",
#     ]]
#         #  Renaming columns for clarity
#         enriched_df.columns = [
#         "Date",
#         "Sell_Currency",
#         f'{sell_currency}/EUR',
#         "Buy_Currency",
#         f'{buy_currency}/EUR',
#         "Year",
#         "Month",
#         f'{sell_currency}/{buy_currency}_Rate',
#     ]
#     #     return enriched_df
    
#     # def update_graph(time_range_tabs, sell_cu):
#     # # Defne date ranges
#     #     data_final = update_chart()
#         end_date = enriched_df["Date"].max()
#         if time_range_tabs == "1D":
#             start_date = end_date - timedelta(days=1)
#             label = "1 Day"
#         elif time_range_tabs == "1W":
#             start_date = end_date - timedelta(weeks=1)
#             label = "1 Week"
#         elif time_range_tabs == "1M":
#             start_date = end_date - timedelta(days=30)
#             label = "1 Month"
#         elif time_range_tabs == "6M":
#             start_date = end_date - timedelta(days=180)
#             label = "6 Months"
#         elif time_range_tabs == "1Y":
#             start_date = end_date - timedelta(days=365)
#             label = "1 Year"
#         else:
#             start_date = enriched_df["Date"].min()
#             label = "Full Time Range"

#         filtered_data = enriched_df[(enriched_df["Date"] >= start_date) & (enriched_df["Date"] <= end_date)]
#         initial_rate = filtered_data["f'{sell_currency}/{buy_currency}_Rate'"].iloc[0]
#         final_rate = filtered_data["f'{sell_currency}/{buy_currency}_Rate'"].iloc[-1]
#         percent_change = ((final_rate - initial_rate) / initial_rate) * 100

#         if percent_change > 0:
#             arrow = "▲"
#             color = "green"
#         elif percent_change < 0:
#             arrow = "▼"
#             color = "red"
#         else:
#             arrow = ""
#             color = "black"

#     # Tworzenie wykresu
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(
#         x=filtered_data["Date"],
#         y=filtered_data["f'{sell_currency}/{buy_currency}_Rate'"],
#         mode="lines+markers",
#         name=f'{sell_currency}/{buy_currency}_Rate',
#         line=dict(color="blue"),
#         marker=dict(size=6)
#         ))
#         fig.update_layout(
#         title=f"Kursf'{sell_currency}/{buy_currency} ({label})",
#         xaxis_title="Data",
#         yaxis_title="Kurs f'{sell_currency}/{buy_currency}",
#         template="plotly_white"
#     )
#         summary = html.Div([
#             html.Span(f"Actual FX Rate for ktualna wartość: {final_rate:.6f}", style={"marginRight": "10px"}),
#             html.Span(f"Zmiana procentowa: {percent_change:.2f}% {arrow}", style={"color": color}),
#         ])
#         return fig, summary, f"Displaying rates for {sell_currency} and {buy_currency}."


import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from datetime import datetime, timedelta
from . import ids


def update_chart_callbacks(app: Dash, data: pd.DataFrame):
    @app.callback(
        [
            Output(ids.SELECTED_CURRENCIES_TREND_CHART, "figure"),
            Output(ids.FX_RATE_SUMMARY, "children"),
            Output(ids.SELECTED_CURRENCIES, "children"),
        ],
        [
            Input(ids.SELL_CURRENCY_DROPDOWN, "value"),
            Input(ids.BUY_CURRENCY_DROPDOWN, "value"),
            Input(ids.TIME_RANGE_TABS, "value"),
        ],
    )
    def update_chart(sell_currency, buy_currency, time_range_tabs):
        if not sell_currency or not buy_currency:
            return {}, html.Div("Please select both currencies.", style={"color": "red"}), ""

        # Filter data for selected currencies
        df_input = data[data["Currency"] == sell_currency]
        df_base = data[data["Currency"] == buy_currency]

        merged_df = pd.merge(
            df_input,
            df_base,
            on=["Date", "Year", "Month"],
            suffixes=("_input", "_base"),
        )

        if merged_df.empty:
            return {}, html.Div("No data available for the selected currencies.", style={"color": "red"}), ""

        # Calculate conversion rates
        merged_df[f"{sell_currency}/{buy_currency}"] = merged_df["Rate_input"] / merged_df["Rate_base"]

        # Enrich DataFrame
        enriched_df = merged_df[
            [
                "Date",
                "Currency_input",
                "Rate_input",
                "Currency_base",
                "Rate_base",
                "Year",
                "Month",
                f"{sell_currency}/{buy_currency}",
            ]
        ]
        enriched_df.columns = [
            "Date",
            "Sell_Currency",
            f"{sell_currency}/EUR",
            "Buy_Currency",
            f"{buy_currency}/EUR",
            f"{sell_currency}/{buy_currency}_Rate",
        ]

        # Define date ranges
        end_date = enriched_df["Date"].max()
       
        if time_range_tabs == "1W":
            start_date = end_date - timedelta(weeks=1)
            label = "1 Week"
        elif time_range_tabs == "1M":
            start_date = end_date - timedelta(days=30)
            label = "1 Month"
        elif time_range_tabs == "6M":
            start_date = end_date - timedelta(days=180)
            label = "6 Months"
        elif time_range_tabs == "1Y":
            start_date = end_date - timedelta(days=365)
            label = "1 Year"
        else:
            start_date = enriched_df["Date"].min()
            label = "Full Time Range"

        filtered_data = enriched_df[
            (enriched_df["Date"] >= start_date) & (enriched_df["Date"] <= end_date)
        ]

        if filtered_data.empty:
            return {}, html.Div("No data available for the selected time range.", style={"color": "red"}), ""

        # Calculate initial and final rates
        initial_rate = filtered_data[f"{sell_currency}/{buy_currency}_Rate"].iloc[0]
        final_rate = filtered_data[f"{sell_currency}/{buy_currency}_Rate"].iloc[-1]
        percent_change = ((final_rate - initial_rate) / initial_rate) * 100

        # Determine arrow and color based on percent change
        if percent_change > 0:
            arrow = "▲"
            color = "green"
        elif percent_change < 0:
            arrow = "▼"
            color = "red"
        else:
            arrow = ""
            color = "black"

        # Create the chart
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=filtered_data["Date"],
                y=filtered_data[f"{sell_currency}/{buy_currency}_Rate"],
                mode="lines+markers",
                name=f"{sell_currency}/{buy_currency}_Rate",
                line=dict(color="blue"),
                marker=dict(size=6),
            )
        )
        fig.update_layout(
            title=f"{sell_currency}/{buy_currency} Rate ({label})",
            xaxis_title="Date",
            yaxis_title=f"{sell_currency}/{buy_currency} Rate",
            template="plotly_white",
        )

        # Summary information
        summary = html.Div(
            [
                html.Span(
                    f"Actual FX Rate: {final_rate:.6f}", style={"marginRight": "10px"}
                ),
                html.Span(
                    f"Percentage Change: {percent_change:.2f}% {arrow}",
                    style={"color": color},
                ),
            ]
        )

        return fig, summary, f"Displaying rates for {sell_currency} and {buy_currency}."
