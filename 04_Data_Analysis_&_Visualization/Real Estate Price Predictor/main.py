"""
main.py
--------
End-to-End pipeline for Real Estate Price Prediction using ML.
"""

import os
from src.data_preprocessing import DataPreprocessor
from src.feature_engineering import FeatureEngineer
from src.model_training import ModelTrainer
from src.model_evaluation import ModelEvaluator
from src.visualize_results import Visualizer
from src.utils import log

os.makedirs("outputs/figures", exist_ok=True)
os.makedirs("models", exist_ok=True)

def main():
    log("=== Starting Real Estate Price Prediction Pipeline ===")

    # Step 1: Load and clean data
    df = DataPreprocessor.load_data("data/raw/real_estate_data.csv")
    clean_df = DataPreprocessor.clean_data(df)

    # Step 2: Feature Engineering
    (X_train, X_test, y_train, y_test), encoder, scaler = FeatureEngineer.prepare_features(clean_df)

    # Step 3: Train Model
    model = ModelTrainer.train(X_train, y_train, "models/linear_regression_model.pkl")

    # Step 4: Evaluate Model
    r2, mae, rmse, predictions = ModelEvaluator.evaluate(model, X_test, y_test)

    # Step 5: Visualize Results
    Visualizer.plot_results(y_test, predictions, "outputs/figures/predicted_vs_actual.png")

    log("=== Pipeline Execution Completed Successfully ===")

if __name__ == "__main__":
    main()

