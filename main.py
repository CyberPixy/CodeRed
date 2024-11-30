""" The core module of the apllication, that encapsulate app logic
"""
# import dash
# from dash import dcc, html, Input, Output, State
# import pandas as pd
# # import plotly.express as px
# from datetime import datetime
from src.fetch_and_save_data import fetch_and_save_fx_rate
from dash_app import run_dash

# from src.fx_convertor import convert_currency, get_currency_trend

def main():

    while True:
        print("\nMain Menu:")
        print("1. Retrieve current rate for EUR base currencies to csv file")
        print("2. Run Dash UI")
        print("3. Create a stop order")
        print("4. Create a limit order")
        print("7. Exit")
        
        choice = input("Enter the option number from menu: ")

        if choice == '1':
            print("Started: Fetching FX rate data....")
            fetch_and_save_fx_rate()
        elif choice == '2':
            try:
                run_dash()
                
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

            input("\n To continue press Enter")
        # elif choice == '3.?':
        #     try:
        #         from_currency_input = input("Enter the currency you wish to see trend(e.g., ZAR, ISK): ").strip().upper()
        #         trend = get_currency_trend(from_currency_input)
        #         print(f"The trend for EUR/{from_currency_input} is {trend[0]}. Initial rate:{trend[1]}, Latest rate: {trend[2]}")
        #     except ValueError as e:
        #         print(f"Error: {e}")
        #     except Exception as e:
        #         print(f"An error occurred: {e}")
        #     input("\n To continue press Enter")
        # elif choice == '3':
        #     create_stop_order()
        # elif choice == '4':
        #     create_limit_order()
       
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid or unavailable choice, please select a valid option.")
            input("\n To continue press Enter")
  
    

if __name__ =="__main__":
    main()
    print("The End")