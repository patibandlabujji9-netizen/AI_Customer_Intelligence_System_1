import pandas as pd

def get_recommendations(age, income, score, gender, subscribed):

    recommendations = []

    # -------------------------
    # High value customers
    # -------------------------
    if income > 80000 and score > 60:
        recommendations = [
            "Premium Laptop 💻",
            "Luxury Watch ⌚",
            "Smartphone Pro 📱",
            "Travel Package ✈️"
        ]

    # -------------------------
    # Medium value customers
    # -------------------------
    elif income > 40000:
        recommendations = [
            "Budget Smartphone 📱",
            "Bluetooth Headphones 🎧",
            "Smart Watch ⌚",
            "Online Course Subscription 📚"
        ]

    # -------------------------
    # Low income / young users
    # -------------------------
    else:
        recommendations = [
            "Discount Coupons 🎟️",
            "Budget Accessories 🎧",
            "Mobile Recharge Offers 📶",
            "Streaming Subscription 🎬"
        ]

    # -------------------------
    # Gender-based refinement
    # -------------------------
    if gender == "Female":
        recommendations.append("Fashion Deals 👗")
        recommendations.append("Beauty Products 💄")
    else:
        recommendations.append("Gadget Deals 🔧")

    # -------------------------
    # Subscription bonus
    # -------------------------
    if subscribed:
        recommendations.append("Loyalty Reward Bonus 🎁")

    return recommendations
