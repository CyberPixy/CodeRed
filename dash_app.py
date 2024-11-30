from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP # type: ignore
from src.components.layout import create_layout
from src.data.loader import load_transaction_data
from src.fetch_and_save_data import fetch_and_save_fx_rate
from src.components.callbacks import update_chart_callbacks
DATA_PATH = r'C:\Users\48570\source\python_repository\codeRed\CodeRed-1\data_csv\fx_rates.csv'

def run_dash() -> None:
    try:
        data = load_transaction_data(DATA_PATH)     # load the latest fx data into the fx_rates.csv file and save it down in data+csv folder
    except FileNotFoundError as err:
        print(f"Error found: {err}, requesting date API")
        fetch_and_save_fx_rate()
        data = load_transaction_data(DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP]) # creates the app dashapp and allow it to use bootstap 
    app.title = "FX Rate Tracker and Conversion Tool"
    app.layout = create_layout(app, data)
    update_chart_callbacks(app, data)
    app.run()


