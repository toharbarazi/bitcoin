import sqlite3
from datetime import datetime

DB_PATH = "bitcoin.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            price REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_price(price):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prices (price, timestamp) VALUES (?, ?)", (price, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_all_prices():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM prices")
    prices = [row[0] for row in cursor.fetchall()]
    conn.close()
    return prices
