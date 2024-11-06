'''This module  include functions:
    swap_currency() 
    ...
     '''
import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# PANDA SECTION(to be remove and clean up...)
# Load data from the CSV file
csv_f_path = r'C:\Users\48570\source\python_repository\codeRed\CodeRed-1\data\fx_rates.csv'
data_df = pd.read_csv(csv_f_path)
# print(data_df.head())
all_data_fx_df = data_df.sort_values(by='Date', ascending=False) #sort data by a date descending
current_date = data_df['Date'].max() # get current date for data set
current_fx_df = all_data_fx_df[all_data_fx_df["Date"] == current_date]
# print(current_fx_df)




def convert_currency(amount, from_currency, to_currency, df=current_fx_df):
    """
Converts the specified amount from one currency to another.
    x
    :param amount: The amount to be converted.
    :param from_currency: The currency from which we are converting.
    :param to_currency: The currency to which we are converting.
    :return: The converted amount.
    """
    # input currency rate injest from df
    from_rate = df[df['Currency'] == from_currency]['Rate'].values
    # output currency rate injest from df
    to_rate = df[df['Currency'] == to_currency]['Rate'].values
    
    # Check if fx_rate found for any currency
    if from_rate.size == 0 or to_rate.size == 0:
        raise ValueError("One or both currency rates not found.")
    
    # FX conversion algorythm 
    result = (amount / from_rate[0]) * to_rate[0]
    return result, to_rate 





# def get_currency_trend
    