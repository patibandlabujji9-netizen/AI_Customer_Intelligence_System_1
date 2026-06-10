from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def evaluate_model(
    y_true,
    y_pred
):

    metrics = {

        "MAE":
        mean_absolute_error(
            y_true,
            y_pred
        ),

        "RMSE":
        mean_squared_error(
            y_true,
            y_pred
        ) ** 0.5,

        "R2":
        r2_score(
            y_true,
            y_pred
        )
    }

    return metrics