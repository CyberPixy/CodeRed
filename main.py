from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP # type: ignore

from src.components.layout import create_layout
from src.data.loader import load_transaction_data
from src.fetch_and_save_data import fetch_and_save_fx_rate
DATA_PATH = r'C:\Users\48570\source\python_repository\codeRed\CodeRed-1\data_csv\fx_rates.csv'


def main() -> None:

    # load the data and create the data manager
    try:
        data = load_transaction_data(DATA_PATH)

        print(data)
    except FileNotFoundError as err:
        fetch_and_save_fx_rate()
        data = load_transaction_data(DATA_PATH)
        # print(data)
    app = Dash(external_stylesheets=[BOOTSTRAP]) # creates the app dashapp and allow it to use bootstap 
    app.title = "Currency Rate Trend dashboard"
    app.layout = create_layout(app, data)
    app.run()


if __name__ == "__main__":
    main()
    