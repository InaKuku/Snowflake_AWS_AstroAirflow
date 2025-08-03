import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column

merge_output_schema = pa.DataFrameSchema({
    "sales_id": Column(int),
    "product_id": Column(int),
    "region": Column(str),
    "quantity": Column(int),
    "price": Column(float),
    "timestamp": Column(pa.DateTime),
    "discount": Column(float),
    "order_status": Column(str),
    "total_sales": Column(float),
    "category": Column(str),
    "brand": Column(str),
    "rating": Column(float),
    "in_stock": Column(pa.Bool, required=False, nullable=False),
    "launch_date": Column(pa.DateTime, required=False, nullable=False)
})

def validate_output_merge_schema(merge_df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the output of the merged sales_df with products_df against a predefined schema.
    """
    return merge_output_schema.validate(merge_df)