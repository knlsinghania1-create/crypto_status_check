import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "data/crypto_data.db"

def get_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM crypto_prices", conn)
    conn.close()
    return df

def main():
    st.title("Crypto Price Dashboard")

    df = get_data()

    if df.empty:
        st.write("No data available yet. Run the ingestion script first.")
        return

    # Show latest prices by coin (latest timestamp)
    latest_time = df['timestamp'].max()
    st.subheader(f"Latest prices (Timestamp: {latest_time})")
    latest_df = df[df['timestamp'] == latest_time][['symbol', 'price_usd', 'market_cap_usd', 'change_24h']]
    st.dataframe(latest_df.set_index('symbol'))

    # Plot price trend for selected coin
    st.subheader("Price Trends")
    coins = df['symbol'].unique()
    coin_choice = st.selectbox("Select a coin", coins)

    coin_df = df[df['symbol'] == coin_choice].sort_values('timestamp')
    coin_df['timestamp'] = pd.to_datetime(coin_df['timestamp'])

    plt.figure(figsize=(10, 4))
    plt.plot(coin_df['timestamp'], coin_df['price_usd'], marker='o')
    plt.title(f"Price Trend for {coin_choice}")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    st.pyplot(plt)

if __name__ == "__main__":
    main()
