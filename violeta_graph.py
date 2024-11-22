import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
from src.data.transform_data import deffered_data

# Tworzenie aplikacji Dash
app = dash.Dash(__name__, external_stylesheets=["/assets/style.css"])
app.title = "FX Trend - PLN/CHF"

# Dane wejściowe
data = deffered_data()


# Konwersja kolumny "Date" do formatu datetime
data["Date"] = pd.to_datetime(data["Date"])

# Layout aplikacji
app.layout = html.Div([
    html.H1("FX Rate Trend - PLN/CHF", className="title"),

    # Górne menu
    dcc.Tabs(id="time_range_tabs", value="1D", children=[
        dcc.Tab(label="1D", value="1D"),
        dcc.Tab(label="1W", value="1W"),
        dcc.Tab(label="1M", value="1M"),
        dcc.Tab(label="6M", value="6M"),
        dcc.Tab(label="1Y", value="1Y"),
    ], className="tabs-container"),

    # Wykres i opis
    dcc.Graph(id="fx_rate_graph"),
    html.Div(id="fx_rate_summary", className="summary-container")
])


# Callback do aktualizacji wykresu i opisu
@app.callback(
    [Output("fx_rate_graph", "figure"), Output("fx_rate_summary", "children")],
    Input("time_range_tabs", "value")
)
def update_graph(time_range):
    # Określenie zakresu dat
    end_date = data["Date"].max()
    if time_range == "1D":
        start_date = end_date - timedelta(days=1)
        label = "1 dzień"
    elif time_range == "1W":
        start_date = end_date - timedelta(weeks=1)
        label = "1 tydzień"
    elif time_range == "1M":
        start_date = end_date - timedelta(days=30)
        label = "1 miesiąc"
    elif time_range == "6M":
        start_date = end_date - timedelta(days=180)
        label = "6 miesięcy"
    elif time_range == "1Y":
        start_date = end_date - timedelta(days=365)
        label = "1 rok"
    else:
        start_date = data["Date"].min()
        label = "Pełny zakres"

    # Filtrowanie danych
    filtered_data = data[(data["Date"] >= start_date) & (data["Date"] <= end_date)]

    # Obliczanie procentowej zmiany
    initial_rate = filtered_data["PLN/CHF"].iloc[0]
    final_rate = filtered_data["PLN/CHF"].iloc[-1]
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

    # Tworzenie wykresu
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=filtered_data["Date"],
        y=filtered_data["PLN/CHF"],
        mode="lines+markers",
        name="PLN/CHF",
        line=dict(color="blue"),
        marker=dict(size=6)
    ))
    fig.update_layout(
        title=f"Kurs PLN/CHF ({label})",
        xaxis_title="Data",
        yaxis_title="Kurs PLN/CHF",
        template="plotly_white"
    )

    # Dynamiczny opis
    summary = html.Div([
        html.Span(f"Aktualna wartość: {final_rate:.6f}", style={"marginRight": "10px"}),
        html.Span(f"Zmiana procentowa: {percent_change:.2f}% {arrow}", style={"color": color}),
    ])

    return fig, summary


# Uruchomienie aplikacji
if __name__ == "__main__":
    app.run_server(debug=True)
