"""
stock_analyzer.py
-----------------
Performs stock analysis such as moving averages,
daily returns, and volatility.
"""

import pandas as pd
from src.utils import log


class StockAnalyzer:
    """Performs financial computations and trend analysis."""

    @staticmethod
    def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
        log("Calculating moving averages and daily returns ...")

        df["Daily Return"] = df["Close"].pct_change()
        df["MA20"] = df["Close"].rolling(window=20).mean()
        df["MA50"] = df["Close"].rolling(window=50).mean()
        df["Volatility"] = df["Daily Return"].rolling(window=20).std()

        log("Indicators added successfully.")
        return df

    @staticmethod
    def summary_stats(df: pd.DataFrame) -> pd.DataFrame:
        """Generates summary statistics."""
        log("Generating summary statistics ...")
        stats = {
            "Mean Return": df["Daily Return"].mean(),
            "Volatility": df["Daily Return"].std(),
            "Max Close": df["Close"].max(),
            "Min Close": df["Close"].min(),
            "Final Close": df["Close"].iloc[-1]
        }
        summary_df = pd.DataFrame(stats, index=[0])
        log("Summary stats generated.")
        return summary_df

