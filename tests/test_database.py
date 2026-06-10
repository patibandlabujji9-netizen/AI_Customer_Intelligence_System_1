# tests/test_database.py

import unittest
from database.db_connection import get_connection


class TestDatabase(unittest.TestCase):

    def test_database_connection(self):

        conn = get_connection()

        self.assertIsNotNone(conn)

        conn.close()


if __name__ == "__main__":
    unittest.main()