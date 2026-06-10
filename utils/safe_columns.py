# utils/safe_columns.py


def ensure_column(df, column):

    return column in df.columns


def get_column(df, column):

    if column in df.columns:

        return df[column]

    return None