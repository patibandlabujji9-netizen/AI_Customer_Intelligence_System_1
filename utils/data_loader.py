from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SALES_DATA_CANDIDATES = (
    PROJECT_ROOT / "dataset" / "sales_data.csv",
    PROJECT_ROOT / "datasets" / "sales_data.csv",
)
SALES_DATA_PATH = SALES_DATA_CANDIDATES[0]


def load_sales_data():
    for data_path in SALES_DATA_CANDIDATES:
        if data_path.exists():
            return pd.read_csv(data_path)

    expected_paths = ", ".join(str(path) for path in SALES_DATA_CANDIDATES)
    raise FileNotFoundError(
        "Sales data file not found. Expected one of: "
        f"{expected_paths}"
    )


def normalize_sales_data(df):
    df = df.copy()
    df.columns = df.columns.str.strip()

    required_columns = {"Date", "Sales"}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise KeyError(f"Missing required column(s): {missing}")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    df["Month"] = df["Date"].dt.strftime("%Y-%m")
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)

    if "Profit" in df.columns:
        df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce").fillna(0)

    return df
