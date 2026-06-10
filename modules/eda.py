import streamlit as st
import plotly.express as px

def eda_page():

    st.title("📈 Exploratory Data Analysis")

    if "data" not in st.session_state:
        st.warning("Upload dataset first")
        return

    df = st.session_state["data"]

    numeric_cols = df.select_dtypes(
        include=["int64","float64"]
    ).columns

    selected = st.selectbox(
        "Select Column",
        numeric_cols
    )

    fig1 = px.histogram(
        df,
        x=selected,
        title=f"{selected} Distribution"
    )

    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.box(
        df,
        y=selected,
        title=f"{selected} Outliers"
    )

    st.plotly_chart(fig2, use_container_width=True)