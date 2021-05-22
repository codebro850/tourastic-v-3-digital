import requests
import pandas as pd
import numpy as np


def currency_convert(request, curr_currency, convert_currency):
    api = "QPBLJSYIWL2GB0UY"
    # api = "961QAZ0OUW1W2NX1"
    from_c = curr_currency
    to_c = convert_currency
    if to_c == "":
        rate = 1
    else:
        main_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" + \
            from_c+"&to_currency="+to_c+"&apikey="+api
        response = requests.get(main_url)
        result = response.json()
        print(result)
        rate = result['Realtime Currency Exchange Rate']['5. Exchange Rate']
        print(result)
    return rate


# def countryget(request):
#     url = "http://api.ipstack.com/49.15.181.132?access_key=22fbf0901acc6231dfe325c480ddf613"
#     response = requests.get(url)
#     result = response.json()
#     country = result['country_name']
#     data = pd.read_csv(
#         "D:\data for currency\country-code-currency.csv")
#     filter = (data['Country'] == country)
#     filtered = data[filter]
#     figter = filtered['Code']
#     dat = pd.concat([figter]).reset_index(drop=True)

#     return country, dat[0]

def sessioncreation(request, curr):
    request.session["curr"] = curr
