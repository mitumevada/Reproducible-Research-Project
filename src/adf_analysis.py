# adf_analysis.py

from statsmodels.tsa.stattools import adfuller

class ADFAnalysis:

    def adf_test(self, series):

        result = adfuller(series)

        return {
            "ADF Statistic": result[0],
            "p-value": result[1]
        }

    def level_test(self, df):

        return {
            "inflation":
                self.adf_test(df["inflation"]),

            "interest_rate":
                self.adf_test(df["interest_rate"]),

            "ln_housing_price":
                self.adf_test(df["ln_housing_price"])
        }

    def difference_test(self, df_diff):

        return {
            "inflation":
                self.adf_test(df_diff["inflation"]),

            "interest_rate":
                self.adf_test(df_diff["interest_rate"]),

            "ln_housing_price":
                self.adf_test(df_diff["ln_housing_price"])
        }