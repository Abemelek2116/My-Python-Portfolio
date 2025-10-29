"""
analyzer.py
-----------
Performs statistical analysis on weather data.
"""

import pandas as pd
from src.utils import log


class WeatherAnalyzer:
    """Performs analysis on weather data."""

    @staticmethod
    def add_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
        log("Adding derived columns for analysis ...")
        df["Month"] = df["Date"].dt.month
        df["Year"] = df["Date"].dt.year
        df["DayOfWeek"] = df["Date"].dt.day_name()
        log("Derived columns added successfully.")
        return df

    @staticmethod
    def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
        """Generates summary statistics for temperature, humidity, and rainfall."""
        log("Generating summary statistics ...")
        summary = df[["Temperature", "Humidity", "Rainfall"]].describe().T
        summary["Variance"] = df[["Temperature", "Humidity", "Rainfall"]].var()
        log("Summary statistics computed.")
        return summary

