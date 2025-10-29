"""
report_generator.py
-------------------
Generates a summary text report with key insights.
"""

import pandas as pd
from utils.logger import Logger


class ReportGenerator:
    """Creates summary reports for analysis results."""

    @staticmethod
    def generate_report(top_countries_df: pd.DataFrame, corr_df: pd.DataFrame, save_path: str) -> None:
        """
        Writes summary report to a text file.
        """
        Logger.log("Generating analysis report ...")
        with open(save_path, "w") as f:
            f.write("COVID-19 Data Analysis Report\n")
            f.write("=" * 40 + "\n\n")
            f.write("Top 10 Countries by Total Cases:\n")
            f.write(top_countries_df.to_string(index=False))
            f.write("\n\nCorrelation Analysis:\n")
            f.write(corr_df.to_string())
        Logger.log(f"Report saved to {save_path}")

