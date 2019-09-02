import requests
from flask import Flask, render_template , flash
from flask import request
import os
import jinja2
import cgi
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


app = Flask(__name__)
app.secret_key = 'WEIRD!'

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

@app.route('/')
def alert():
    date = request.args.get('date')
    template = jinja_env.get_template('alert.html')
    return template.render(btc = get_btc(date), user = date)

if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0")

#     current_usd = result["bpi"]["USD"]["rate"]
#       ?start=2016-07-17&end=2016-08-17
#   http://73.56.66.248:5000/?date=(Date goes here in YYYY-MM-DD form)
# -----------@app.route('/')----------------
#            def index():
#               date = request.args.get('date')
#               return get_btc(date)
