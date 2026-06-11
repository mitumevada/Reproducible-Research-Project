import pandas as pd
import numpy as np


class DataLoader:

    def load_data(self, file_path):

        df = pd.read_csv(file_path)
        return df

    def preprocess_data(self, df):
        df['date'] = pd.to_datetime(df['date'])

        df = df.set_index('date')

        df = df.asfreq('QS-JAN')

        df['ln_housing_price'] = np.log(
            df['housing_price']
        )

        return df