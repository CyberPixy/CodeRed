""" The core module of the apllication, that encapsulate app logic
"""
from src.fetch_and_save_data import fetch_and_save_fx_rate


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
        
        choice = input("Enter the option number of your choice: ")

        if choice == '1':
            fetch_and_save_fx_rate()
        # elif choice == '2':
        #     convert_currency()
        # elif choice == '3':
        #     analyze_trend()
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