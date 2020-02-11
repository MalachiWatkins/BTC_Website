import requests
from flask import Flask, render_template , flash, url_for
from flask import request
import os
import jinja2
import cgi
import webbrowser
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
images_dir = os.path.join(os.path.dirname(__file__), 'images')
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
        result = bpi = response.json()["bpi"]
        result = list(bpi.keys())[0]
    else:
        print("No date found!")
        response = requests.get(current_url)
        response = bpi = response.json()["bpi"]["USD"]
        result = list(bpi.keys())[2]

    return bpi[result]

@app.route('/')
def BTC():
    date = request.args.get('date')
    template = jinja_env.get_template('BTC_API.html')
    return template.render(btc = get_btc(date), user = date)

@app.route('/snakes')
def snakes():
    template = jinja_env.get_template('snakes.html')
    return template.render()


if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=80)

#   http://sponge.icarus.io/?date=(Date goes here in YYYY-MM-DD form)
