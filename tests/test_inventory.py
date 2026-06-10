# tests/test_inventory.py

import unittest

from models.inventory_model import (
    calculate_inventory_metrics
)


class TestInventory(unittest.TestCase):

    def test_inventory_calculation(self):

        result = (
            calculate_inventory_metrics(
                avg_demand=100
            )
        )

        self.assertIn(
            "safety_stock",
            result
        )

        self.assertIn(
            "reorder_point",
            result
        )

        self.assertGreater(
            result["reorder_point"],
            0
        )


if __name__ == "__main__":
    unittest.main()