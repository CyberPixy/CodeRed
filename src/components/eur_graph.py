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
        Output(ids.EUR_GRAPH_1, "figure"),
        [
            Input(ids.SELL_CURRENCY, "value"),
            Input(ids.BUY_CURRENCY, "value"),
            Input(ids.TIME_RANGE_TABS, "value")
        ],
    )
    def update_trend_chart(sell_currency:str, buy_currency:str, time_range_tabs:str):
    # def update_trend_chart(sell_currency:str, buy_currency:str):
        """
        Now we need to create proper data set just for Selected Sell and Buy Currency
        :param selected_currency: 
        :return: graph
        """
# Viola: Do zmodyfikowania  Filtrowanie danych dla wybranej waluty, creating data set for graph
        selected_data = data[(data['Currency'] == sell_currency)]
        buy_data = data[(data['Currency'] == buy_currency)]

        if selected_data.empty or buy_data.empty:
            # If na data, return message
            return {
                "data": [],
                "layout": {
                    "title": f"Select Sell & Buy Currency to render plot",
                    "xaxis": {"visible": True, "title": "Date"},
                    "yaxis": {"visible": True, "title": "Rate"},
                },
            }
        
        # Date Range
        st_date = selected_data["Date"].min()
        end_date = selected_data["Date"].max()
       
        if time_range_tabs == "1W":
            start_date = end_date - timedelta(weeks=1)
            label = "range: 1 week"
        elif time_range_tabs == "1M":
            start_date = end_date - timedelta(days=30)
            label = "range: 1 month"
        elif time_range_tabs == "6M":
            start_date = end_date - timedelta(days=180)
            label = "range: 6 months"
        elif time_range_tabs == "1Y":
            start_date = st_date
            label = "range: Full Range"
        # else:
        #     start_date = selected_data["Date"].min()
        #     label = "Full Range"

        filtered_data = selected_data[(data["Date"] >= start_date) & (selected_data["Date"] <= end_date)]
        filtered_buy = buy_data[(data["Date"] >= start_date) & (buy_data["Date"] <= end_date)]# Tworzenie listy wszystkich miesięcy dla osi X

    # Create the figure
        fig = go.Figure()
     # Add Sell Currency (Area under the line with markers)    
        fig.add_trace(go.Scatter(
           x=filtered_data["Date"],
            y=filtered_data["Rate"],
            mode="lines+markers",
            name=f"Sell:{sell_currency}",
            line=dict(color="rgba(0, 0, 255, 0.3)"),
            # fill="tozeroy",  # Fill area under the line
            # fillcolor="rgba(0, 0, 255, 0.3)",  # Blue color fill with transparency
            marker=dict(size=6, color="darkblue"),  # Darker markers
            ))
        fig.add_trace(go.Scatter(
            x=filtered_buy["Date"],
            y=filtered_buy["Rate"],  # Assuming "Buy_Rate" column exists
            mode="lines+markers",
            name=f"Buy:{buy_currency}",
            line=dict(color="orange"),  # Orange Color
             marker=dict(size=6, color="darkorange"),
        ))
        fig.update_layout(
            title= f"EUR FX <span style='color: blue'>Sell:{sell_currency}</span> and <span style='color: orange'>Buy:{buy_currency}</span> ({label})",
            xaxis_title="Date",
            yaxis_title=f"FX Rate",
            template="plotly_white"
        )
        # Dodanie pełnych miesięcy do osi X i dynamicznej osi Y

        return fig

    return dcc.Graph(id=ids.EUR_GRAPH_1)


        