"""
model_evaluation.py
-------------------
Evaluates the performance of the trained model.
"""

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
from src.utils import log


class ModelEvaluator:
    """Evaluates regression model performance."""

    @staticmethod
    def evaluate(model, X_test, y_test):
        log("Evaluating model ...")
        predictions = model.predict(X_test)

        r2 = r2_score(y_test, predictions)
        mae = mean_absolute_error(y_test, predictions)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))

        log(f"R² Score: {r2:.3f}")
        log(f"MAE: {mae:.2f}")
        log(f"RMSE: {rmse:.2f}")

        return r2, mae, rmse, predictions

