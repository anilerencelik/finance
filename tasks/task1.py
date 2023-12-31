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
    if (not stock.info.get('currentPrice')) or (not stock.info.get('previousClose')):
        return
    symbol = Symbol(code, stock.info.get('currentPrice'), stock.info.get('previousClose'), 1)

    if symbol.dailyChangePercentage < -3:
        send_message_to_telegram(symbol.messager(), config['token'])