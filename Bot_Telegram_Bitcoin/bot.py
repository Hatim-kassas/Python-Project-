import requests
import time

#Global Variables
api_key = "Enter Your API KEY Here"
bot_key = "Enter Your BOT KEY Here"
chat_id = "Enter Your CHAT ID Here"
limit = 50000 # Default limit
time_interval = 10 * 60 # Default Time Interval


def get_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price

def send_update(chat_id, msg):
    url = f'https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}'
    requests.get(url)

def main():
    while True:
        price = get_price()
        print(price)
        if price < limit:
            send_update(chat_id, f"update bitcoin price : {price}") # Default Message
        time.sleep(time_interval)
main()



