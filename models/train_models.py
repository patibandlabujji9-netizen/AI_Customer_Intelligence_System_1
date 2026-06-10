from models.train_models import (
    train_random_forest
)

import streamlit as st


def training_page():

    st.title("🤖 Model Training")

    if "data" not in st.session_state:

        st.warning(
            "Upload dataset first"
        )

        return

    df = st.session_state["data"]

    if st.button(
        "Train Random Forest"
    ):

        train_random_forest(df)

        st.success(
            "Model Trained Successfully"
        )

        st.balloons()