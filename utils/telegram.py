import requests
    
def send_message_to_telegram(message, token):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    chat_id = "6601277199"
    params = {
        "text": message,
        "chat_id": chat_id
    }
    response = requests.post(url, json=params)
    if response.status_code != 200:
        print("Hata:", response.status_code, response.json())