import requests

def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']

def calculate_stats(prices):
    if not prices:
        return 0, 0, 0
    avg = sum(prices) / len(prices)
    return avg, min(prices), max(prices)

def get_recommendation(avg_price, current_price):
    if current_price < avg_price:
        return "Buy"
    elif current_price > avg_price:
        return "Sell"
    return "Hold"
