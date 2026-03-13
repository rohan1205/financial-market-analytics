# Data Directory Structure

This directory should contain your original stock and ETF data files.

## Required Files:

### dataset/stocks/
- Place individual stock CSV files here (one per stock)
- Each CSV should contain: Date, Open, High, Low, Close, Volume
- File naming: [TICKER].csv (e.g., AAPL.csv, MSFT.csv)

### dataset/etfs/
- Place ETF CSV files here
- Same format as stock files
- File naming: [ETF_SYMBOL].csv (e.g., SPY.csv, QQQ.csv)

### dataset/symbols_valid_meta.csv
- Metadata file with valid stock symbols
- Should contain symbol information and validation data

## To restore your data:

1. If you have backups, restore the CSV files to these directories
2. If you need to re-download, check your original data sources
3. Once files are in place, run the processing scripts in order:
   - python scripts/combine_stocks.py
   - python scripts/data_cleaning.py
   - python scripts/feature_engineering.py
   - python scripts/analytics.py

## Note:
The original data files were permanently deleted. Please restore them from backups or re-download from your data provider.