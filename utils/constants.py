# utils/auth.py

import streamlit as st


def login(username, password):

    if username == "admin" and password == "admin123":

        st.session_state["logged_in"] = True

        return True

    return False


def logout():

    st.session_state.clear()


def is_logged_in():

    return st.session_state.get(
        "logged_in",
        False
    )