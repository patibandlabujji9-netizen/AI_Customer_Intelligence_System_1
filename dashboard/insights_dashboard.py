import streamlit as st
import plotly.express as px
from utils.data_loader import normalize_sales_data


def insights_dashboard():

    st.header("🧠 AI Insights")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    try:
        df = normalize_sales_data(st.session_state["data"])
    except KeyError as exc:
        st.error(str(exc))
        return

    if "Product" not in df.columns or "Region" not in df.columns:
        st.warning("Product and Region columns are required for insights")
        return

    best_product = (
        df.groupby("Product")["Sales"]
        .sum()
        .idxmax()
    )

    best_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    st.success(
        f"Best Product : {best_product}"
    )

    st.success(
        f"Best Region : {best_region}"
    )

    st.info(
        "Increase inventory for top selling products."
    )

    product_sales = (
        df.groupby("Product")["Sales"]
        .sum()
        .reset_index()
    )

    pie_fig = px.pie(
        product_sales,
        names="Product",
        values="Sales",
        title="Product Sales Share"
    )

    st.plotly_chart(
        pie_fig,
        width="stretch"
    )
