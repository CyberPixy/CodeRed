import pandas

from data.loader import DataSchema, load_transaction_data

path = r'C:\Users\48570\source\python_repository\codeRed\CodeRed-1\data_csv\fx_rates.csv'

data = load_transaction_data(path)
print(data['Currency'].unique())
