from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


def tune_random_forest(X, y):

    params = {

        "n_estimators": [50, 100, 200],

        "max_depth": [
            5,
            10,
            20
        ]
    }

    model = RandomForestRegressor()

    grid = GridSearchCV(
        model,
        params,
        cv=3,
        scoring="r2"
    )

    grid.fit(X, y)

    return grid.best_estimator_