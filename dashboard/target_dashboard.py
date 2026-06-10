import streamlit as st


def target_dashboard():

    st.header("🎯 Target Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    df = st.session_state["data"]

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