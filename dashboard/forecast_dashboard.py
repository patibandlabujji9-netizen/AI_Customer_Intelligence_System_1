import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from models.demand_prediction import forecast_sales
from utils.data_loader import load_sales_data

def show_forecast_dashboard():

    st.title("Sales Forecast Dashboard")

    try:
        df = st.session_state["data"] if "data" in st.session_state else load_sales_data()
        forecast_df = forecast_sales(df)
    except (FileNotFoundError, KeyError) as exc:
        st.error(str(exc))
        return

    st.dataframe(forecast_df)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=forecast_df["Month"],
            y=forecast_df["Actual"],
            name="Actual"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast_df["Month"],
            y=forecast_df["Forecast"],
            name="Forecast"
        )
    )

    st.plotly_chart(fig, width="stretch")

    forecast_summary = pd.DataFrame({
        "Type": ["Actual", "Forecast"],
        "Sales": [
            forecast_df["Actual"].sum(),
            forecast_df["Forecast"].sum()
        ]
    })

    pie_fig = px.pie(
        forecast_summary,
        names="Type",
        values="Sales",
        title="Actual vs Forecast Share"
    )

    st.plotly_chart(pie_fig, width="stretch")
