# utils/export.py

import pandas as pd


def export_csv(
    df,
    file_name="export.csv"
):

    df.to_csv(
        file_name,
        index=False
    )

    return file_name