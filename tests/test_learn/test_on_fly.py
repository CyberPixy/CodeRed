import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pandas as pd

from src.fetch_and_save_data import fetch_fx_rate, save_to_csv

fx_spot_csv = 'C:\Users\48570\source\python_repository\codeRed\CodeRed-1\data_csv\fx_rates.csv'

fx_spt_df = pd.read_csv(fx_spot_csv)

