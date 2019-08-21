import requests

def get_btc(date = ""):
    current_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    date_url = "https://api.coindesk.com/v1/bpi/historical/close.json"
    if date:
        print("Date found:", date)
        response = requests.get(date_url)
        result = response.json()
    else:
        print("No date found!")
        response = requests.get(current_url)
        response_json = response.json()
        result = response_json["bpi"]["USD"]["rate"]


    return result
# current https://api.coindesk.com/v1/bpi/currentprice.json

#                               NO IF STATEMENTS
#   use a library to interpret date when imputed


print(get_btc(""))
#     if info == '1':
#     current_usd = result["bpi"]["USD"]["rate"]
#     print(current_usd)
#     print(current_usd)
