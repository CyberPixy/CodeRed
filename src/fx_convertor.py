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
csv_f_path = r'C:\Users\48570\source\python_repository\codeRed\CodeRed-1\data_csv\fx_rates.csv'


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def convert_currency(amount, from_currency, to_currency):
    """
Converts the specified amount from one currency to another.
    x
    :param amount: The amount to be converted.
    :param from_currency: The currency from which we are converting.
    :param to_currency: The currency to which we are converting.
    :return: The converted amount.
    """
    # input currency rate injest from df
    data_df = pd.read_csv(csv_f_path)
    # print(data_df.head())
    all_data_fx_df = data_df.sort_values(by='Date', ascending=False) #sort data by a date descending
    current_date = data_df['Date'].max() # get current date for data set
    current_fx_df = all_data_fx_df[all_data_fx_df["Date"] == current_date]
    # print(current_fx_df)
    from_rate = df[df['Currency'] == from_currency]['Rate'].values
    # output currency rate injest from df
    to_rate = df[df['Currency'] == to_currency]['Rate'].values
    
    print(f'Check {from_rate.size} ZWARIUJE')

    if from_rate.size == 0 and to_rate.size == 0:
        result = amount
    if from_currency == to_currency:
        result = amount
        # print(f'Entered from_currency: EUR!')
        # if to_rate == 'EUR':
        # if to_rate.size == 0:
        #     raise ValueError(ValueError("Currency rates cannot be blank, try with correct ccy code"))
        # result = amount * to_rate[0]
    
    # if from_currency == 'EUR':
    #     print(f'Entered from_currency: EUR!')
    #     if to_rate == 'EUR':
    #     if to_rate.size == 0:
    #         raise ValueError(ValueError("Currency rates cannot be blank, try with correct ccy code"))
    #     result = amount * to_rate[0]
    
    #     if from_currency.size == 0:
    #         raise ValueError(ValueError("Currency rates cannot be blank, try with correct ccy code"))
    #     result = (amount / from_rate[0])
    

    # Check if fx_rate found for any currency
    if from_rate.size == 0 or to_rate.size == 0:
        raise ValueError("One or both currency rates not found.")
    
    # FX conversion algorythm 
    result = (amount / from_rate[0]) * to_rate[0]
    return result, to_rate 



# Function to get the trend of the rate
def get_currency_trend(currency, df=all_data_fx_df):
    currency_data = df[df['Currency'] == currency].sort_values(by='Date')
    if len(currency_data) < 2:
        return "Not enough data to determine trend."
    
    initial_rate = currency_data.iloc[0]['Rate']
    latest_rate = currency_data.iloc[-1]['Rate']
    
    trend = "upward" if latest_rate > initial_rate else "downward"
    return trend, initial_rate, latest_rate
    