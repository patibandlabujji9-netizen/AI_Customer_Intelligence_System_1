def create_features(df):
    df["Income_Per_Age"] = df["AnnualIncome"] / df["Age"]
    return df