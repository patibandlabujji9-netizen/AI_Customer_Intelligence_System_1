import streamlit as st
import plotly.express as px
from utils.data_loader import normalize_sales_data


def inventory_dashboard():

    st.header("📦 Inventory Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    try:
        df = normalize_sales_data(st.session_state["data"])
    except KeyError as exc:
        st.error(str(exc))
        return

    if "Inventory" not in df.columns:
        st.warning("Inventory column not found")
        return

    if "Product" not in df.columns:
        st.warning("Product column not found")
        return

    fig = px.bar(
        df,
        x="Product",
        y="Inventory",
        title="Inventory Levels"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    if "Product" in df.columns:
        inventory_share = (
            df.groupby("Product")["Inventory"]
            .sum()
            .reset_index()
        )

        pie_fig = px.pie(
            inventory_share,
            names="Product",
            values="Inventory",
            title="Inventory Share by Product"
        )

        st.plotly_chart(
            pie_fig,
            width="stretch"
        )
