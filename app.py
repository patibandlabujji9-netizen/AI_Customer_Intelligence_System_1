import streamlit as st

from modules.home import home_page
from modules.upload import upload_page
from modules.preprocessing import preprocessing_page
from modules.eda import eda_page
from modules.model_training import training_page
from modules.forecasting import forecasting_page
from modules.inventory import inventory_page
from modules.reports import reports_page

st.set_page_config(
    page_title="AI Sales Forecasting",
    layout="wide"
)

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Select",
    [
        "Dashboard",
        "Upload",
        "Processing",
        "EDA",
        "Training",
        "Forecasting",
        "Inventory",
        "Reports"
    ]
)

if page == "Dashboard":
    home_page()

elif page == "Upload":
    upload_page()

elif page == "Processing":
    preprocessing_page()

elif page == "EDA":
    eda_page()

elif page == "Training":
    training_page()

elif page == "Forecasting":
    forecasting_page()

elif page == "Inventory":
    inventory_page()

elif page == "Reports":
    reports_page()