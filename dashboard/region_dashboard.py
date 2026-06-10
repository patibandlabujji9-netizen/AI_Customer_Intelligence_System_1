import streamlit as st
import plotly.express as px


def region_dashboard():

    st.header("🌍 Region Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    df = st.session_state["data"]

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
        use_container_width=True
    )