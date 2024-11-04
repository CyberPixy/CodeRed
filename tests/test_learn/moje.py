import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

# Load data from the CSV file
data_df = pd.read_csv("fx_rates.csv")

data_df['date'] = pd.to_datetime(data_df['date'])

# Function to get the trend of the rate
def get_currency_trend(df, currency):
    currency_data = df[df['ccy_rate'] == currency].sort_values(by='date')
    if len(currency_data) < 2:
        return "Not enough data to determine trend."
    
    initial_rate = currency_data.iloc[0]['rate']
    latest_rate = currency_data.iloc[-1]['rate']
    
    trend = "upward" if latest_rate > initial_rate else "downward"
    return f"The trend for {currency} is {trend}. Initial rate: {initial_rate}, Latest rate: {latest_rate}."

# Dash app setup
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Currency Rate Trend and Orders"),
    dcc.Dropdown(
        id='currency-dropdown',
        options=[{'label': currency, 'value': currency} for currency in data_df['ccy_rate'].unique()],
        placeholder="Select a currency"
    ),
    html.Div(id='trend-output'),
    html.H3("Create Stop and Limit Orders"),
    html.Div([
        html.Label("Order Type"),
        dcc.RadioItems(
            id='order-type',
            options=[{'label': 'Stop Order', 'value': 'stop'}, {'label': 'Limit Order', 'value': 'limit'}],
            value='stop'
        ),
        html.Label("Set Price"),
        dcc.Input(id='set-price', type='number', placeholder="Enter the stop/limit price"),
        html.Button('Submit Order', id='submit-order', n_clicks=0),
        html.Div(id='order-output')
    ]),
    dcc.Graph(id='currency-trend-graph')
])

@app.callback(
    [Output('trend-output', 'children'), Output('currency-trend-graph', 'figure')],
    [Input('currency-dropdown', 'value')]
)
def update_trend(currency):
    if currency is None:
        return "", go.Figure()
    
    trend_info = get_currency_trend(data_df, currency)
    filtered_data = data_df[data_df['ccy_rate'] == currency]
    
    # Create a line chart of the selected currency's trend
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_data['date'], y=filtered_data['rate'], mode='lines', name=currency))
    fig.update_layout(title=f"Trend for {currency}", xaxis_title="Date", yaxis_title="Rate")
    
    return trend_info, fig

@app.callback(
    Output('order-output', 'children'),
    [Input('order-type', 'value'), Input('set-price', 'value'), Input('currency-dropdown', 'value'), Input('submit-order', 'n_clicks')]
)
def create_order(order_type, price, currency, n_clicks):
    if n_clicks > 0:
        if not currency or price is None:
            return "Please select a currency and set a price."
        if order_type == 'stop':
            return f"Stop order set for {currency} at price {price}."
        elif order_type == 'limit':
            return f"Limit order set for {currency} at price {price}."
    return ""

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
