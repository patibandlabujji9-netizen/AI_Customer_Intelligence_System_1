# utils/column_mapper.py

COLUMN_MAPPING = {

    "sales": "Sales",

    "revenue": "Sales",

    "qty": "Quantity",

    "region_name": "Region",

    "product_name": "Product"
}


def map_columns(df):

    df = df.rename(
        columns=COLUMN_MAPPING
    )

    return df