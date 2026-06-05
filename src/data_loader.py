"""Data loading and cleaning utilities."""
import pandas as pd
from pathlib import Path


def load_data(path: str | Path) -> pd.DataFrame:
    """Load the mobile price dataset from a CSV file."""
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values and basic cleaning."""
    df = df.copy()
    # Fill missing numeric values with column median
    for col in df.select_dtypes(include="number").columns:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())
    return df


def split_features_target(df: pd.DataFrame, target: str = "price_range"):
    """Split a dataframe into X (features) and y (target)."""
    X = df.drop(columns=[target])
    y = df[target]
    return X, y
