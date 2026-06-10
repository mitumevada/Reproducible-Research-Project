import pandas as pd


class DataPipeline:

    def __init__(self):

        self.inflation = None
        self.rate = None
        self.housing = None
        self.df = None

    def load_data(self):

        self.inflation = pd.read_csv(
            "data/raw/inflation.csv"
        )

        self.rate = pd.read_csv(
            "data/raw/interest_rate.csv"
        )

        self.housing = pd.read_csv(
            "data/raw/housing_price.csv"
        )

    def clean_data(self):

        self.inflation = self.inflation.rename(
            columns={
                "TIME_PERIOD": "date",
                "OBS_VALUE": "inflation"
            }
        )

        self.rate = self.rate.rename(
            columns={
                "TIME_PERIOD": "date",
                "OBS_VALUE": "interest_rate"
            }
        )

        self.housing = self.housing.rename(
            columns={
                "TIME_PERIOD": "date",
                "OBS_VALUE": "housing_price"
            }
        )

        self.inflation = self.inflation[
            ["date", "inflation"]
        ]

        self.rate = self.rate[
            ["date", "interest_rate"]
        ]

        self.housing = self.housing[
            ["date", "housing_price"]
        ]

    def convert_dates(self):

        self.inflation["date"] = pd.to_datetime(
            self.inflation["date"]
        )

        self.rate["date"] = pd.to_datetime(
            self.rate["date"]
        )

        self.housing["date"] = pd.to_datetime(
            self.housing["date"]
        )

    def resample_data(self):

        self.inflation = (
            self.inflation
            .set_index("date")
            .resample("QS")
            .mean()
            .reset_index()
        )

        self.rate = (
            self.rate
            .set_index("date")
            .resample("QS")
            .mean()
            .reset_index()
        )

    def merge_data(self):

        self.df = self.inflation.merge(
            self.rate,
            on="date"
        )

        self.df = self.df.merge(
            self.housing,
            on="date"
        )

        self.df = self.df.dropna()

        self.df = self.df.sort_values(
            "date"
        )

    def save_data(self):

        self.df.to_csv(
            "data/processed/final_dataset.csv",
            index=False
        )

    def run(self):

        self.load_data()

        self.clean_data()

        self.convert_dates()

        self.resample_data()

        self.merge_data()

        self.save_data()

        return self.df
    
if __name__ == "__main__":

    pipeline = DataPipeline()

    pipeline.run()
