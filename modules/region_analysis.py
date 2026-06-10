import streamlit as st
import plotly.express as px

def region_analysis_page():

    st.title("🌍 Region Analysis")

    if "data" not in st.session_state:
        return

    df = st.session_state["data"]

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        region_sales,
        names="Region",
        values="Sales"
    )

    st.plotly_chart(fig, use_container_width=True)