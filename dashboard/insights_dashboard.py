import streamlit as st


def insights_dashboard():

    st.header("🧠 AI Insights")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    df = st.session_state["data"]

    best_product = (
        df.groupby("Product")["Sales"]
        .sum()
        .idxmax()
    )

    best_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    st.success(
        f"Best Product : {best_product}"
    )

    st.success(
        f"Best Region : {best_region}"
    )

    st.info(
        "Increase inventory for top selling products."
    )