import yfinance as yf
from utils.symbol import Symbol
from utils.time import getTime
from utils.telegram import send_message_to_telegram

def run(config):
    print(getTime(), f"{config['name']} çalışıyor!")
    for code in config['params']:
        getDataFinans(code, config)
    print(getTime(), f"{config['name']} çalıştı!")

def getDataFinans(code, config):
    stock = yf.Ticker(code)
    symbol = Symbol(code, stock.info.get('currentPrice'), stock.info.get('previousClose'))

    if symbol.dailyChangePercentage < -3.5:
        send_message_to_telegram(symbol.messager2(), config['token'])