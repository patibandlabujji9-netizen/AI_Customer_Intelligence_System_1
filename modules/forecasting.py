import streamlit as st
import pandas as pd
import plotly.express as px

def forecasting_page():

    st.title("🔮 Sales Forecasting")

    if "data" not in st.session_state:
        st.warning("Upload dataset first")
        return

    df = st.session_state["data"]

    if "Date" not in df.columns:
        st.error("Date column required")
        return

    df["Date"] = pd.to_datetime(df["Date"])

    forecast = (
        df.groupby("Date")["Sales"]
        .sum()
        .reset_index()
    )

    forecast["Forecast"] = (
        forecast["Sales"] * 1.10
    )

    fig = px.line(
        forecast,
        x="Date",
        y=["Sales","Forecast"],
        title="Actual vs Forecast"
    )

    st.plotly_chart(fig, use_container_width=True)