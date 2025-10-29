"""
model_training.py
-----------------
Trains a regression model on real estate data.
"""

from sklearn.linear_model import LinearRegression
from src.utils import log, save_model


class ModelTrainer:
    """Trains and saves a Linear Regression model."""

    @staticmethod
    def train(X_train, y_train, save_path: str):
        log("Training Linear Regression model ...")
        model = LinearRegression()
        model.fit(X_train, y_train)
        log("Training completed.")
        save_model(model, save_path)
        return model

