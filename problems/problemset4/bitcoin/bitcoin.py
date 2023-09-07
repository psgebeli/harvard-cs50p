# Paul Gebeline, Problem Set 4

'''

INSTRUCTIONS
------------

Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, 
Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there`s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

--Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be 
converted to a float, the program should exit via sys.exit with an error message.
--Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, 
among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of 
Bitcoins in USD to four decimal places, using , as a thousands separator.

'''

# Preamble
import json 
import requests as r 
import sys


# Function that returns the number of bitcoin the user wants to buy from cmd-line arguments
def get_input():

    # Try to convert the second cmd-line argument to a float.
    try:
        num_bitcoin = float(sys.argv[1])
    
    # Except if there is an index error (there is no second cmd-line argument), then exit with msg
    except IndexError:
        sys.exit("Please enter a command-line argument")

    # Except if there is a type error (second argument cannt be converted to a float), then exit with msg
    except TypeError:
        sys.exit("Command-line argument cannot be converted to float")

    # If it got through the exceptions, return the float
    return num_bitcoin

# Function that queries bitcoin API for the current price per bitcoin
def get_bitcoin_price():

    # Try to query the API (using requests library) and convert it to a json object
    try:
        query = r.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    
    # Except if the requests library raises some exception
    except r.RequestException:
        sys.exit("Could not query API")
    
    # Return the rate associated with {'bpi' : {'USD': { 'rate_float' : rate}} from the JSON object converted to a float
    return float(query['bpi']['USD']['rate_float'])



def main():
    
    # Call the previous to functions
    quantity_desired = get_input()
    price_per_bitcoin = get_bitcoin_price()

    # Calculate the price for the user to buy that many bitcoin
    price_total = quantity_desired * price_per_bitcoin

    # Print the price with (1) commas to seperate thousands and (2) 4 decimal places
    print(f"${price_total:,.4f}")


# Only execute if this is the script being executed
if __name__ == '__main__':
    main()

