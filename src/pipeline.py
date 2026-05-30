# Step 1: Data Loading
# Load raw datasets into pandas DataFrames

import pandas as pd

inflation = pd.read_csv("data/raw/inflation.csv")
rate = pd.read_csv("data/raw/interest_rate.csv")
housing = pd.read_csv("data/raw/housing_price.csv")

print("=== Inflation ===")
print(inflation.head())
print(inflation.columns)

print("\n=== interest_rate ===")
print(rate.head())
print(rate.columns)

print("\n=== Housing ===")
print(housing.head())
print(housing.columns)

# Step 2: Data Cleaning and Formatting
# Clean data and standardize column names and structure

# Rename Columns for consistency

inflation = inflation.rename(columns={
    "TIME_PERIOD": "date",
    "OBS_VALUE": "inflation"
})

rate = rate.rename(columns={
    "TIME_PERIOD": "date",
    "OBS_VALUE": "interest_rate"
})

housing = housing.rename(columns={
    "TIME_PERIOD": "date",
    "OBS_VALUE": "housing_price"
})

# Select Relevant Columns

inflation = inflation[['date', 'inflation']]
rate = rate [['date', 'interest_rate']]
housing = housing [['date', 'housing_price']]

# Convert Date Format

inflation['date'] = pd.to_datetime(inflation['date'])
rate['date'] = pd.to_datetime(rate['date'])
housing['date'] = pd.to_datetime(housing['date'])

# Sort Data by Date

inflation = inflation.sort_values('date')
rate = rate.sort_values('date')
housing = housing.sort_values('date')

# Inspect Cleaned Data

print(inflation.head())
print(rate.head())
print(housing.head())

# Step 3: Frequency Alignment
# Convert inflation and interest rate data to quarterly frequency to match other datasets

inflation = inflation.set_index('date')
inflation = inflation.resample('QS').mean()
inflation = inflation.reset_index()

rate = rate.set_index('date')
rate = rate.resample('QS').mean()
rate = rate.reset_index()

# Step 4: Standardize Date Format
# Convert all date columns to a consistent quarterly format to ensure proper alignment across datasets.

def standardize_date_format(df, col='date'):
    df[col] = pd.to_datetime(df[col])
    df[col] = df[col].dt.to_period('M').dt.to_timestamp()
    return df

inflation = standardize_date_format(inflation)
rate = standardize_date_format(rate)
housing = standardize_date_format(housing)

# Step 5: Merge Datasets
# Merge all datasets into a single time series based on date

df = inflation.merge(rate, on='date')  ## Merge Inflation and Interest Rate
df = df.merge(housing, on='date')      ## Merge Housing Data

print(df.head(10))   ## Inspect Merged Data
df = df.dropna()     ## Drop Missing Values

df = df.sort_values('date')   ## Sort Data

print(df.head())
print(df.tail())
print(df.shape)

# Step 6: Save Final Dataset

df.to_csv("data/processed/final_dataset.csv", index=False)

# Step 7: Raw Data Visualization for Sanity Check

import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

plt.plot(df['date'], df['inflation'], label='Inflation')
plt.plot(df['date'], df['interest_rate'], label='Interest Rate')
plt.plot(df['date'], df['housing_price'], label='Housing Price')

plt.title("Raw Data Overview (Sanity Check)")
plt.xlabel("Date")
plt.ylabel("Value")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Step 8: Pipeline Entry Point

def run_pipeline():
    print("Running pipeline...")

if __name__ == "__main__":
    run_pipeline()

