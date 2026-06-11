import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_sales_data, normalize_sales_data

def show_executive_dashboard():

    st.title("Executive Dashboard")

    try:
        df = st.session_state["data"] if "data" in st.session_state else load_sales_data()
        df = normalize_sales_data(df)
    except (FileNotFoundError, KeyError) as exc:
        st.error(str(exc))
        return

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum() if "Profit" in df.columns else 0
    total_orders = len(df)

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Sales", f"${total_sales:,.0f}")
    c2.metric("Total Profit", f"${total_profit:,.0f}")
    c3.metric("Orders", total_orders)

    monthly = df.groupby("Month")["Sales"].sum().reset_index()

    fig = px.line(
        monthly,
        x="Month",
        y="Sales",
        title="Monthly Revenue Trend"
    )

    st.plotly_chart(fig, width="stretch")

    if "Region" in df.columns:
        region_sales = (
            df.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        pie_fig = px.pie(
            region_sales,
            names="Region",
            values="Sales",
            title="Sales Share by Region"
        )

        st.plotly_chart(pie_fig, width="stretch")

    st.subheader("Recent Transactions")
    st.dataframe(df.tail(20))
