"""
data_preprocessing.py
---------------------
Handles loading and cleaning of raw real estate data.
"""

import pandas as pd
from src.utils import log


class DataPreprocessor:
    """Cleans and prepares raw data for modeling."""

    @staticmethod
    def load_data(filepath: str) -> pd.DataFrame:
        log(f"Loading data from {filepath}")
        df = pd.read_csv(filepath)
        log(f"Loaded {len(df)} records.")
        return df

    @staticmethod
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        log("Cleaning data ...")
        df = df.dropna(subset=["price", "sqft", "bedrooms", "bathrooms", "year_built", "location"])
        df = df[df["price"] > 0]
        df = df[df["sqft"] > 200]  # filter unrealistic data
        log(f"Cleaned data: {len(df)} valid records remaining.")
        return df

