import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 Analytics Dashboard")

# Load data
df = pd.read_csv("dataset/customer_data.csv")

# -------------------------
# METRICS
# -------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(df))
col2.metric("Avg Age", round(df["Age"].mean(), 2))
col3.metric("Avg Income", round(df["AnnualIncome"].mean(), 2))
col4.metric("Churn Rate", f"{round(df['Churn'].mean()*100, 2)}%")

st.markdown("---")

# -------------------------
# CHURN CHART
# -------------------------
st.subheader("📉 Churn Distribution")

fig, ax = plt.subplots()
df["Churn"].value_counts().plot(kind="bar", ax=ax)
ax.set_title("Churn Distribution")
st.pyplot(fig)

# -------------------------
# AGE DISTRIBUTION
# -------------------------
st.subheader("👥 Age Distribution")

fig2, ax2 = plt.subplots()
df["Age"].value_counts().sort_index().plot(kind="line", ax=ax2)
ax2.set_title("Age Trend")
st.pyplot(fig2)

# -------------------------
# INCOME VS SCORE
# -------------------------
st.subheader("💰 Income vs Spending Score")

fig3, ax3 = plt.subplots()
ax3.scatter(df["AnnualIncome"], df["SpendingScore"])
ax3.set_xlabel("Income")
ax3.set_ylabel("Score")
st.pyplot(fig3)

# -------------------------
# INSIGHT
# -------------------------
st.info("💡 Insight: Higher income customers show higher spending variability.")