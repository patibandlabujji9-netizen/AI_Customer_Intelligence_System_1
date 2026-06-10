import streamlit as st

def preprocessing_page():

    st.title("⚙ Data Processing")

    if "data" not in st.session_state:
        st.warning("Upload dataset first")
        return

    df = st.session_state["data"]

    st.subheader("Missing Values")

    st.dataframe(df.isnull().sum())

    if st.button("Remove Missing Values"):

        df = df.dropna()

        st.session_state["data"] = df

        st.success("Data Cleaned Successfully")

        st.dataframe(df.head())