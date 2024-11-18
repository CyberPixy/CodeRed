import pandas as pd

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px 
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:

    @app.callback(
        Output(ids.TREND_CHART, "figure"),
        [
            # Input(ids.YEAR_DROPDOWN, "value"),
            # Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CURRENCY_DROPDOWN, "value"),
        ],
    )
    def update_trend_chart(selected_currencies: list[str])-> html.Div:
        '''    '''
       # Create a line chart of the selected currency's trend
        if not selected_currencies:
            return{
                'data': [], 
                'layout': {
                    'title': "Select a currency tp display the plot.", 
                    'xaxis': {'visible': False}, 
                    'yaxix': {'visible': False},
                },
            }
        df_end_of_month = data[data["Date"] == data.groupby(["Year", "Month"])["Date"].transform("max")]

        if selected_currencies:
            # Filtrowanie danych po wybranych walutach
            filtered_data = df_end_of_month[df_end_of_month["Currency"].isin(selected_currencies)]
        else:
            # Bez wyboru walut pokazujemy wszystkie dane
            filtered_data = df_end_of_month

        if filtered_data.empty:
            return {
                "data": [],
                "layout": {
                    "title": "No data available for the selected filters.",
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

        # Tworzenie wykresu liniowego
        fig = px.line(
            filtered_data,
            x="Date",
            y="Rate",
            color="Currency",
            title="FX Rates Over Time",
            labels={"Rate": "Rate", "Date": "Date", "Currency": "Currency"},
        )

        # Dodanie pełnych miesięcy do osi X
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
    

    
