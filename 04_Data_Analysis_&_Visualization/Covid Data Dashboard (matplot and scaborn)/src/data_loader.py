"""
data_loader.py
---------------
Responsible for loading COVID-19 dataset from local CSV or remote source.
Uses pandas for structured data handling.
"""

import pandas as pd
from utils.logger import Logger


class DataLoader:
    """Handles loading of COVID-19 data from CSV files."""

    @staticmethod
    def load_data(filepath: str) -> pd.DataFrame:
        """
        Loads COVID-19 data from a CSV file.
        :param filepath: Path to CSV file containing COVID-19 data.
        :return: pandas DataFrame
        """
        Logger.log(f"Loading data from {filepath} ...")
        try:
            df = pd.read_csv(filepath, parse_dates=["date"])
            Logger.log(f"Successfully loaded {len(df)} records.")
            return df
        except Exception as e:
            Logger.log(f"Error loading data: {e}")
            raise

