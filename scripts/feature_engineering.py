import pandas as pd

print("Loading cleaned dataset...")

df = pd.read_csv("data/cleaned_stock_data.csv")

print("Dataset Shape:", df.shape)

# Calculate Daily Return
df["Daily_Return"] = df.groupby("Ticker")["Close"].pct_change()

# Moving Average (20 days)
df["MA20"] = df.groupby("Ticker")["Close"].rolling(window=20).mean().reset_index(level=0, drop=True)

# Volatility (20 day rolling std)
df["Volatility"] = df.groupby("Ticker")["Daily_Return"].rolling(window=20).std().reset_index(level=0, drop=True)

# RSI Calculation
delta = df.groupby("Ticker")["Close"].diff()

gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)

avg_gain = gain.groupby(df["Ticker"]).rolling(window=14).mean().reset_index(level=0, drop=True)
avg_loss = loss.groupby(df["Ticker"]).rolling(window=14).mean().reset_index(level=0, drop=True)

rs = avg_gain / avg_loss

df["RSI"] = 100 - (100 / (1 + rs))

print("Feature engineering completed.")

# Save dataset
df.to_csv("data/engineered_stock_data.csv", index=False)

print("Engineered dataset saved successfully!")