import pandas as pd

print("Loading engineered dataset...")

# Load dataset
df = pd.read_csv("data/engineered_stock_data.csv")

print("Dataset shape:", df.shape)

# Remove rows where indicators are missing
df = df.dropna(subset=["Daily_Return", "Volatility", "RSI"])

print("Dataset after removing missing values:", df.shape)


# ---------------------------------------------------
# Top 10 Stocks by Average Daily Return
# ---------------------------------------------------

top_returns = (
    df.groupby("Ticker")["Daily_Return"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Stocks by Average Daily Return:")
print(top_returns)

top_returns.to_csv("data/top10_returns.csv")


# ---------------------------------------------------
# Top 10 Most Volatile Stocks
# ---------------------------------------------------

top_volatility = (
    df.groupby("Ticker")["Volatility"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Most Volatile Stocks:")
print(top_volatility)

top_volatility.to_csv("data/top10_volatility.csv")


# ---------------------------------------------------
# Overbought Stocks (RSI > 70)
# ---------------------------------------------------

overbought = df[df["RSI"] > 70][["Date", "Ticker", "RSI"]]

print("\nOverbought stocks found:", len(overbought))

overbought.to_csv("data/overbought_stocks.csv", index=False)


# ---------------------------------------------------
# Oversold Stocks (RSI < 30)
# ---------------------------------------------------

oversold = df[df["RSI"] < 30][["Date", "Ticker", "RSI"]]

print("\nOversold stocks found:", len(oversold))

oversold.to_csv("data/oversold_stocks.csv", index=False)


print("\nAll analytics files created successfully!")