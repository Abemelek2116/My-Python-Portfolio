"""
analyze.py
-----------
Performs analytical queries and summary statistics on the loaded data.
"""

import pandas as pd
from utils.db_utils import Database
from utils.logger import Logger


class Analyzer:
    """Handles analytical computations."""

    @staticmethod
    def compute_summary() -> pd.DataFrame:
        Logger.log("Running data analysis ...")
        with Database() as db:
            rows = db.query("""
                SELECT region, SUM(revenue) as total_revenue, SUM(quantity) as total_quantity
                FROM sales
                GROUP BY region
                ORDER BY total_revenue DESC
            """)
        df = pd.DataFrame(rows, columns=["Region", "Total Revenue", "Total Quantity"])
        Logger.log("Data analysis completed.")
        return df

