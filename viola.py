import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px
from datetime import datetime

# Tworzenie aplikacji Dash
app = dash.Dash(__name__, external_stylesheets=["/assets/style.css"])
app.title = "Kalkulator Walutowy"

# Wczytywanie danych
data = pd.DataFrame({
    "Date": ["2024-11-19", "2024-11-18", "2024-11-15", "2024-11-14", "2024-11-13"],
    "Input_Currency": ["PLN"] * 5,
    "PLN/EUR": [4.3303, 4.3278, 4.3200, 4.3383, 4.3425],
    "Swap_To_Ccy": ["CHF"] * 5,
    "Swap_To_Ccy_EUR_Base_Rate": [0.9329, 0.9364, 0.9389, 0.9369, 0.9379],
    "PLN/CHF": [4.215435, 4.216369, 4.217338, 4.215960, 4.215982]
})


# Funkcja deffered_data
def deffered_data(df, sell_currency: str, buy_currency: str):
    """
    Filtrowanie i obliczenia na podstawie walut i daty.

    Args:
        df (pd.DataFrame): Dane walutowe.
        sell_currency (str): Waluta wejściowa (sprzedaż).
        buy_currency (str): Waluta wyjściowa (zakup).

    Returns:
        enriched_df (pd.DataFrame): Przetworzony DataFrame.
    """
    # Filtrowanie danych na podstawie walut
    df_sell = df[df["Input_Currency"] == sell_currency]
    df_buy = df[df["Swap_To_Ccy"] == buy_currency]

    # Łączenie danych dla obliczeń
    enriched_df = pd.merge(
        df_sell,
        df_buy,
        on=["Date", "PLN/EUR", "Swap_To_Ccy_EUR_Base_Rate", "PLN/CHF"],
        how="inner"
    )

    return enriched_df


# Layout aplikacji
app.layout = html.Div([
    html.H1("Kalkulator Walutowy", className="title"),

    # Główna sekcja formularza
    html.Div(className="form-container", children=[
        html.Div(className="form-field", children=[
            html.Label("Kwota:"),
            dcc.Input(
                id="amount",
                type="number",
                placeholder="Podaj kwotę",
                step=0.01
            )
        ]),
        html.Div(className="form-field", children=[
            html.Label("Mam:"),
            dcc.Input(
                id="sell_currency",
                type="text",
                placeholder="Podaj walutę wejściową (np. PLN)"
            )
        ]),
        html.Div(className="form-field", children=[
            html.Label("Chcę otrzymać:"),
            dcc.Input(
                id="buy_currency",
                type="text",
                placeholder="Podaj walutę wyjściową (np. CHF)"
            )
        ]),
    ]),

    # Wybór daty
    html.Div(className="date-picker-container", children=[
        html.Label("Wybierz datę:"),
        dcc.DatePickerSingle(
            id="date_picker",
            date=datetime.now().date(),
            display_format="DD.MM.YYYY"
        )
    ]),

    # Przycisk "Przelicz" i "Pokaż Trend"
    html.Div(className="button-container", children=[
        html.Button("Przelicz", id="convert_button", n_clicks=0, style={"marginRight": "10px"}),
        html.Button("Pokaż Trend", id="trend_button", n_clicks=0)
    ]),

    # Wynik
    html.Div(id="result", className="result", style={"marginTop": "20px"}),

    # Wykres trendu
    dcc.Graph(id="trend_plot", style={"marginTop": "20px"})
])


# Callback do przeliczenia walut
@app.callback(
    Output("result", "children"),
    Input("convert_button", "n_clicks"),
    State("amount", "value"),
    State("sell_currency", "value"),
    State("buy_currency", "value"),
    State("date_picker", "date")
)
def calculate_exchange_rate(n_clicks, amount, sell_currency, buy_currency, date):
    if n_clicks == 0 or amount is None or not sell_currency or not buy_currency:
        return "Proszę uzupełnić wszystkie pola."

    # Filtrowanie danych na podstawie daty
    filtered_data = data[data["Date"] == date]
    if filtered_data.empty:
        return f"Błąd: Brak danych dla wybranej daty {date}."

    # Wywołanie funkcji deffered_data
    enriched_df = deffered_data(filtered_data, sell_currency, buy_currency)
    if enriched_df.empty:
        return f"Błąd: Nie znaleziono kursu dla {sell_currency} -> {buy_currency} na dzień {date}."

    # Pobieranie kursu przeliczeniowego
    rate_column = f"{sell_currency}/{buy_currency}"
    rate = enriched_df["PLN/CHF"].values[0]

    # Obliczenie kwoty
    converted_amount = amount * rate
    return f"{amount:.2f} {sell_currency} = {converted_amount:.2f} {buy_currency} (1 {sell_currency} = {rate:.4f} {buy_currency})"


# Callback do rysowania wykresu trendu
@app.callback(
    Output("trend_plot", "figure"),
    Input("trend_button", "n_clicks")
)
def show_trend(n_clicks):
    if n_clicks == 0:
        return {}

    # Tworzenie wykresu trendu dla PLN/CHF
    fig = px.line(
        data,
        x="Date",
        y="PLN/CHF",
        title="Trend PLN/CHF w czasie",
        labels={"Date": "Data", "PLN/CHF": "Kurs PLN/CHF"},
        markers=True
    )
    fig.update_layout(
        title={"x": 0.5},  # Wyśrodkowanie tytułu
        xaxis_title="Data",
        yaxis_title="Kurs PLN/CHF"
    )
    return fig


# Uruchomienie aplikacji
if __name__ == "__main__":
    app.run_server(debug=True)
