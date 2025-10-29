"""
data_loader.py
---------------
Handles loading of weather data from CSV files.
"""

import pandas as pd
from src.utils import log


class DataLoader:
    """Loads raw weather data from a CSV file."""

    @staticmethod
    def load_data(filepath: str) -> pd.DataFrame:
        log(f"Loading data from {filepath} ...")
        df = pd.read_csv(filepath)
        log(f"Loaded {len(df)} records successfully.")
        return df

