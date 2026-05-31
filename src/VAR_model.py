#Import libraries
import pandas as pd
import numpy as np

#Load and preprocess data
df = pd.read_csv("./data/processed/final_dataset.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

#Log-transform housing price
df['ln_housing_price'] = np.log(df['housing_price'])

df.head()

#Visualize the data
import matplotlib.pyplot as plt

df.plot(subplots=True, figsize=(10,6))
plt.show()

#ADF test for stationarity
from statsmodels.tsa.stattools import adfuller
def adf_test(series, name):
    result = adfuller(series)
    print(f"ADF Test for {name}")
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    print("Critical Values:")
    for key, value in result[4].items():
        print(f"   {key}: {value}")
    print("--------------------------")

#ADF test (Level data)
adf_test(df['inflation'], 'Inflation')
adf_test(df['interest_rate'], 'Interest Rate')
adf_test(df['ln_housing_price'], 'Log Housing Price')

#Differencing the data to achieve stationarity
df_diff = df[['inflation', 'interest_rate', 'ln_housing_price']].diff().dropna()
df_diff.plot(subplots=True, figsize=(10,6))
plt.suptitle("Differenced Series")
plt.show()

df_diff.head()

#ADF test (Differenced data)
adf_test(df_diff['inflation'], 'Inflation (diff)')
adf_test(df_diff['interest_rate'], 'Interest Rate (diff)')
adf_test(df_diff['ln_housing_price'], 'Diff Log Housing Price')

#Var Modeling
from statsmodels.tsa.api import VAR

final_df = df_diff[['inflation', 'interest_rate', 'ln_housing_price']]

#Lag selection
model = VAR(final_df)
lag_selection = model.select_order(maxlags=8)
print(lag_selection.summary())

#Fit model using selected lag
optimal_lag = lag_selection.aic
results = model.fit(optimal_lag)

#Impulse response functions
irf = results.irf(12)
irf.plot(orth=False)

#Granger Causality test
from statsmodels.tsa.stattools import grangercausalitytests
print("\n=== Granger Causality Tests ===")
# Inflation → Interest Rate
print("\nInflation causes Interest Rate?")
grangercausalitytests(final_df[['interest_rate', 'inflation']], maxlag=4)
#Interest Rate → Inflation
print("\nInterest Rate causes Inflation?")
grangercausalitytests(final_df[['inflation', 'interest_rate']], maxlag=4)
# Interest Rate → Housing Price
print("\nInterest Rate causes Housing Price?")
grangercausalitytests(final_df[['ln_housing_price', 'interest_rate']], maxlag=4)
# Inflation → Housing Price
print("\nInflation causes Housing Price?")
grangercausalitytests(final_df[['ln_housing_price', 'inflation']], maxlag=4)


print(results.summary())