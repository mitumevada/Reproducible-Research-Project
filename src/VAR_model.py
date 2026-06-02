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
var_results = model.fit(optimal_lag)

print(var_results.summary())

#Impulse response functions
irf = var_results.irf(12)
irf.plot(orth=False)

#Granger Causality test
from statsmodels.tsa.stattools import grangercausalitytests
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

pairs = [
    ('inflation', 'ln_housing_price'),
    ('interest_rate', 'ln_housing_price'),
    ('inflation', 'interest_rate'),
    ('interest_rate', 'inflation')
]

granger_results = []

for cause, target in pairs:

    test = grangercausalitytests(
        df_diff[[target, cause]],
        maxlag=4,
        verbose=False
    )

    p_value = test[4][0]['ssr_chi2test'][1]

    granger_results.append({
        'Cause': cause,
        'Target': target,
        'Lag': 4,
        'p-value': round(p_value, 4)
    })

granger_table = pd.DataFrame(granger_results)

print(granger_table)


print("VAR model completed successfully.")
