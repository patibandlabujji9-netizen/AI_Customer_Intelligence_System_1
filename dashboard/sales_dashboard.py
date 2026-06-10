import streamlit as st
import plotly.express as px


def sales_dashboard():

    st.header("💰 Sales Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    df = st.session_state["data"]

    if "Region" in df.columns:

        region_sales = (
            df.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            region_sales,
            x="Region",
            y="Sales",
            title="Region Wise Sales"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    if "Product" in df.columns:

        product_sales = (
            df.groupby("Product")["Sales"]
            .sum()
            .reset_index()
        )

        fig2 = px.pie(
            product_sales,
            names="Product",
            values="Sales",
            title="Product Contribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )