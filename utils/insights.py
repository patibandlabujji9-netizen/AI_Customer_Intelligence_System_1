# utils/insights.py


def generate_insights(df):

    insights = []

    if "Sales" in df.columns:

        highest = df["Sales"].max()

        insights.append(
            f"Highest Sales: {highest}"
        )

    if "Profit" in df.columns:

        highest_profit = df["Profit"].max()

        insights.append(
            f"Highest Profit: {highest_profit}"
        )

    return insights