import requests
def get_data_from_tradingview(ticker, fields):
    url = f"https://scanner.tradingview.com/symbol?symbol={ticker}&fields={fields}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Hata:", response.status_code, response.json())
        return None
    else:
        return response.json()
