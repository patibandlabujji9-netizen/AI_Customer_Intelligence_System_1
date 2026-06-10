import streamlit as st
import pandas as pd

def reports_page():

    st.title("📑 Reports")

    if "data" not in st.session_state:
        st.warning("Upload dataset first")
        return

    df = st.session_state["data"]

    report = pd.DataFrame({

        "Metric":[
            "Total Sales",
            "Total Profit",
            "Total Quantity",
            "Records"
        ],

        "Value":[
            df["Sales"].sum(),
            df["Profit"].sum(),
            df["Quantity"].sum(),
            len(df)
        ]
    })

    st.dataframe(report)

    csv = report.to_csv(index=False)

    st.download_button(
        "⬇ Download Report",
        csv,
        "sales_report.csv",
        "text/csv"
    )

    st.subheader("Dataset Summary")

    st.dataframe(df.describe())