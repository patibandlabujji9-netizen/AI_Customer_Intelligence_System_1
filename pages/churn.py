import streamlit as st
import matplotlib.pyplot as plt
from models.churn_prediction import predict_churn, predict_probability

st.set_page_config(page_title="Churn Prediction", layout="centered")

st.title("📉 Customer Churn Prediction")

# -------------------------
# INPUT SECTION
# -------------------------
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        customer_id = st.number_input("Customer ID", 1)
        age = st.number_input("Age", 18, 70)

    with col2:
        income = st.number_input("Income", 20000, 120000)
        score = st.number_input("Spending Score", 1, 100)

gender = st.selectbox("Gender", ["Male", "Female"])
subscribed = st.selectbox("Subscribed", ["Yes", "No"])

subscribed_bool = subscribed == "Yes"

# -------------------------
# PREDICTION
# -------------------------
if st.button("🚀 Predict"):

    result = predict_churn(customer_id, age, income, score, gender, subscribed_bool)
    prob = predict_probability(customer_id, age, income, score, gender, subscribed_bool)

    st.markdown("---")

    if result == "Churn":
        st.error("⚠ High Risk Customer")
    else:
        st.success("✅ Low Risk Customer")

    col1, col2 = st.columns(2)
    col1.metric("Churn Probability", f"{prob:.2f}%")
    col2.metric("Retention Score", f"{100 - prob:.2f}%")

    # -------------------------
    # GRAPH
    # -------------------------
    st.subheader("📊 Risk Visualization")

    fig, ax = plt.subplots()
    ax.bar(["Stay", "Churn"], [100 - prob, prob])
    st.pyplot(fig)