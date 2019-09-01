import requests
from flask import Flask

app = Flask(__name__)
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


@app.route('/')
def index():
    return print(get_btc("2015-06-01"))


if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0")

#     current_usd = result["bpi"]["USD"]["rate"]
#       ?start=2016-07-17&end=2016-08-17
