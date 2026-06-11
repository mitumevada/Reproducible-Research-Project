from statsmodels.tsa.stattools import grangercausalitytests
import pandas as pd
import warnings


class GrangerAnalysis:

    def __init__(self, data):
        self.data = data

    def run(self, max_lag):

        pairs = [
            ('inflation', 'ln_housing_price'),
            ('interest_rate', 'ln_housing_price'),
            ('inflation', 'interest_rate'),
            ('interest_rate', 'inflation')
        ]

        granger_results = []

        for cause, target in pairs:

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")

                test = grangercausalitytests(
                    self.data[[target, cause]],
                    maxlag=max_lag,
                    verbose=False
                )

            p_value = test[4][0]['ssr_chi2test'][1]

            granger_results.append({
                "Cause": cause,
                "Target": target,
                "Lag": 4,
                "p-value": round(p_value, 4)
            })

        granger_table = pd.DataFrame(granger_results)

        return granger_table