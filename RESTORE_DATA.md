

The original CSV files were deleted using `Remove-Item -Force` which bypasses the Recycle Bin. They cannot be recovered from the filesystem.

## 📊 What Files You Need

### 1. Individual Stock Data Files
**Location:** `dataset/stocks/`
**Format:** One CSV file per stock (e.g., `AAPL.csv`, `MSFT.csv`, `GOOGL.csv`)
**Required Columns:** Date, Open, High, Low, Close, Volume, Adj Close (optional)

### 2. ETF Data Files
**Location:** `dataset/etfs/`
**Format:** One CSV file per ETF (e.g., `SPY.csv`, `QQQ.csv`, `VTI.csv`)
**Required Columns:** Same as stock files

### 3. Symbols Metadata
**Location:** `dataset/symbols_valid_meta.csv`
**Purpose:** Contains valid stock symbols and metadata

## 🔄 How to Get the Data Back

### Option 1: Restore from Backup
If you have backups, restore the files to their original locations:
- `dataset/stocks/*.csv` → `dataset/stocks/`
- `dataset/etfs/*.csv` → `dataset/etfs/`
- `dataset/symbols_valid_meta.csv` → `dataset/`

### Option 2: Download from Financial Data Providers

#### Yahoo Finance (Free)
```python
import yfinance as yf
import pandas as pd

# Download stock data
stock = yf.Ticker("AAPL")
data = stock.history(period="max")
data.to_csv("dataset/stocks/AAPL.csv")
```

#### Alpha Vantage (Free API)
- Sign up: https://www.alphavantage.co/
- API documentation: https://www.alphavantage.co/documentation/

#### Other Free Sources:
- **IEX Cloud**: https://iexcloud.io/
- **Twelve Data**: https://twelvedata.com/
- **Polygon.io**: https://polygon.io/

### Option 3: Use Sample Data for Testing
For testing purposes, you can download sample data:

```python
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Download sample stocks
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
start_date = datetime.now() - timedelta(days=365*2)  # 2 years

for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date)
        data.to_csv(f"dataset/stocks/{ticker}.csv")
        print(f"Downloaded {ticker}")
    except Exception as e:
        print(f"Error downloading {ticker}: {e}")
```

## 🛠️ Next Steps After Restoring Data

Once you have the CSV files in place, run these scripts in order:

```bash
# 1. Combine all individual stock CSVs
python scripts/combine_stocks.py

# 2. Clean the combined data
python scripts/data_cleaning.py

# 3. Add technical indicators
python scripts/feature_engineering.py

# 4. Generate analytics
python scripts/analytics.py
```

## 📝 Data Format Requirements

Each CSV file should have these columns:
- **Date**: YYYY-MM-DD format
- **Open**: Opening price
- **High**: Highest price
- **Low**: Lowest price
- **Close**: Closing price
- **Volume**: Trading volume
- **Adj Close**: Adjusted closing price (optional)

Example CSV structure:
```csv
Date,Open,High,Low,Close,Volume
2023-01-01,150.00,155.00,149.00,154.00,1000000
2023-01-02,154.00,158.00,153.00,157.00,1200000
```

## 💡 Recommendation

Start with a small dataset (5-10 stocks) to test your pipeline, then scale up to more stocks as needed. This will help you verify everything works before downloading large amounts of data.
