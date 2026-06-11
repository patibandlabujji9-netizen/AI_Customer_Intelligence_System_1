import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from utils.data_loader import load_sales_data, normalize_sales_data

def forecast_sales(df=None):

    if df is None:
        df = load_sales_data()

    df = normalize_sales_data(df)

    monthly = (
        df.groupby("Month")["Sales"]
        .sum()
        .reset_index()
    )

    monthly["Index"] = np.arange(len(monthly))

    X = monthly[["Index"]]
    y = monthly["Sales"]

    model = LinearRegression()
    model.fit(X, y)

    monthly["Forecast"] = model.predict(X)

    return pd.DataFrame({
        "Month": monthly["Month"],
        "Actual": monthly["Sales"],
        "Forecast": monthly["Forecast"]
    })
