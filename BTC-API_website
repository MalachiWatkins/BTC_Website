import requests

def get_btc(date = ""):
    current_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    date_url = "https://api.coindesk.com/v1/bpi/historical/close.json"
    user_date = {'start': date , 'end': date}
    if date:
        print("Date found:", date)
        response = requests.get(date_url, params=user_date)
        result = response.json()["bpi"]
    else:
        print("No date found!")
        response = requests.get(current_url)
        response_json = response.json()
        result = response_json["bpi"]["USD"]["rate"]


    return result
# current https://api.coindesk.com/v1/bpi/currentprice.json

#                               NO IF STATEMENTS
#   use a library to interpret date when imputed


print(get_btc("2015-06-01"))
#     if info == '1':
#     current_usd = result["bpi"]["USD"]["rate"]
#     print(current_usd)
#     print(current_usd)
#       ?start=2016-07-17&end=2016-08-17
