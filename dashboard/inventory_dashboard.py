import streamlit as st
import plotly.express as px


def inventory_dashboard():

    st.header("📦 Inventory Dashboard")

    if "data" not in st.session_state:
        st.warning("Upload data first")
        return

    df = st.session_state["data"]

    if "Inventory" not in df.columns:
        st.warning("Inventory column not found")
        return

    fig = px.bar(
        df,
        x="Product",
        y="Inventory",
        title="Inventory Levels"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )