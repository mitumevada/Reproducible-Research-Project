class IRFAnalysis:

    def __init__(self, var_results):

        self.var_results = var_results

    def plot(self):

        irf = self.var_results.irf(12)

        return irf.plot(orth=False)