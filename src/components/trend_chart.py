import pandas as pd

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.TREND_CHART, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CURRENCY_DROPDOWN, "value"),
        ],
    )
    def update_trend_chart(
        years: list[str], months: list[str], currencies: list[str]
    ) -> html.Div:
        filtered_data = data.query(
            "Year in @years and Month in @months and Currency in @currencies"
        )

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.TREND_CHART)

        # def create_pivot_table() -> pd.DataFrame:
        #     pt = filtered_data.pivot_table(
        #         values=DataSchema.RATE,
        #         index=[DataSchema.CURRENCY],
        #         aggfunc="avg",
        #         fill_value=0,
        #         dropna=False,
        #     )
        #     return pt.reset_index().sort_values(DataSchema.RATE, ascending=False)

       # Create a line chart of the selected currency's trend
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data['Rate'], mode='lines', name=Currency))
        fig.update_layout(title=f"Trend for {Currency}", xaxis_title="Date", yaxis_title="Rate")
    

        return html.Div(dcc.Graph(figure=fig), id=ids.TREND_CHART)

    return html.Div(id=ids.TREND_CHART)