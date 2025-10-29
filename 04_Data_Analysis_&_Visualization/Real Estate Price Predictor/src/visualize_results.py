"""
visualize_results.py
--------------------
Visualizes predicted vs actual prices.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from src.utils import log


class Visualizer:
    """Creates model performance plots."""

    @staticmethod
    def plot_results(y_test, predictions, save_path: str):
        log("Generating visualization ...")
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=y_test, y=predictions, color='royalblue', alpha=0.7)
        plt.xlabel("Actual Price")
        plt.ylabel("Predicted Price")
        plt.title("Actual vs Predicted House Prices")
        plt.plot([y_test.min(), y_test.max()],
                 [y_test.min(), y_test.max()],
                 color='red', linestyle='--')
        plt.tight_layout()
        plt.savefig(save_path)
        log(f"Visualization saved to {save_path}")

