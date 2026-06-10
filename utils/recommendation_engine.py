# utils/recommendation_engine.py


def generate_recommendations(df):

    recommendations = []

    if "Inventory" in df.columns:

        low_stock = df[
            df["Inventory"] < 100
        ]

        if len(low_stock) > 0:

            recommendations.append(
                "Some products need restocking."
            )

    if "Sales" in df.columns:

        recommendations.append(
            "Focus on top-selling products."
        )

    return recommendations