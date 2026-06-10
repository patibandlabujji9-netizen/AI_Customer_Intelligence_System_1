import pandas as pd


def forecast_accuracy(
    actual,
    predicted
):

    actual = pd.Series(actual)
    predicted = pd.Series(predicted)

    mape = (
        abs(
            (actual - predicted)
            / actual
        ).mean()
    ) * 100

    accuracy = 100 - mape

    return round(
        accuracy,
        2
    )