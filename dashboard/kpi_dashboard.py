import streamlit as st
import plotly.express as px
from utils.data_loader import normalize_sales_data


def kpi_dashboard():

    st.header("📈 KPI Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    try:
        df = normalize_sales_data(st.session_state["data"])
    except KeyError as exc:
        st.error(str(exc))
        return

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
        width="stretch"
    )

    if "Product" in df.columns:
        product_sales = (
            df.groupby("Product")["Sales"]
            .sum()
            .reset_index()
        )

        pie_fig = px.pie(
            product_sales,
            names="Product",
            values="Sales",
            title="Sales Share by Product"
        )

        st.plotly_chart(
            pie_fig,
            width="stretch"
        )
