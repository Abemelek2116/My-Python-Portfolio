"""
transform.py
-------------
Performs data cleaning, type conversion, and feature engineering.
"""

import pandas as pd
from utils.logger import Logger


class Transformer:
    """Cleans and transforms raw data for consistency."""

    @staticmethod
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        Logger.log("Cleaning data ...")

        # Drop missing or invalid rows
        df = df.dropna(subset=["region", "product", "revenue", "quantity"])

        # Ensure correct data types
        df["revenue"] = df["revenue"].astype(float)
        df["quantity"] = df["quantity"].astype(int)

        # Add derived metric: revenue per item
        df["revenue_per_item"] = df["revenue"] / df["quantity"]

        Logger.log("Data cleaning completed.")
        return df

    @staticmethod
    def aggregate_data(df: pd.DataFrame) -> pd.DataFrame:
        """Aggregates data by region and product."""
        Logger.log("Aggregating data by region and product ...")
        agg_df = df.groupby(["region", "product"], as_index=False).agg(
            total_revenue=("revenue", "sum"),
            total_quantity=("quantity", "sum"),
            avg_revenue_per_item=("revenue_per_item", "mean"),
        )
        Logger.log("Aggregation completed.")
        return agg_df

