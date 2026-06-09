import pandas as pd

def clean_data(df):
    df = df.dropna()
    df.columns = [c.strip() for c in df.columns]
    return df