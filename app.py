""" The core module of the apllication, that encapsulate app logic
"""
from src.fetch_and_save_data import fetch_fx_rate, save_to_csv


def main():
    try:
        data = fetch_fx_rate()
        save_to_csv(data=data)

        print("All Good")
    except Exception as e:
        print(f"Error {e} occured, please veryfied")
  
    

if __name__ =="__main__":
    main()
    print("Finish running main code")