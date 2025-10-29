"""
main.py
-------
Entry point for the COVID-19 Data Dashboard.
Runs the complete workflow: load -> clean -> analyze -> visualize -> report.
"""

import os
from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.data_analyzer import DataAnalyzer
from src.data_visualizer import DataVisualizer
from src.report_generator import ReportGenerator

OUTPUT_DIR = "outputs"
FIG_DIR = os.path.join(OUTPUT_DIR, "figures")
REPORT_DIR = os.path.join(OUTPUT_DIR, "reports")

os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

def main():
    data_path = "data/covid_data.csv"

    # Step 1: Load Data
    df = DataLoader.load_data(data_path)

    # Step 2: Clean Data
    df = DataCleaner.clean_data(df)

    # Step 3: Analyze Data
    top_cases = DataAnalyzer.top_countries(df, "total_cases")
    corr = DataAnalyzer.correlation_analysis(df)

    # Step 4: Visualize Results
    DataVisualizer.plot_top_countries(top_cases, "total_cases", f"{FIG_DIR}/top_countries.png")
    DataVisualizer.plot_trend(df, "United States", f"{FIG_DIR}/us_trend.png")
    DataVisualizer.plot_correlation(corr, f"{FIG_DIR}/correlation_heatmap.png")

    # Step 5: Generate Report
    ReportGenerator.generate_report(top_cases, corr, f"{REPORT_DIR}/summary_report.txt")

if __name__ == "__main__":
    main()

