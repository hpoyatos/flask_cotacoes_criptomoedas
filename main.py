from flask import Flask
app = Flask(__name__)

import requests
import json
import locale
from datetime import datetime, timedelta

@app.route('/')
def main():
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    r = requests.get('https://api.bitcointrade.com.br/v3/public/BRLBTC/ticker')
    btc_cotacao = ""
    btc_cotacao_data = ""
    if r.status_code == 200:
        json = r.json()
        btc_cotacao = json['data']['buy']
        data = datetime.strptime(json['data']['date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        data -= timedelta(hours=3)
        btc_cotacao_data = data.strftime("%d/%m/%Y %H:%M:%S")

    r = requests.get('https://api.bitcointrade.com.br/v3/public/BRLETH/ticker')
    eth_cotacao = ""
    eth_cotacao_data = ""
    if r.status_code == 200:
        json = r.json()
        eth_cotacao = json['data']['buy']
        data = datetime.strptime(json['data']['date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        data -= timedelta(hours=3)
        eth_cotacao_data = data.strftime("%d/%m/%Y %H:%M:%S")

    r = requests.get('https://api.bitcointrade.com.br/v3/public/BRLBCH/ticker')
    bch_cotacao = ""
    bch_cotacao_data = ""
    if r.status_code == 200:
        json = r.json()
        bch_cotacao = json['data']['buy']
        data = datetime.strptime(json['data']['date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        data -= timedelta(hours=3)
        bch_cotacao_data = data.strftime("%d/%m/%Y %H:%M:%S")

    html = "<div style='position:relative'>\
        <div style='float:left; width: 33%; border: 1px solid black; height:100px; text-align: center;'><br>BTC<br>{}<br>{}\
        </div>\
        <div style='float:left; width: 33%; border: 1px solid black; height:100px; text-align: center;'><br>BCH<br>{}<br>{}\
        </div>\
        <div style='float:left; width: 33%; border: 1px solid black;height:100px; text-align: center;'><br>ETH<br>{}<br>{}\
        </div>\
    </div>".format(btc_cotacao_data, locale.currency(btc_cotacao, grouping=True),
    bch_cotacao_data, locale.currency(bch_cotacao, grouping=True),
    eth_cotacao_data, locale.currency(eth_cotacao, grouping=True))

    return html