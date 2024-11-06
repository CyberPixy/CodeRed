""" The core module of the apllication, that encapsulate app logic
"""
from src.fetch_and_save_data import fetch_and_save_fx_rate
from src.fx_convertor import convert_currency, get_currency_trend

def main():

    while True:
        print("\nMain Menu:")
        print("1. Retrieve current rate for EUR base currencies to csv file")
        print("2. Convert an amount from one currency to another")
        print("3. Analyze current and historic data for trend and suggeste if exchange")
        print("4. Create a stop order")
        print("5. Create a limit order")
        print("6. Plot chart showing rates over a last month")
        print("7. Exit")
        
        choice = input("Enter the option number from menu: ")

        if choice == '1':
            fetch_and_save_fx_rate()
        elif choice == '2':
            try:
                amount_input = float(input("Enter the amount to convert: "))
                from_currency_input = input("Enter the currency you have (e.g., ZAR, ISK): ").strip().upper()
                to_currency_input = input("Enter the currency you want (e.g., AUD, BGN): ").strip().upper()
                converted_amount = convert_currency(amount_input, from_currency_input, to_currency_input)          # Conversion
                print(f"Converted:{amount_input}''{from_currency_input} is {converted_amount[0]:.2f} {to_currency_input}, and todays'fx for {from_currency_input} is {converted_amount[1]}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

            input("\n To continue press Enter")
        elif choice == '3':
            try:
                from_currency_input = input("Enter the currency you wish to see trend(e.g., ZAR, ISK): ").strip().upper()
                trend = get_currency_trend(from_currency_input)
                print(f"The trend for EUR/{from_currency_input} is {trend[0]}. Initial rate:{trend[1]}, Latest rate: {trend[2]}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
            input("\n To continue press Enter")
        # elif choice == '4':
        #     create_stop_order()
        # elif choice == '5':
        #     create_limit_order()
        # elif choice == '6':
        #     plot_chart()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid or unavailable choice, please select a valid option.")
            input("\n To continue press Enter")
  
    

if __name__ =="__main__":
    main()
    print("The End")