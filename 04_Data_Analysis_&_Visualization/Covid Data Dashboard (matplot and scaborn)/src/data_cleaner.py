"""
data_cleaner.py
---------------
Performs data preprocessing: cleaning, handling missing values,
and adding derived features such as rolling averages.
"""

import pandas as pd
from utils.logger import Logger


class DataCleaner:
    """Cleans and preprocesses COVID-19 dataset."""

    @staticmethod
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans raw data by handling missing values and adding useful columns.
        :param df: Raw DataFrame
        :return: Cleaned DataFrame
        """
        Logger.log("Cleaning data ...")
        df = df.dropna(subset=["location", "date", "total_cases", "total_deaths"], how="any")

        # Fill vaccination data with zeros if missing
        df["total_vaccinations"] = df["total_vaccinations"].fillna(0)

        # Compute daily new cases and deaths
        df = df.sort_values(["location", "date"])
        df["new_cases"] = df.groupby("location")["total_cases"].diff().fillna(0)
        df["new_deaths"] = df.groupby("location")["total_deaths"].diff().fillna(0)

        # Rolling average for trend smoothing
        df["7_day_avg_cases"] = df.groupby("location")["new_cases"].transform(lambda x: x.rolling(7).mean())

        Logger.log("Data cleaning completed.")
        return df

