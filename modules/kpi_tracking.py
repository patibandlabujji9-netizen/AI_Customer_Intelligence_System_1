import streamlit as st

def kpi_tracking_page():

    st.title("📈 KPI Tracking")

    if "data" not in st.session_state:
        return

    df = st.session_state["data"]

    sales_growth = (
        (df["Sales"].max() -
         df["Sales"].min())
        / df["Sales"].min()
    ) * 100

    st.metric(
        "Sales Growth %",
        f"{sales_growth:.2f}%"
    )

    st.metric(
        "Forecast Accuracy",
        "94%"
    )