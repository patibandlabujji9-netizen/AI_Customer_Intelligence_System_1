import streamlit as st

st.set_page_config(
    page_title="AI Customer Intelligence System",
    layout="wide",
    page_icon="📊"
)

# -------------------------
# HEADER UI
# -------------------------
st.title("📊 AI Driven Customer Intelligence System")
st.markdown("### Smart Analytics • Churn Prediction • Segmentation • Recommendations")

st.markdown("---")

# -------------------------
# SIDEBAR NAVIGATION INFO
# -------------------------
st.sidebar.title("📌 Navigation")
st.sidebar.info(
    """
    Use the pages below:

    📊 Dashboard  
    📉 Churn Prediction  
    👥 Segmentation  
    🎯 Recommendations  
    🔮 Prediction Tool
    """
)

# -------------------------
# HOME DASHBOARD UI
# -------------------------
st.subheader("🏠 System Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("📊 Dashboard Analytics")
    st.write("View customer insights and trends")

with col2:
    st.warning("📉 Churn Prediction")
    st.write("Predict whether customers will leave")

with col3:
    st.info("🎯 Recommendations")
    st.write("AI-based product suggestions")

st.markdown("---")

st.subheader("🚀 Features")

st.write("""
✔ Customer Churn Prediction  
✔ Customer Segmentation  
✔ Personalized Recommendations  
✔ Data Analytics Dashboard  
✔ Interactive Visual Reports  
""")