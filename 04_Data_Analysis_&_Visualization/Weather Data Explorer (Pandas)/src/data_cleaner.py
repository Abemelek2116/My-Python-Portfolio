"""
data_cleaner.py
---------------
Cleans and prepares weather data for analysis.
"""

import pandas as pd
from src.utils import log


class DataCleaner:
    """Cleans raw weather data."""

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        log("Cleaning weather data ...")

        # Convert Date column to datetime
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        # Drop missing or invalid rows
        df = df.dropna(subset=["Date", "Temperature", "Humidity", "Rainfall"])

        # Remove negative values (invalid)
        df = df[(df["Temperature"] >= -30) & (df["Temperature"] <= 60)]
        df = df[df["Rainfall"] >= 0]
        df = df[df["Humidity"].between(0, 100)]

        df = df.sort_values("Date").reset_index(drop=True)
        log("Data cleaning completed successfully.")
        return df

