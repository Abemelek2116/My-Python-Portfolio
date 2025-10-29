"""
visualizer.py
--------------
Generates visualizations for stock prices, moving averages,
and daily returns using matplotlib and seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from src.utils import log


class Visualizer:
    """Handles visualizations for stock analysis."""

    @staticmethod
    def plot_price_trend(df, ticker, save_path):
        log("Plotting stock price trend ...")
        plt.figure(figsize=(10, 6))
        plt.plot(df["Date"], df["Close"], label="Close", linewidth=1.8)
        plt.plot(df["Date"], df["MA20"], label="MA 20", linestyle="--")
        plt.plot(df["Date"], df["MA50"], label="MA 50", linestyle="--")
        plt.title(f"{ticker} Price Trend with Moving Averages")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        log(f"Price trend plot saved to {save_path}")

    @staticmethod
    def plot_returns(df, save_path):
        log("Plotting daily returns ...")
        plt.figure(figsize=(10, 5))
        sns.histplot(df["Daily Return"].dropna(), bins=50, color="royalblue", kde=True)
        plt.title("Distribution of Daily Returns")
        plt.xlabel("Daily Return")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        log(f"Daily returns plot saved to {save_path}")

