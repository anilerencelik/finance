import yfinance as yf
from tefas import Crawler
import pandas as pd

from utils.symbol import Symbol
from utils.time import getTime, getDates
from utils.telegram import send_message_to_telegram

def run(config):
    print(getTime(), f"{config['name']} çalışıyor!")
    for fons in config['fons']:
        getDataTefas(fons, config)
    for code in config['params']:
        getDataFinans(code, config)
    print(getTime(), f"{config['name']} çalıştı!")

def getDataTefas(code, config):
    tefas = Crawler()
    dates = getDates()
    data = tefas.fetch(start=dates[1], end=dates[0], name=code, columns=["date", "price" , "code"])
    symbol = Symbol(code, data['price'][0], data['price'][1], 3)
    send_message_to_telegram(symbol.messager(), config['token'])

def getDataFinans(code, config):
    stock = yf.Ticker(code)
    symbol = Symbol(code, stock.info.get('currentPrice'), stock.info.get('previousClose'), 3)
    send_message_to_telegram(symbol.messager(), config['token'])