import pandas as pd

print("Loading dataset...")

df = pd.read_csv("data/raw_stock_data.csv")

print("Initial Shape:", df.shape)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Sort by stock and date
df = df.sort_values(by=["Ticker", "Date"])

print("Cleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv("data/cleaned_stock_data.csv", index=False)

print("Cleaned dataset saved successfully!")