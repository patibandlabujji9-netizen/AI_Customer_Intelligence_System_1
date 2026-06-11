import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import normalize_sales_data


def show_upload():

    st.title("📂 Upload Dataset")

    file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if file is not None:

        try:
            df = normalize_sales_data(pd.read_csv(file))
        except KeyError as exc:
            st.error(str(exc))
            return

        st.session_state["data"] = df

        st.success("Dataset Uploaded Successfully")

        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        st.dataframe(
            df.head(),
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
                title="Uploaded Data Product Share"
            )

            st.plotly_chart(
                pie_fig,
                width="stretch"
            )
