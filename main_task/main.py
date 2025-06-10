import time
from datetime import datetime

from db import init_db, save_price, get_all_prices
from btc import get_bitcoin_price, calculate_stats, get_recommendation

init_db()

while True:
    try:
        current_price = get_bitcoin_price()
        save_price(current_price)

        prices = get_all_prices()
        avg, min_p, max_p = calculate_stats(prices)
        recommendation = get_recommendation(avg, current_price)

        print(f"[{datetime.now()}] Current: ${current_price} | Avg: ${avg:.2f} | Min: ${min_p} | Max: ${max_p} | Recommendation: {recommendation}")
        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(60)
