# utils/validation.py

import pandas as pd


REQUIRED_COLUMNS = [
    "Date",
    "Sales",
    "Quantity"
]


def validate_dataset(df):

    missing = []

    for col in REQUIRED_COLUMNS:

        if col not in df.columns:

            missing.append(col)

    return missing