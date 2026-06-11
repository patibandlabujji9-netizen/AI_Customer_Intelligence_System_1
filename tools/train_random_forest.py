import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os



def main():
    csv_path = os.path.join("dataset", "sales_data.csv")
    df = pd.read_csv(csv_path)

    X = df[["Quantity", "Inventory"]].values
    y = df["Sales"].values

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    out_path = os.path.join("models_saved", "random_forest.pkl")
    joblib.dump(model, out_path)

    print(f"Saved RandomForest model to {out_path}")


if __name__ == "__main__":
    main()
