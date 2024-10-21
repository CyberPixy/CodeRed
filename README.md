## Project Overview ->Currency exchange – A program that sources current spot exchange rates for any pair of currencies, calculates day-to-day changes and plots the historical data.


Currency Exchange: final  the web App


### Project Name:  **_FXSignal_**
 Project Overview the main functionality 
- retrieve a current rate for at least 5 currencies (ideally for every available currency with base EUR)
- convert an amount provided by user from one currency to another  
- based on current and historic data get the information about the trend of the rate and suggest if it is a good moment for an exchange of a given currency (or currencies)
- allow user for creation of a stop order (an order to buy or sell a currency once the price reaches a specific price, known as the stop price. 
                When the stop price is reached, a stop order becomes a market order and is executed at the best available price (which can be lower or higher than the stop price).
                Stop orders aren't guaranteed to execute until the price of the currency reaches the set stop price.)
- allow user for creation of a limit order (an order to buy or sell currency at a price you choose, or better. Buy limit orders are executed at your specified price or lower, 
                sell limit orders are executed at your specified price or higher. Limit orders aren't guaranteed – they'll only exchange if the price of a currency increases or decreases to your set limit price. 
                If it doesn't, your order is left unfilled.)
- data retrieved from external sources should be stored in a csv file (or database)
- plot a chart showing rates across specific time frame.
- create a chart showing rates change across day-to-day, month-to-month and year-to-year for one or more currencies


Step 1 _create new python environment,  using your environment managemnt tool(conda/env)_

Step 2  _Frankfurter API Currency source [Click here](https://frankfurter.dev/). Frankfurter provides endpoints to rerive lates rates, historical data, or time series._

Step 3 _ User FX Currencies are control from config file: fx_config.json, base currency defined as EUR._

- 




