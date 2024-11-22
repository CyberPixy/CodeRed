import pandas as pd

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px 
from . import ids


def render(app, data: pd.DataFrame):
    """
    Renderuje wykres liniowy pokazujący dane dla tylko jednej wybranej waluty.
    """

    @app.callback(
        Output(ids.TREND_CHART, "figure"),
        [Input(ids.CURRENCY_DROPDOWN, "value")],
    )
    def update_trend_chart(selected_currency:list[str]):
        """
        Aktualizuje wykres dla wybranej waluty.

        :param selected_currency: Waluta wybrana przez użytkownika.
        :return: Obiekt wykresu.
        """
        # Wyznaczenie ostatniego dnia miesiąca dla wybranej waluty
        # df_end_of_month = data[data["Date"] == data.groupby(["Year", "Month"])["Date"].transform("max")]
        df_end_of_month = data[data["Date"].isin(data.groupby(["Year", "Month"])["Date"].transform("max"))]
        if not selected_currency:
            # Jeśli użytkownik nie wybrał waluty, zwracamy pusty wykres z komunikatem.
            return {
                "data": [],
                "layout": {
                    "title": "Please select a currency to display.",
                    "xaxis": {"visible": False},
                    "yaxis": {"visible": False},
                },
            }

        # Filtrowanie danych dla wybranej waluty
        filtered_data = df_end_of_month[df_end_of_month["Currency"] == selected_currency]

        if filtered_data.empty:
            # Jeśli brak danych dla wybranej waluty, zwracamy pusty wykres z komunikatem.
            return {
                "data": [],
                "layout": {
                    "title": f"No data available for the selected currency: {selected_currency}.",
                    "xaxis": {"visible": True, "title": "Date"},
                    "yaxis": {"visible": True, "title": "Rate"},
                },
            }

        # Tworzenie listy wszystkich miesięcy dla osi X
        all_dates = pd.date_range(
            start=filtered_data["Date"].min(),
            end=filtered_data["Date"].max(),
            freq="M",
        )

        # Tworzenie wykresu liniowego dla jednej waluty
        fig = px.line(
            filtered_data,
            x="Date",
            y="Rate",
            title=f"FX Rate Over Time: {selected_currency}",
            labels={"Rate": "Rate", "Date": "Date"},
        )

        # Dodanie pełnych miesięcy do osi X i dynamicznej osi Y
        fig.update_layout(
            xaxis=dict(
                tickformat="%b %Y",  # Formatowanie osi X na miesiące i rok
                tickmode="array",    # Wymuszenie ręcznego ustawienia punktów siatki
                tickvals=all_dates,  # Ustawienie wszystkich dostępnych miesięcy
            ),
            yaxis=dict(
                tickformat=".3f",  # Precyzja do 3 miejsc po przecinku
                range=[
                    filtered_data["Rate"].min() * 0.95,
                    filtered_data["Rate"].max() * 1.05,
                ],
                showgrid=True,  # Wyświetlanie siatki
            ),
            height=700,  # Zwiększenie wysokości wykresu
        )

        return fig

    return dcc.Graph(id=ids.TREND_CHART)


    

    
