import streamlit as st
import numpy as np
import plotly.graph_objects as go


def forecast_dashboard():

    st.header("🔮 Forecast Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    df = st.session_state["data"]

    sales = df["Sales"].values

    future = np.random.randint(
        int(sales.mean()),
        int(sales.mean()*1.3),
        30
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=sales,
            name="Actual Sales"
        )
    )

    fig.add_trace(
        go.Scatter(
            y=list(sales[-1:])+list(future),
            name="Forecast"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )