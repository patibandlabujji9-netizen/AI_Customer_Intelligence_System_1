import streamlit as st
import pandas as pd

st.title("👥 Customer Segmentation")

data = pd.read_csv("dataset/customer_data.csv")

st.subheader("Customer Groups by Spending Score")

st.dataframe(data.groupby("SpendingScore").mean(numeric_only=True))