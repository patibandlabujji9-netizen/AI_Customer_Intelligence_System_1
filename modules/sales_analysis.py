
import streamlit as st
import plotly.express as px

def sales_analysis_page():

    st.title("📊 Sales Analysis")

    if "data" not in st.session_state:
        return

    df = st.session_state["data"]

    sales_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        sales_region,
        x="Region",
        y="Sales"
    )

    st.plotly_chart(fig, use_container_width=True)