"""
utils.py
--------
Utility module for logging and saving/loading files.
"""

import joblib
from datetime import datetime
import os


def log(message: str):
    """Simple logger with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def save_model(model, filepath: str):
    """Save trained ML model to file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(model, filepath)
    log(f"Model saved to {filepath}")


def load_model(filepath: str):
    """Load saved ML model."""
    model = joblib.load(filepath)
    log(f"Model loaded from {filepath}")
    return model

