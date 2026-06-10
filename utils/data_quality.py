# utils/data_quality.py

import pandas as pd


def data_quality_report(df):

    report = {

        "rows": len(df),

        "columns": len(df.columns),

        "missing_values":
        int(
            df.isnull()
            .sum()
            .sum()
        ),

        "duplicate_rows":
        int(
            df.duplicated()
            .sum()
        )
    }

    return report