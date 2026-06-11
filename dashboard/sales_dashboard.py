import streamlit as st
import plotly.express as px
from utils.data_loader import load_sales_data, normalize_sales_data

def show_sales_dashboard():

    st.title("Sales Dashboard")

    try:
        df = st.session_state["data"] if "data" in st.session_state else load_sales_data()
        df = normalize_sales_data(df)
    except (FileNotFoundError, KeyError) as exc:
        st.error(str(exc))
        return

    st.subheader("Sales Table")
    st.dataframe(df)

    if "Product" in df.columns:
        product_sales = (
            df.groupby("Product")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            product_sales,
            x="Product",
            y="Sales",
            color="Product",
            title="Product Wise Sales"
        )

        st.plotly_chart(fig, width="stretch")

        product_pie = px.pie(
            product_sales,
            names="Product",
            values="Sales",
            title="Product Sales Share"
        )

        st.plotly_chart(product_pie, width="stretch")
    else:
        st.warning("Product column not found")

    if "Region" in df.columns:
        region_sales = (
            df.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        fig2 = px.pie(
            region_sales,
            names="Region",
            values="Sales",
            title="Region Distribution"
        )

        st.plotly_chart(fig2, width="stretch")
    else:
        st.warning("Region column not found")
