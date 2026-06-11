import streamlit as st

from dashboard.executive_dashboard import show_executive_dashboard
from dashboard.sales_dashboard import show_sales_dashboard
from dashboard.forecast_dashboard import show_forecast_dashboard
from dashboard.inventory_dashboard import inventory_dashboard as show_inventory_dashboard
from dashboard.insights_dashboard import insights_dashboard as show_insights_dashboard
from dashboard.kpi_dashboard import kpi_dashboard as show_kpi_dashboard
from dashboard.region_dashboard import region_dashboard as show_region_dashboard
from dashboard.target_dashboard import target_dashboard as show_target_dashboard
from modules.upload import show_upload
from utils.data_loader import load_sales_data

st.set_page_config(
    page_title="Intelligent Sales Forecasting",
    page_icon="📈",
    layout="wide"
)

if "data" not in st.session_state:
    try:
        st.session_state["data"] = load_sales_data()
    except FileNotFoundError:
        pass

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Upload",
        "Executive",
        "Sales",
        "Forecast",
        "Inventory",
        "Insights",
        "KPI",
        "Region",
        "Target"
    ]
)

if page == "Upload":
    show_upload()

elif page == "Executive":
    show_executive_dashboard()

elif page == "Sales":
    show_sales_dashboard()

elif page == "Forecast":
    show_forecast_dashboard()

elif page == "Inventory":
    show_inventory_dashboard()

elif page == "Insights":
    show_insights_dashboard()

elif page == "KPI":
    show_kpi_dashboard()

elif page == "Region":
    show_region_dashboard()

elif page == "Target":
    show_target_dashboard()
