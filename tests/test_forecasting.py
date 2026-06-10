# tests/test_forecasting.py

import unittest
from models.forecasting_models import predict_sales


class TestForecasting(unittest.TestCase):

    def test_prediction_output(self):

        try:

            result = predict_sales(
                quantity=50,
                inventory=200
            )

            self.assertTrue(
                isinstance(
                    result,
                    (int, float)
                )
            )

        except Exception:

            self.fail(
                "Forecast prediction failed"
            )


if __name__ == "__main__":
    unittest.main()