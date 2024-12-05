import pandas as pd

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from . import ids

def render_results_comme(app, data: pd.DataFrame):
    """
    Renders  calculated commantaries 
    """

    @app.callback(
        [Output(ids.SELL_TO_BUY_GRAPH, "figure"),
        Output("fx_rate_summary", "children")]
        
        [Input(ids.SELL_CURRENCY, "value"),
            Input(ids.BUY_CURRENCY, "value"),
            Input(ids.SELL_BUY_TIME_RANGE_TABS, "value"),
            Input(ids.SELECT_DATE)
        ],
    )

    def update_trend_chart(sell_currency:str, buy_currency:str, sell_buy_time_range_tabs:str, select_date:str):
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

        
# Viola to change # Create 
        # merged_df[f{sell_currency}/"user_base_rate"] = (
        # (1/merged_df["Rate_input"])/(1/merged_df["Rate_base"]))

    
    
        final_data = sell_data[(data["Date"] >= start_date) & (sell_data["Date"] <= end_date)]
         # Calculates % change
        initial_rate = final_data["Rate"].iloc[-1]
        final_rate = final_data["Rate"].iloc[0]
        percent_change = ((final_rate - initial_rate) / initial_rate) * 100

         # Określenie kierunku zmiany (wzrost/spadek)
        if percent_change > 0:
            arrow = "▲"
            color = "green"
        elif percent_change < 0:
            arrow = "▼"
            color = "red"
        else:
            arrow = ""
            color = "black"

        summary = html.Div([
        html.Span(f"Actual FX Rate for ktualna wartość: {final_rate:.6f}", style={"marginRight": "10px"}),
        html.Span(f"Zmiana procentowa: {percent_change:.2f}% {arrow}", style={"color": color}),
    ]
   
        )
       

        return summary, 

    return dcc.Graph(id=ids.FX_RATE_SUMMARY)


        