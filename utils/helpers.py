def format_currency(value):
    return f"${value:,.2f}"


def risk_level(prob):
    if prob < 30:
        return "Low Risk"
    elif prob < 70:
        return "Medium Risk"
    else:
        return "High Risk"