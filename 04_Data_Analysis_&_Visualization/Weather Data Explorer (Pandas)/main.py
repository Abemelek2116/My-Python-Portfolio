"""
main.py
--------
Entry point for the Weather Data Explorer project.
"""

from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.analyzer import WeatherAnalyzer
from src.visualizer import Visualizer
from src.utils import log, ensure_dir

def main():
    log("=== Starting Weather Data Explorer ===")

    # Step 1: Ensure output directories
    ensure_dir("outputs/figures")
    ensure_dir("outputs/reports")

    # Step 2: Load Data
    df = DataLoader.load_data("data/raw/weather_data.csv")

    # Step 3: Clean Data
    df_clean = DataCleaner.clean(df)

    # Step 4: Analyze
    df_analysis = WeatherAnalyzer.add_derived_columns(df_clean)
    summary = WeatherAnalyzer.summary_statistics(df_analysis)
    summary.to_csv("outputs/reports/weather_summary.csv")

    # Step 5: Visualize
    Visualizer.plot_temperature_trend(df_analysis, "outputs/figures/temperature_trend.png")
    Visualizer.plot_monthly_rainfall(df_analysis, "outputs/figures/monthly_rainfall.png")
    Visualizer.plot_humidity_distribution(df_analysis, "outputs/figures/humidity_distribution.png")

    log("=== Weather Data Analysis Completed Successfully ===")

if __name__ == "__main__":
    main()

