#!/usr/bin/env python3
"""
Data Restoration Script
Downloads sample stock data to restore your dataset
"""

import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta

def download_sample_stocks():
    """Download sample stock data for testing"""

    # Create directories if they don't exist
    os.makedirs("dataset/stocks", exist_ok=True)
    os.makedirs("dataset/etfs", exist_ok=True)

    # Sample stocks (tech companies)
    stocks = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA',
        'NVDA', 'META', 'NFLX', 'CRM', 'ORCL'
    ]

    # Sample ETFs
    etfs = [
        'SPY', 'QQQ', 'VTI', 'VEA', 'VWO',
        'BND', 'VNQ', 'VIG', 'VUG', 'VTV'
    ]

    # Download last 2 years of data
    start_date = datetime.now() - timedelta(days=365*2)

    print("Downloading sample stock data...")

    # Download stocks
    for ticker in stocks:
        try:
            print(f"Downloading {ticker}...")
            stock = yf.Ticker(ticker)
            data = stock.history(start=start_date)

            if not data.empty:
                data.to_csv(f"dataset/stocks/{ticker}.csv")
                print(f"✓ Saved {ticker}.csv")
            else:
                print(f"✗ No data for {ticker}")

        except Exception as e:
            print(f"✗ Error downloading {ticker}: {e}")

    print("\nDownloading sample ETF data...")

    # Download ETFs
    for ticker in etfs:
        try:
            print(f"Downloading {ticker}...")
            etf = yf.Ticker(ticker)
            data = etf.history(start=start_date)

            if not data.empty:
                data.to_csv(f"dataset/etfs/{ticker}.csv")
                print(f"✓ Saved {ticker}.csv")
            else:
                print(f"✗ No data for {ticker}")

        except Exception as e:
            print(f"✗ Error downloading {ticker}: {e}")

    print("\nDownload complete!")
    print(f"Check dataset/stocks/ and dataset/etfs/ for the CSV files")

if __name__ == "__main__":
    download_sample_stocks()