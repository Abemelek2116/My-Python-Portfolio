"""
visualizer.py
--------------
Generates visualizations for weather trends using Matplotlib and Seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from src.utils import log


class Visualizer:
    """Handles all visualizations for weather data."""

    @staticmethod
    def plot_temperature_trend(df, save_path):
        log("Plotting temperature trend over time ...")
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x="Date", y="Temperature", color="tomato")
        plt.title("Daily Temperature Trend")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        log(f"Temperature trend saved to {save_path}")

    @staticmethod
    def plot_monthly_rainfall(df, save_path):
        log("Plotting monthly rainfall ...")
        monthly_rainfall = df.groupby("Month")["Rainfall"].sum()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=monthly_rainfall.index, y=monthly_rainfall.values, color="skyblue")
        plt.title("Total Monthly Rainfall")
        plt.xlabel("Month")
        plt.ylabel("Rainfall (mm)")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        log(f"Monthly rainfall plot saved to {save_path}")

    @staticmethod
    def plot_humidity_distribution(df, save_path):
        log("Plotting humidity distribution ...")
        plt.figure(figsize=(10, 6))
        sns.histplot(df["Humidity"], bins=40, kde=True, color="green")
        plt.title("Humidity Distribution")
        plt.xlabel("Humidity (%)")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        log(f"Humidity distribution plot saved to {save_path}")

