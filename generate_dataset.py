import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "CustomerID": range(1, n + 1),
    "Age": np.random.randint(18, 70, n),
    "AnnualIncome": np.random.randint(20000, 120000, n),
    "SpendingScore": np.random.randint(1, 100, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "IsSubscribed": np.random.choice([0, 1], n),
    "Churn": np.random.choice([0, 1], n)
})

data.to_csv("dataset/customer_data.csv", index=False)

print("Dataset generated successfully!")