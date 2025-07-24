import requests
import datetime
from db_handler import create_table,insert_price

# CoinGecko IDs mapped to your symbols
coin_name_map = {
    "alchemy-pay": "ACH",
    "cardano": "ADA",
    "toshi": "TOSHI",
    "shiba-inu": "SHIBU",
    "xyo": "XYO",
    "swftcoin": "SWFT",  # spelling fixed here: swftcoin, not swtfcoin
    "bitcoin": "BTC"
}

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    ids = ",".join(coin_name_map.keys())
    params = {
        "ids": ids,
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_change": "true"
    }

    print(f"⏳ Fetching data from CoinGecko for: {ids}")
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        timestamp = datetime.datetime.utcnow().isoformat()
        print(f"\nTimestamp: {timestamp}")
        for coin in data:
            symbol = coin_name_map.get(coin, coin.upper())
            price = data[coin].get('usd', 0)
            change = data[coin].get('usd_24hr_change', 0)
            market_cap = data[coin].get('usd_market_cap', 0)
            print(f"{symbol}: ${price:.5f} | 24h Change: {change:.2f}% | Market Cap: ${market_cap:,.2f}")
            insert_price(timestamp,coin,symbol,price,market_cap,change)
        return {
            "timestamp": timestamp,
            "data": data
        }

    except Exception as e:
        print("❌ Error fetching data:", e)
        return None

# ✅ This must be outside the function, no indent
if __name__ == "__main__":
    create_table()
    fetch_crypto_data()
