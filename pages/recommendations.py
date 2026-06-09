import streamlit as st
from models.recommendation import get_recommendations

st.set_page_config(page_title="Recommendations", layout="centered")

st.title("🎯 AI Recommendations")

age = st.number_input("Age", 18, 70, 25)
income = st.number_input("Income", 20000, 120000, 50000)
score = st.number_input("Spending Score", 1, 100, 50)

gender = st.selectbox("Gender", ["Male", "Female"])
subscribed = st.selectbox("Subscribed", ["Yes", "No"])

if st.button("Generate Recommendations 🚀"):

    recs = get_recommendations(age, income, score, gender, subscribed == "Yes")

    st.markdown("---")
    st.subheader("✨ Recommended Products")

    for r in recs:
        st.success(r)

    st.info("💡 Personalized based on customer profile & behavior patterns.")