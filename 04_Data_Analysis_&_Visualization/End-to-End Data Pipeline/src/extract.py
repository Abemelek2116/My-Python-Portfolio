"""
extract.py
-----------
Extracts data from different sources such as CSV and simulated API.
"""

import pandas as pd
from utils.logger import Logger
import requests


class Extractor:
    """Handles data extraction from multiple sources."""

    @staticmethod
    def from_csv(filepath: str) -> pd.DataFrame:
        Logger.log(f"Extracting data from CSV: {filepath}")
        df = pd.read_csv(filepath)
        Logger.log(f"Loaded {len(df)} records from CSV.")
        return df

    @staticmethod
    def from_api(url: str) -> pd.DataFrame:
        """
        Simulates an API extraction (dummy for demonstration).
        """
        Logger.log(f"Fetching data from API: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            Logger.log(f"Extracted {len(df)} records from API.")
            return df
        except Exception as e:
            Logger.log(f"API extraction failed: {e}")
            return pd.DataFrame()

