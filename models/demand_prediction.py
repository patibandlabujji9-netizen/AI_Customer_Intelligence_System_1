import pandas as pd


def predict_demand(df):

    avg_demand = (
        df["Quantity"]
        .rolling(7)
        .mean()
    )

    return avg_demand