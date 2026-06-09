
import streamlit as st
from models.churn_prediction import predict_churn

st.title("Customer Churn Prediction")

customer_id = st.number_input(
    "Customer ID",
    min_value=1,
    step=1
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=25,
    step=1
)

income = st.number_input(
    "Annual Income",
    min_value=1000,
    value=50000,
    step=1000
)

score = st.number_input(
    "Spending Score",
    min_value=1,
    max_value=100,
    value=50,
    step=1
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

subscribed = st.selectbox(
    "Subscribed",
    [0, 1]
)

if st.button("Predict Churn"):

    result = predict_churn(
        customer_id,
        age,
        income,
        score,
        gender,
        subscribed
    )

    if result == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")
