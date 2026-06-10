import streamlit as st
import pandas as pd
import plotly.express as px

def home_page():

    st.title("📊 AI Sales Forecasting Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload a dataset first")
        return

    df = st.session_state["data"]

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_quantity = df["Quantity"].sum()
    avg_sales = df["Sales"].mean()

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Total Sales", f"₹{total_sales:,.0f}")
    c2.metric("Total Profit", f"₹{total_profit:,.0f}")
    c3.metric("Total Quantity", f"{total_quantity:,}")
    c4.metric("Average Sales", f"₹{avg_sales:,.0f}")

    if "Date" in df.columns:

        df["Date"] = pd.to_datetime(df["Date"])

        sales_trend = (
            df.groupby("Date")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.line(
            sales_trend,
            x="Date",
            y="Sales",
            title="Sales Trend"
        )

        st.plotly_chart(fig, use_container_width=True)