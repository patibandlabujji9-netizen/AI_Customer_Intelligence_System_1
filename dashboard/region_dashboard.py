import streamlit as st
import plotly.express as px
from utils.data_loader import normalize_sales_data


def region_dashboard():

    st.header("🌍 Region Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    try:
        df = normalize_sales_data(st.session_state["data"])
    except KeyError as exc:
        st.error(str(exc))
        return

    if "Region" not in df.columns:
        st.warning("Region column not found")
        return

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.treemap(
        region_sales,
        path=["Region"],
        values="Sales",
        title="Region Performance"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    pie_fig = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Region Sales Share"
    )

    st.plotly_chart(
        pie_fig,
        width="stretch"
    )
