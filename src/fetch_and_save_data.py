"""Please find list of API that will be used in thise project 
- "https://api.frankfurter.app/latest"  # List of spot rate to base Eur to all available currencies on the API
- "https://api.frankfurter.app/latest?symbols=CHF"  #Limit the response to specific target currencies.
- "https://api.frankfurter.app/2024-01-01..?symbols=USD" #Filter currencies to reduce response size and improve performance

This module  will be used to define structure of source FX rate and if needed its transformation, for app requirement to hold data in csv or database

"""
import requests # library for simple HTTP request 
import csv # csv format files reading and writing 




api_fx_spot_url = "https://api.frankfurter.app/latest"  # Frnakfurt URL API endpoint

def fetch_fx_rate():
    '''Function to request get api url defined with api_fx_spot_url, check the response status, return json format response or catch  other then OK status'''
    response = requests.get(api_fx_spot_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Fails to fetch data from API. Status code{response.status_code}")
    

def save_to_csv(data, filepath='data/fx_rates.csv'):
    ''' Function to save the FX rate to a CSV file 
    :param data: data return from the API 
    :param filepath: Path to save the CSV file, default(filepath='data/fx_rates.csv) '''
    rates = data.get("rates", {})
    date = data.get("date", "") 
    with open(filepath, mode='w', newline='') as file:

        writer = csv.writer(file)
        writer.writerow(["Currency", "Rate", "Date"])
        for currency, rate in rates.items():
            writer.writerow([date, currency, rate])



