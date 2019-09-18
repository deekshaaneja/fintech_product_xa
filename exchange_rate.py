import requests
import json
from BaseError import NotFoundError


def get_exchange_rate(currency):
    currency_rate = -1
    url = "https://openexchangerates.org/api/latest.json?app_id=841a28ce9a464522bae12e9001d22ec8"

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    rates = parsed['rates']

    if currency in rates:
        currency_rate = parsed['rates'][currency]
    else:
        raise NotFoundError("Could not retrieve curreny info from open exchange. Please check the curency type.")
    return currency_rate

def get_valid_currencies():
    url = "https://openexchangerates.org/api/latest.json?app_id=841a28ce9a464522bae12e9001d22ec8"

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    rates = parsed['rates']
    return rates.keys()

# print(get_valid_currencies())