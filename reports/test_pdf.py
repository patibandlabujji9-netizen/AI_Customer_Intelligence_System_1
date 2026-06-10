import pandas as pd
from reports.pdf_report import generate_pdf_report

df = pd.DataFrame({
    "Sales": [1000, 2000, 3000],
    "Profit": [200, 500, 800],
    "Quantity": [10, 20, 30]
})

file_path = generate_pdf_report(df)

print("PDF Created:", file_path)