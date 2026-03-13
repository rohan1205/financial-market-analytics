import pandas as pd
import os

# path where all stock csv files exist
stocks_path = "dataset/stocks"

all_data = []

# loop through all files
for file in os.listdir(stocks_path):

    if file.endswith(".csv"):

        file_path = os.path.join(stocks_path, file)

        df = pd.read_csv(file_path)

        # add ticker name from file name
        ticker = file.replace(".csv", "")
        df["Ticker"] = ticker

        all_data.append(df)

# combine all stock datasets
combined_df = pd.concat(all_data, ignore_index=True)

print("Total rows:", len(combined_df))

# save combined dataset
combined_df.to_csv("data/raw_stock_data.csv", index=False)

print("Dataset created successfully!")