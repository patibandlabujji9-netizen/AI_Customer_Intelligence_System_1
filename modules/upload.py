import streamlit as st
import pandas as pd

def upload_page():

    st.title("📂 Upload Dataset")

    file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if file is not None:

        df = pd.read_csv(file)

        st.session_state["data"] = df

        st.success("Dataset Uploaded Successfully")

        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        st.dataframe(df.head())