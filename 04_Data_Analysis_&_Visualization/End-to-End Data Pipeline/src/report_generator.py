"""
report_generator.py
-------------------
Creates a text report summarizing pipeline execution results.
"""

import pandas as pd
from utils.logger import Logger


class ReportGenerator:
    """Generates analysis reports."""

    @staticmethod
    def generate_report(summary_df: pd.DataFrame, save_path: str) -> None:
        Logger.log("Generating pipeline summary report ...")
        with open(save_path, "w") as f:
            f.write("End-to-End Data Pipeline Report\n")
            f.write("=" * 40 + "\n\n")
            f.write("Summary by Region:\n")
            f.write(summary_df.to_string(index=False))
        Logger.log(f"Report saved to {save_path}")

