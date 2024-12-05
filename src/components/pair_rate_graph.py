import pandas as pd

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from datetime import datetime, timedelta
from . import ids

def render_eur_base_graph(app, data: pd.DataFrame):
    """
    Renders data and plot lines for EUR Base Rate
    """

    @app.callback(
        Output(ids.SELL_TO_BUY_GRAPH, "figure"),
        [
            Input(ids.SELL_CURRENCY, "value"),
            Input(ids.BUY_CURRENCY, "value"),
            Input(ids.SELL_BUY_TIME_RANGE_TABS, "value")
        ],
    )
    def update_trend_chart(sell_currency:str, buy_currency:str, sell_buy_time_range_tabs:str):
        """
        Now we need to create proper data set just for Selected Sell and Buy Currency
        :param selected_currency: 
        :return: graph
        """
# Viola: Do zmodyfikowania  Filtrowanie danych dla wybranej waluty, creating data set for graph
        sell_data = data[(data['Currency'] == sell_currency)]
        buy_data = data[(data['Currency'] == buy_currency)]

        if sell_data.empty or buy_data.empty:
            # If na data, return message
            return {
                "data": [],
                "layout": {
                    "title": f"Select Sell & Buy Currency to render plot",
                    "xaxis": {"visible": True, "title": "Date"},
                    "yaxis": {"visible": True, "title": "Rate"},
                },
            }
        if sell_currency == buy_currency:
            return {
                "data": [],
                "layout": {
                    "title": f"Selected Sell & Buy Currency are the same",
                    "xaxis": {"visible": True, "title": "Date"},
                    "yaxis": {"visible": True, "title": "Rate"},
                },
            }
        
        # Date Range
        st_date = sell_data["Date"].min()
        end_date = sell_data["Date"].max()
        
        if sell_buy_time_range_tabs == "1W":
            start_date = end_date - timedelta(weeks=1)
            label = "range: 1 week"
        elif sell_buy_time_range_tabs == "1M":
            start_date = end_date - timedelta(days=30)
            label = "range: 1 month"
        elif sell_buy_time_range_tabs == "6M":
            start_date = end_date - timedelta(days=180)
            label = "range: 6 months"
        elif sell_buy_time_range_tabs == "1Y":
            start_date = st_date
            label = "range: Full Range"

        
        # # Create 
        # merged_df[f{sell_currency}/"user_base_rate"] = (
        # (1/merged_df["Rate_input"])/(1/merged_df["Rate_base"]))

    
    
        final_data = sell_data[(data["Date"] >= start_date) & (sell_data["Date"] <= end_date)]

    # Create the figure
        fig = go.Figure()
     # Add Sell Currency (Area under the line with markers)    
        fig.add_trace(go.Scatter(
            x=final_data["Date"],
            y=final_data["Rate"],
            mode="lines+markers",
            name=f"{sell_currency}",
            line=dict(color="rgba(0, 0, 255, 0.3)"),
            # fill="tozeroy",  # Fill area under the line
            # fillcolor="rgba(0, 0, 255, 0.3)",  # Blue color fill with transparency
            marker=dict(size=6, color="darkblue"),  # Darker markers
            ))
        fig.update_layout(
            title= f"{sell_currency}/{buy_currency} FX Rate Trend Plot ({label})",
            xaxis_title="Date",
            yaxis_title=f"{sell_currency}/{buy_currency} Rate",
            template="plotly_white"
        )
        # Dodanie pełnych miesięcy do osi X i dynamicznej osi Y

        return fig

    return dcc.Graph(id=ids.SELL_TO_BUY_GRAPH)


        