from database.db_connection import get_connection


# -----------------------------
# USER OPERATIONS
# -----------------------------

def add_user(username, password, role):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (username,password,role)
        VALUES(?,?,?)
        """,
        (username, password, role)
    )

    conn.commit()

    conn.close()


def get_all_users():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users"
    )

    users = cursor.fetchall()

    conn.close()

    return users


def delete_user(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    conn.commit()

    conn.close()


# -----------------------------
# FORECAST OPERATIONS
# -----------------------------

def save_forecast(
    forecast_date,
    predicted_sales,
    model_name
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO forecasts
        (
        forecast_date,
        predicted_sales,
        model_name
        )
        VALUES(?,?,?)
        """,
        (
            forecast_date,
            predicted_sales,
            model_name
        )
    )

    conn.commit()

    conn.close()


def get_forecasts():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM forecasts
        """
    )

    data = cursor.fetchall()

    conn.close()

    return data