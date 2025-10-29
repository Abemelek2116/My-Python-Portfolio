"""
main.py
--------
Entry point for the Stock Analyzer project.
Performs full data fetching, cleaning, analysis, and visualization.
"""

import os
import pandas as pd
from src.data_fetcher import DataFetcher
from src.data_cleaner import DataCleaner
from src.stock_analyzer import StockAnalyzer
from src.visualizer import Visualizer
from src.utils import log, ensure_dir


def main():
    log("=== Starting Stock Analyzer Pipeline ===")

    # Create output directories
    ensure_dir("outputs/figures")
    ensure_dir("outputs/reports")

    # Step 1: Fetch
    ticker = "AAPL"  # You can change this to any stock
    df = DataFetcher.fetch_data(ticker, "2023-01-01", "2025-01-01")

    # Step 2: Clean
    df_clean = DataCleaner.clean(df)

    # Step 3: Analyze
    df_analysis = StockAnalyzer.add_indicators(df_clean)
    summary = StockAnalyzer.summary_stats(df_analysis)

    # Step 4: Visualize
    Visualizer.plot_price_trend(df_analysis, ticker, "outputs/figures/price_trend.png")
    Visualizer.plot_returns(df_analysis, "outputs/figures/daily_returns.png")

    # Step 5: Save summary
    summary.to_csv("outputs/reports/summary_stats.csv", index=False)
    log("Summary saved to outputs/reports/summary_stats.csv")

    log("=== Stock Analysis Completed Successfully ===")


if __name__ == "__main__":
    main()

