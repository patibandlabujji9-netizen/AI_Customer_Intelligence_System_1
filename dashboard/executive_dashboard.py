import streamlit as st
import plotly.express as px
import pandas as pd


def executive_dashboard():

    st.header("📊 Executive Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload dataset first")
        return

    df = st.session_state["data"]

    total_sales = df["Sales"].sum()
    total_orders = len(df)

    profit = (
        df["Profit"].sum()
        if "Profit" in df.columns
        else 0
    )

    avg_sales = df["Sales"].mean()

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Total Sales", f"₹{total_sales:,.0f}")
    c2.metric("Orders", total_orders)
    c3.metric("Profit", f"₹{profit:,.0f}")
    c4.metric("Average Sales", f"₹{avg_sales:,.0f}")

    if "Date" in df.columns:

        df["Date"] = pd.to_datetime(df["Date"])

        trend = df.groupby(
            df["Date"].dt.to_period("M")
        )["Sales"].sum().reset_index()

        trend["Date"] = trend["Date"].astype(str)

        fig = px.line(
            trend,
            x="Date",
            y="Sales",
            markers=True,
            title="Monthly Sales Trend"
        )

        st.plotly_chart(fig, use_container_width=True)