def calculate_inventory_metrics(
    avg_demand,
    lead_time=7,
    safety_factor=0.25
):

    safety_stock = (
        avg_demand *
        safety_factor
    )

    reorder_point = (
        avg_demand *
        lead_time
    ) + safety_stock

    return {
        "safety_stock": round(safety_stock, 2),
        "reorder_point": round(reorder_point, 2)
    }