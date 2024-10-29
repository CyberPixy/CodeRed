'''This module  include functionalities:
    swap_currency() 
    ...
     '''


def swap_currency(given_currency, amount, swap_to_ccy, 
                  ):
    """
    Converts an amount from the given currency to the target currency

    This function takes four parameters: the data with current_rates, input_ccy, the amount to swap, and the target_currency. It than calulates the converted amount based on current
    exchange rate.
    
    : current_rates: dict - A dictionary containing current  fx exchange rate  source from api data
    : param  given_currency: str - The currency of User input
    : param amount: float -  User amount of money give in currency 
    : param swap_to_ccy: str -  currency to buy in target currency
    : param b

    :return: fload - The converted amount in the target currency

    """
    converted_amount = float(amount)/fx_rates[given_currency] * fx_rates[swap_currency]
    return converted_amount
    