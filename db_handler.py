import sqlite3
import os

DB_PATH = os.path.join("data", "crypto_data.db")

def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            coin_id TEXT,
            symbol TEXT,
            price_usd REAL,
            market_cap_usd REAL,
            change_24h REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_price(timestamp, coin_id, symbol, price_usd, market_cap_usd, change_24h):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO crypto_prices (
            timestamp, coin_id, symbol, price_usd, market_cap_usd, change_24h
        ) VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, coin_id, symbol, price_usd, market_cap_usd, change_24h))
    conn.commit()
    conn.close()
