from database.db_connection import get_connection


def register_user(username, password, role="User"):
    """
    Register a new user
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users
            (username, password, role)
            VALUES (?, ?, ?)
            """,
            (username, password, role)
        )

        conn.commit()

        return True, "User registered successfully"

    except Exception as e:

        return False, str(e)

    finally:
        conn.close()


def user_exists(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user is not None