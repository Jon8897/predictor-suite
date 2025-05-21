# Version 1.0.0.0

import pandas as pd
import os

def load_draw_history(filepath: str = "data/euromillions/draws.csv") -> pd.DataFrame:
    """
    Loads and cleans historical EuroMillions draw data.

    Parameters:
        filepath (str): Path to the CSV file with draw history.

    Returns:
        pd.DataFrame: Cleaned DataFrame with draw date, main numbers, and lucky stars.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Draw history file not found: {filepath}")

    df = pd.read_csv(filepath)

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Expected columns: 'date', 'main_1' through 'main_5', 'star_1', 'star_2'
    expected_cols = {'date', 'main_1', 'main_2', 'main_3', 'main_4', 'main_5', 'star_1', 'star_2'}
    if not expected_cols.issubset(df.columns):
        raise ValueError("Missing expected columns in draw history CSV.")

    # Convert date to datetime format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop rows with invalid dates or missing values
    df.dropna(subset=['date'], inplace=True)
    df.dropna(axis=0, how='any', inplace=True)

    # Sort by date (newest first)
    df.sort_values(by='date', ascending=False, inplace=True)

    return df