# utils/preprocessing.py

import pandas as pd


def clean_data(df):

    df = df.copy()

    df.drop_duplicates(
        inplace=True
    )

    df.dropna(
        inplace=True
    )

    return df


def convert_date(df):

    if "Date" in df.columns:

        df["Date"] = pd.to_datetime(
            df["Date"]
        )

    return df