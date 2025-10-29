"""
visualize.py
-------------
Generates summary visualizations using matplotlib and seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils.logger import Logger


class Visualizer:
    """Generates data visualizations."""

    @staticmethod
    def plot_revenue_by_region(df: pd.DataFrame, save_path: str) -> None:
        Logger.log("Visualizing revenue by region ...")
        plt.figure(figsize=(8, 6))
        sns.barplot(x="Total Revenue", y="Region", data=df, palette="viridis")
        plt.title("Total Revenue by Region")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        Logger.log(f"Plot saved to {save_path}")

