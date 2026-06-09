import pandas as pd
import joblib
import os

BASE = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE, "..", "saved_models", "churn_model.pkl"))
scaler = joblib.load(os.path.join(BASE, "..", "saved_models", "scaler.pkl"))


def preprocess(customer_id, age, income, score, gender, subscribed):

    gender = 1 if gender == "Male" else 0
    subscribed = 1 if subscribed else 0

    df = pd.DataFrame([{
        "CustomerID": customer_id,
        "Age": age,
        "AnnualIncome": income,
        "SpendingScore": score,
        "Gender": gender,
        "IsSubscribed": subscribed
    }])

    return scaler.transform(df)


def predict_churn(customer_id, age, income, score, gender, subscribed):

    X = preprocess(customer_id, age, income, score, gender, subscribed)
    pred = model.predict(X)[0]

    return "Churn" if pred == 1 else "No Churn"


def predict_probability(customer_id, age, income, score, gender, subscribed):

    X = preprocess(customer_id, age, income, score, gender, subscribed)
    prob = model.predict_proba(X)[0][1]

    return round(prob * 100, 2)