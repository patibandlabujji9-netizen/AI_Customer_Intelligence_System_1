from database.db_connection import get_connection


# ---------------------------
# DATASET OPERATIONS
# ---------------------------

def save_uploaded_file(file_name):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO uploaded_data
        (file_name)
        VALUES(?)
        """,
        (file_name,)
    )

    conn.commit()

    conn.close()


def get_uploaded_files():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM uploaded_data
        ORDER BY id DESC
        """
    )

    files = cursor.fetchall()

    conn.close()

    return files


# ---------------------------
# INVENTORY OPERATIONS
# ---------------------------

def add_inventory_item(
    product_name,
    stock_level,
    reorder_point,
    safety_stock
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO inventory
        (
        product_name,
        stock_level,
        reorder_point,
        safety_stock
        )
        VALUES(?,?,?,?)
        """,
        (
            product_name,
            stock_level,
            reorder_point,
            safety_stock
        )
    )

    conn.commit()

    conn.close()


def get_inventory():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM inventory
        """
    )

    inventory = cursor.fetchall()

    conn.close()

    return inventory


def delete_inventory_item(item_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM inventory
        WHERE id=?
        """,
        (item_id,)
    )

    conn.commit()

    conn.close()