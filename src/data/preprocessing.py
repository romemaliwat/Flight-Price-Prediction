"""
Preprocessing module for Flight Price Prediction dataset.
Handles data cleaning, feature transformation, and encoding.
"""

def load_dataset(path):
    import pandas as pd
    return pd.read_csv(path)