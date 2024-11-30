"This module provide function that transform data into datasets, that will get use in dash layout visualisation for select values graph and othe visualisations"""


import pandas as pd
from src.data.loader import load_transaction_data

path = r'C:\Users\48570\source\python_repository\codeRed\CodeRed-1\data_csv\fx_rates.csv'



df = load_transaction_data(path)
# print(data)


# df = pd.DataFrame(data)

# Waluty wejściowe od użytkownika
currency_input = "PLN"  # Waluta użytkownika 1
currency_base = "CHF"   # Waluta użytkownika 2


def deffered_data(df=df, ccy_input: str=currency_input, currency_base:str = currency_base):
    # Filtrowanie danych dla obu walut
    df_input = df[df["Currency"] == currency_input]
    df_base = df[df["Currency"] == currency_base]

    # Merging danych dla przeliczeń
    merged_df = pd.merge(
        df_input,
        
        df_base,
        on=["Date", "Year", "Month"],
        suffixes=("_input", "_base"),
    )

    # Tworzenie nowej kolumny z przeliczeniami
    merged_df["user_base_rate"] = (
        (1/merged_df["Rate_input"])/(1/merged_df["Rate_base"]))

    # Finalny DataFrame z wybranymi kolumnami
    enriched_df = merged_df[[
        "Date",
        "Currency_input",
        "Rate_input",
        "Currency_base",
        "Rate_base",
        "Year",
        "Month",
        "user_base_rate",
    ]]

    # Renaming columns for clarity
    enriched_df.columns = [
        "Date",
        "Input_Currency",
        f'{ccy_input}/EUR',
        "Swap_To_Ccy",
        "Swap_To_Ccy_EUR_Base_Rate",
        "Year",
        "Month",
        f'{ccy_input}/{currency_base}',
    ]

    
    return enriched_df


# test = deffered_data(df)
# # print(test)
'''
Wyjaśnienie:

    Filtracja danych:
        df_input zawiera dane dla waluty wejściowej (np. "USD").
        df_base zawiera dane dla waluty bazowej (np. "CHF").

    Łączenie danych (merge):
        Dane są łączone na podstawie wspólnych kolumn: Date, Year, i Month.

    Kolumny wyjściowe:
        input_EU_Rate: kurs waluty wejściowej w EUR.
        eur_rate_base: kurs waluty bazowej w EUR.
        user_base_rate: wynik przeliczenia.

    Renaming:
        Kolumny są zmieniane, aby odpowiadały Twojemu oczekiwanemu formatowi.

Możesz zmieniać wartości currency_input i currency_base, aby przeliczać dla innych walut!'''

# # input currency rate injest from df
# # print(data_df.to_string(index=False))
# sorted_data = data_df.sort_values(by=['Date', 'Currency'], ascending=[False, True]).copy() #sort data by a date descending
# print(sorted_data.head(1))

# # current_date = data_df['Date'].max() # get current date for data set
# # # print(current_date)
# input_ccy = "CHF"
# input_ccy_data = sorted_data[sorted_data['Currency']==input_ccy].copy()
# print(input_ccy_data)
# user_base = "CHF"
# required_base_date = sorted_data[sorted_data['Currency']==user_base]
# input_ccy_data[{user_base}+'Rate'] = (input_ccy_data['Rate']*input_ccy_data[user_base])

# print(input_ccy_data)
# from_rate = df[df['Currency'] == from_currency]['Rate'].values
# # output currency rate injest from df
# to_rate = df[df['Currency'] == to_currency]['Rate'].values

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# current_date = data_df['Date'].max() # get current date for data set