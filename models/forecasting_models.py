import joblib
import pandas as pd


def load_forecast_model():

    return joblib.load(
        "models_saved/random_forest.pkl"
    )


def predict_sales(quantity, inventory):

    model = load_forecast_model()

    data = pd.DataFrame({
        "Quantity": [quantity],
        "Inventory": [inventory]
    })

    prediction = model.predict(data)

    return float(prediction[0])