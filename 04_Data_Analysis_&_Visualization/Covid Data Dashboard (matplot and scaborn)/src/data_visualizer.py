"""
data_visualizer.py
------------------
Generates charts and visualizations using matplotlib and seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils.logger import Logger


class DataVisualizer:
    """Handles all data visualization tasks."""

    @staticmethod
    def plot_top_countries(top_df: pd.DataFrame, metric: str, save_path: str) -> None:
        """
        Bar chart of top countries by a given metric.
        """
        Logger.log(f"Creating bar chart for top countries by {metric} ...")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=metric, y="location", data=top_df, palette="Reds_r")
        plt.title(f"Top 10 Countries by {metric.replace('_', ' ').title()}")
        plt.xlabel(metric.replace("_", " ").title())
        plt.ylabel("Country")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        Logger.log(f"Chart saved to {save_path}")

    @staticmethod
    def plot_trend(df: pd.DataFrame, country: str, save_path: str) -> None:
        """
        Line chart of 7-day average cases for a given country.
        """
        Logger.log(f"Plotting case trend for {country} ...")
        country_df = df[df["location"] == country]
        plt.figure(figsize=(10, 6))
        plt.plot(country_df["date"], country_df["7_day_avg_cases"], label="7-Day Average", color="blue")
        plt.title(f"COVID-19 Trend: {country}")
        plt.xlabel("Date")
        plt.ylabel("7-Day Avg Cases")
        plt.legend()
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        Logger.log(f"Trend chart saved to {save_path}")

    @staticmethod
    def plot_correlation(corr_df: pd.DataFrame, save_path: str) -> None:
        """
        Heatmap of correlation matrix.
        """
        Logger.log("Plotting correlation heatmap ...")
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_df, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Between COVID-19 Metrics")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        Logger.log(f"Heatmap saved to {save_path}")

