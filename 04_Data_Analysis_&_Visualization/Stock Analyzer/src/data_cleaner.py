"""
data_cleaner.py
---------------
Cleans and prepares stock data for analysis.
"""

import pandas as pd
from src.utils import log


class DataCleaner:
    """Cleans and preprocesses raw stock data."""

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        log("Cleaning stock data ...")
        df = df.dropna(subset=["Close"])
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date").reset_index(drop=True)
        log("Data cleaning completed.")
        return df

