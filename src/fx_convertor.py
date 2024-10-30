'''This module  include functionalities:
    swap_currency() 
    ...
     '''


def swap_currency(amount, input_ccy_code, swap_to_ccy):
    """
    Converts an amount from the given currency to the target currency

    This function takes three parameters: input_ccy, the amount to swap, and the target_currency. It than calulates the converted amount based on current
    exchange rate.
   
    : param  given_currency: str - The currency of User input
    : param amount: float -  User amount of money give in currency 
    : param swap_to_ccy: str -  currency to buy in target currency

    :return: fload - The converted amount in the target currency

    """
    converted_amount = (amount/input_ccy_code) * swap_to_ccy
    return converted_amount
    