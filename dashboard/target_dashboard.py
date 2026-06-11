import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import normalize_sales_data


def target_dashboard():

    st.header("🎯 Target Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    try:
        df = normalize_sales_data(st.session_state["data"])
    except KeyError as exc:
        st.error(str(exc))
        return

    total_sales = df["Sales"].sum()

    target = st.number_input(
        "Sales Target",
        value=100000
    )

    progress = (
        total_sales / target
    ) * 100

    st.metric(
        "Achievement %",
        f"{progress:.2f}%"
    )

    st.progress(
        min(int(progress),100)
    )

    target_summary = pd.DataFrame({
        "Status": ["Achieved", "Remaining"],
        "Sales": [
            min(total_sales, target),
            max(target - total_sales, 0)
        ]
    })

    pie_fig = px.pie(
        target_summary,
        names="Status",
        values="Sales",
        title="Target Achievement Share"
    )

    st.plotly_chart(
        pie_fig,
        width="stretch"
    )
