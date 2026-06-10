import streamlit as st

def inventory_page():

    st.title("📦 Inventory Optimization")

    if "data" not in st.session_state:
        st.warning("Upload dataset first")
        return

    df = st.session_state["data"]

    demand = df["Quantity"].mean()

    lead_time = 7

    safety_stock = demand * 0.25

    reorder_point = (
        demand * lead_time
    ) + safety_stock

    c1,c2 = st.columns(2)

    c1.metric(
        "Safety Stock",
        round(safety_stock)
    )

    c2.metric(
        "Reorder Point",
        round(reorder_point)
    )