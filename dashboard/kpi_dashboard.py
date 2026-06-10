import streamlit as st
import plotly.express as px


def kpi_dashboard():

    st.header("📈 KPI Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    df = st.session_state["data"]

    total_sales = df["Sales"].sum()

    avg_sales = df["Sales"].mean()

    max_sales = df["Sales"].max()

    min_sales = df["Sales"].min()

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Total Sales",
        f"₹{total_sales:,.0f}"
    )

    c2.metric(
        "Average Sales",
        f"₹{avg_sales:,.0f}"
    )

    c3.metric(
        "Highest Sale",
        f"₹{max_sales:,.0f}"
    )

    c4.metric(
        "Lowest Sale",
        f"₹{min_sales:,.0f}"
    )

    fig = px.box(
        df,
        y="Sales",
        title="Sales Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )