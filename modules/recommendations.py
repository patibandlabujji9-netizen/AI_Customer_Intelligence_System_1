import streamlit as st

def recommendations_page():

    st.title("💡 AI Recommendations")

    if "data" not in st.session_state:
        st.warning("Upload dataset first")
        return

    df = st.session_state["data"]

    best_product = (
        df.groupby("Product")["Sales"]
        .sum()
        .idxmax()
    )

    st.success(
        f"Increase inventory for {best_product}"
    )

    st.info(
        "Top-selling products should maintain higher safety stock."
    )