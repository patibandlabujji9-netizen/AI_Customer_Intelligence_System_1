# reports/excel_export.py

import os


def export_to_excel(df):

    os.makedirs(
        "generated_reports",
        exist_ok=True
    )

    file_path = (
        "generated_reports/"
        "sales_report.xlsx"
    )

    df.to_excel(
        file_path,
        index=False
    )

    return file_path