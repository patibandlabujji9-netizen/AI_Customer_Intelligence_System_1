# utils/helpers.py

import pandas as pd


def load_csv(file):

    return pd.read_csv(file)


def get_shape(df):

    return df.shape


def get_columns(df):

    return list(df.columns)