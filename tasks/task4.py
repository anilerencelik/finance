from utils.time import getTime
from utils.tradingiew import get_data_from_tradingview
from utils.telegram import send_message_to_telegram

def run(config):
    print(getTime(), f"{config['name']} çalışıyor!")
    for ticker in config['params']:
        getData(ticker, config['token'])
    print(getTime(), f"{config['name']} çalıştı!")


def getData(ticker, token): 
    fields = "EMA200,open,close,high,low,Perf.5Y,Perf.3Y,Perf.Y,Perf.YTD,Perf.6M,Perf.3M,PERF.1M"
    fields = "EMA200,close"
    data = get_data_from_tradingview(ticker, fields)

    ema_below_200 = data['EMA200'] > data['close']
    diff_percentage = abs((data['EMA200'] - data['close']) / data['close']) * 100
    ema_within_2_percent = (data['close'] / data['EMA200'] ) <= 1.020001

    if ema_below_200: 
        message = f"{ticker} 200 Günlük Ortalama Altında."
        send_message_to_telegram(message, token)
    elif ema_within_2_percent:
        message = f"{ticker} 200 Günlük Ortalama Yakınında fark %{diff_percentage:.2f}."
        send_message_to_telegram(message, token)
    print(data)
