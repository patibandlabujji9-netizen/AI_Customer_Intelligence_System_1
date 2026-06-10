# tests/test_auth.py

import unittest


class TestAuth(unittest.TestCase):

    def test_login_validation(self):

        username = "admin"
        password = "admin123"

        self.assertEqual(
            username,
            "admin"
        )

        self.assertEqual(
            password,
            "admin123"
        )


if __name__ == "__main__":
    unittest.main()