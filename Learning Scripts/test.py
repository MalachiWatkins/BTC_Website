import requests
date = ("2016-07-17")
payload = {'start': date , 'end': date}
r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json', params=payload)

print(r.url)


#       ?start=2016-07-17&end=2016-08-17
