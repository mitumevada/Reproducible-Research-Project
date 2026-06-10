from statsmodels.tsa.stattools import grangercausalitytests
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

class GrangerAnalysis:

    def __init__(self, data):

        self.data = data

    def run(self):

        pairs = [
            ('inflation', 'ln_housing_price'),
            ('interest_rate', 'ln_housing_price'),
            ('inflation', 'interest_rate'),
            ('interest_rate', 'inflation')
        ]

        granger_results = []

        for cause, target in pairs:

            test = grangercausalitytests(
                self.data[[target, cause]],
                maxlag=4,
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