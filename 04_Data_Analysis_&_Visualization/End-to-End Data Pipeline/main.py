"""
main.py
-------
Entry point of the End-to-End Data Pipeline project.
Executes all ETL + analysis + visualization + reporting steps sequentially.
"""

import os
import pandas as pd
from src.extract import Extractor
from src.transform import Transformer
from src.load import Loader
from src.analyze import Analyzer
from src.visualize import Visualizer
from src.report_generator import ReportGenerator
from utils.logger import Logger

# Output directories
os.makedirs("outputs/figures", exist_ok=True)
os.makedirs("outputs/reports", exist_ok=True)

def main():
    Logger.log("=== Starting End-to-End Data Pipeline ===")

    # Step 1: Extract
    df = Extractor.from_csv("data/raw/sales_data.csv")

    # Step 2: Transform
    cleaned = Transformer.clean_data(df)
    aggregated = Transformer.aggregate_data(cleaned)

    # Step 3: Load
    Loader.to_database(cleaned[["region", "product", "revenue", "quantity", "date"]].values.tolist())

    # Step 4: Analyze
    summary = Analyzer.compute_summary()

    # Step 5: Visualize
    Visualizer.plot_revenue_by_region(summary, "outputs/figures/revenue_by_region.png")

    # Step 6: Report
    ReportGenerator.generate_report(summary, "outputs/reports/summary_report.txt")

    Logger.log("=== Pipeline Execution Completed Successfully ===")

if __name__ == "__main__":
    main()

