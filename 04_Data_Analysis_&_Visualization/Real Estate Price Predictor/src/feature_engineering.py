"""
feature_engineering.py
----------------------
Encodes categorical features and prepares numerical data for ML.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.utils import log


class FeatureEngineer:
    """Transforms data for model consumption."""

    @staticmethod
    def prepare_features(df: pd.DataFrame):
        log("Starting feature engineering ...")

        X = df[["location", "sqft", "bedrooms", "bathrooms", "year_built"]]
        y = df["price"]

        # One-hot encode 'location'
        encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
        X_encoded = encoder.fit_transform(X[["location"]])
        encoded_cols = encoder.get_feature_names_out(["location"])
        X_encoded_df = pd.DataFrame(X_encoded, columns=encoded_cols)

        # Combine with numerical features
        X_final = pd.concat([X[["sqft", "bedrooms", "bathrooms", "year_built"]].reset_index(drop=True),
                             X_encoded_df.reset_index(drop=True)], axis=1)

        # Scale numeric data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_final)
        X_scaled_df = pd.DataFrame(X_scaled, columns=X_final.columns)

        log("Feature engineering completed.")
        return train_test_split(X_scaled_df, y, test_size=0.2, random_state=42), encoder, scaler

