# 📊 Crypto Status Check Dashboard

A simple Python-based Streamlit dashboard that fetches real-time cryptocurrency data using the CoinGecko API, stores it in a SQLite database, and visualizes key metrics like price, market cap, and daily changes.

## 🔧 Features

- Real-time crypto price ingestion using CoinGecko API
- Data stored in SQLite (`data/crypto_data.db`)
- Interactive Streamlit dashboard to view prices and trends
- Modular codebase (Ingestion, DB handler, Dashboard)
- Lightweight and runs locally

## 🧱 Project Structure

crypto_data_pipeline/
│
├── ingest.py # Fetches data from CoinGecko and writes to DB
├── db_handler.py # Handles SQLite DB operations
├── dashboard.py # Streamlit app
├── data/crypto_data.db # SQLite DB storing prices
└── README.md # You're reading this 🙂
