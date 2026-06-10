from statsmodels.tsa.api import VAR

class VARAnalysis:

    def __init__(self, data):

        self.data = data

        self.model = None

        self.results = None

    def select_lag(self):

        self.model = VAR(self.data)

        return self.model.select_order(maxlags=8)

    def fit(self):

        lag_selection = self.select_lag()

        optimal_lag = lag_selection.aic

        self.results = self.model.fit(optimal_lag)

        return self.results