from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Przykładowe dane
data = pd.DataFrame({
    "Date": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02"],
    "Currency": ["USD", "EUR", "USD", "EUR"],
    "Rate": [1.1, 0.9, 1.2, 0.85]
})
data["Date"] = pd.to_datetime(data["Date"])

# Funkcja do tworzenia dropdown
def create_dropdown(label: str, id: str, options: list[str]) -> html.Div:
    return html.Div(
        children=[
            html.P(label),
            dcc.Dropdown(
                id=id,
                options=[{"label": currency, "value": currency} for currency in options],
                placeholder="Select a currency...",
            ),
        ],
        style={"margin-bottom": "20px"}
    )

# Funkcja do tworzenia layoutu
def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    unique_currencies = data["Currency"].unique().tolist()
    return html.Div(
        className="app-div",
        children=[
            html.H1("Currency Exchange Dashboard"),
            html.Hr(),
            create_dropdown(
                label="Select the currency you want to sell:",
                id="sell_currency_dropdown",
                options=unique_currencies,
            ),
            create_dropdown(
                label="Select the currency you want to buy:",
                id="buy_currency_dropdown",
                options=unique_currencies,
            ),
            dcc.Graph(id="currency_rate_chart"),  # Miejsce na wykres
            html.Div(id="output_div")  # Miejsce na informacje
        ],
    )

# Callback do obsługi wyborów i generowania wykresu
def register_callbacks(app: Dash, data: pd.DataFrame):
    @app.callback(
        [
            Output("currency_rate_chart", "figure"),
            Output("output_div", "children")
        ],
        [
            Input("sell_currency_dropdown", "value"),
            Input("buy_currency_dropdown", "value"),
        ],
    )
    def update_chart(sell_currency, buy_currency):
        if not sell_currency or not buy_currency:
            return {}, "Please select both currencies."
        
        # Filtruj dane dla wybranych walut
        filtered_data = data[data["Currency"].isin([sell_currency, buy_currency])]

        if filtered_data.empty:
            return {}, "No data available for the selected currencies."
        
        # Twórz wykres
        fig = px.line(
            filtered_data,
            x="Date",
            y="Rate",
            color="Currency",
            title=f"Exchange Rates: {sell_currency} and {buy_currency}",
            labels={"Rate": "Exchange Rate", "Date": "Date", "Currency": "Currency"}
        )
        return fig, f"Displaying rates for {sell_currency} and {buy_currency}."

# Tworzenie aplikacji
app = Dash(__name__)
app.title = "Currency Exchange Dashboard"
app.layout = create_layout(app, data)
register_callbacks(app, data)

if __name__ == "__main__":
    app.run(debug=True)
