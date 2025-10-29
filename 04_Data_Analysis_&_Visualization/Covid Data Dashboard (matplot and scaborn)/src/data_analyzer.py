"""
data_analyzer.py
----------------
Performs analytical computations such as identifying top affected countries,
growth rates, and correlation analysis.
"""

import pandas as pd
from utils.logger import Logger


class DataAnalyzer:
    """Performs exploratory analysis and computes summary metrics."""

    @staticmethod
    def top_countries(df: pd.DataFrame, metric: str = "total_cases", n: int = 10) -> pd.DataFrame:
        """
        Returns the top N countries by a specified metric.
        """
        Logger.log(f"Computing top {n} countries by {metric} ...")
        top_df = (
            df.groupby("location")[metric]
            .max()
            .sort_values(ascending=False)
            .head(n)
            .reset_index()
        )
        return top_df

    @staticmethod
    def correlation_analysis(df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates correlation between COVID-19 metrics.
        """
        Logger.log("Performing correlation analysis ...")
        subset = df[["total_cases", "total_deaths", "total_vaccinations"]]
        corr = subset.corr()
        Logger.log("Correlation analysis completed.")
        return corr

