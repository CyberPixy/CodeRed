import requests # library request 
import csv 

"""Please find list of API that will be used in thise project 
- "https://api.frankfurter.app/latest"  # List of spot rate to base Eur to all available currencies on the API
- "https://api.frankfurter.app/latest?symbols=CHF"  #Limit the response to specific target currencies.
- "https://api.frankfurter.app/2024-01-01..?symbols=USD" #Filter currencies to reduce response size and improve performance
"""


api_fx_spot = "https://api.frankfurter.app/latest"  # variable to hold http get request call base URL API


r = requests.get(api_fx_spot) # now we have response object 
print(r)


