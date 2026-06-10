import streamlit as st
from database.db_connection import get_connection


def login_user(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, username, role
        FROM users
        WHERE username=?
        AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def authenticate(username, password):

    user = login_user(username, password)

    if user:

        st.session_state["logged_in"] = True
        st.session_state["user_id"] = user[0]
        st.session_state["username"] = user[1]
        st.session_state["role"] = user[2]

        return True

    return False


def logout():

    st.session_state.clear()


def is_logged_in():

    return st.session_state.get(
        "logged_in",
        False
    )


def get_role():

    return st.session_state.get(
        "role",
        None
    )


def is_admin():

    return get_role() == "Admin"


def can_access_forecasting():

    role = get_role()

    return role in [
        "Admin",
        "Manager",
        "Analyst"
    ]


def can_access_inventory():

    role = get_role()

    return role in [
        "Admin",
        "Manager"
    ]


def can_access_reports():

    role = get_role()

    return role in [
        "Admin",
        "Manager",
        "Analyst",
        "User"
    ]