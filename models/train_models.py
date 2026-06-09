import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
data = pd.read_csv("dataset/customer_data.csv")

# Features
X = data.drop(["Churn"], axis=1)
y = data["Churn"]

# Encode Gender
X["Gender"] = X["Gender"].map({"Male": 1, "Female": 0})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save folder
os.makedirs("saved_models", exist_ok=True)

joblib.dump(model, "saved_models/churn_model.pkl")
joblib.dump(scaler, "saved_models/scaler.pkl")

print("Model trained and saved successfully!")