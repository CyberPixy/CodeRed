"""Please find list of API that will be used in thise project 
- "https://api.frankfurter.app/latest"  # List of spot rate to base Eur to all available currencies on the API
- "https://api.frankfurter.app/latest?symbols=CHF"  #Limit the response to specific target currencies.
- "https://api.frankfurter.app/2024-01-01..?symbols=USD" #Filter currencies to reduce response size and improve performance

This module  will be used to define structure of source FX rate and if needed its transformation, for app requirement to hold data in csv or database

"""
import requests # library for simple HTTP request 
import csv # csv format files reading and writing
from datetime import date, datetime, timedelta


def fetch_and_save_fx_rate():
    '''Function to fetch FX rates and save them to a CSV file'''
    try:
        # Fetch data from the API
        data = fetch_fx_rate()
        
        # Save data to CSV
        save_to_csv(data)
        print("FXrate data succesfully saved to fx_rate.csv file\n")
        input("\nPress Enter for main menu...")
    except Exception as e:
        print(f"Error {e} occurred, please verify")

def get_date_one_year_ago() ->str:
    # Function that calculates date_from, that is 12months before current_date
    today = date.today()
    # one_year_ago = today.replace(year=today.year -1)
    start_date =today.replace(year=today.year -1).strftime('%Y-%m-%d') 
    return start_date

def get_last_business_day() -> str:
    # source todays  date
    today = datetime.today()
    # source last working day, before today
    if today.weekday() == 0:  # Monday
        last_business_day = today - timedelta(days=3)
    else:                     # Other week day
        last_business_day = today - timedelta(days=1)
    # Return date as string formated to YYYY-MM-DD
    return last_business_day.strftime('%Y-%m-%d')


# api_fx_spot_url = "https://api.frankfurter.app/latest"  # Frnakfurt URL API endpoint

# Fetch rates over the period interface  https://api.frankfurter.app/2024-01-01..2024-10-31

def fetch_fx_rate():
    '''Function to request get api url defined with api_fx_spot_url, check the response status, return json format response or catch  other then OK status'''
      
    start_date = get_date_one_year_ago()
    yesterday = get_last_business_day()
    api_fx_spot_url = f"https://api.frankfurter.app/{start_date}..{yesterday}"  # Frnakfurt URL API endpoint
    response = requests.get(api_fx_spot_url)
    if response.status_code == 200:
        return response.json()
        print(f'Fetching fx rate data from date:{start_date} to {yesterday} has finished')
    else:
        raise Exception(f"Fails to fetch data from API. Status code{response.status_code}")
    

def save_to_csv(data, filepath='data_csv/fx_rates.csv'):
    ''' Function to save the FX rate to a CSV file 
    :param data: data return from the API 
    :param filepath: Path to save the CSV file, default(filepath='data/fx_rates.csv) '''
    date = data.get("date", "") 
    rates = data.get("rates", {})
  
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)
        # Write header
        writer.writerow(['Date', 'Currency', 'Rate'])

        # Write data

        for date, currencies in data['rates'].items():

                for currency, rate in currencies.items():

                    writer.writerow([

                        date, 

                        currency, 

                        rate

                    ])





