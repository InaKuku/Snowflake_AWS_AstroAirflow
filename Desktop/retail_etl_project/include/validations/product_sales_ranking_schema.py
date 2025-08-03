import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, Check

product_sales_ranking_schema = pa.DataFrameSchema({
    "product_id": Column(int),
    "total_revenue": Column(float, Check.greater_than(0)),
    "total_units_sold": Column(int, Check.greater_than(0)),
    "category": Column(str),
    "brand": Column(str),
    "rating": Column(float),
    "performance_tier": Column(str, Check.isin(["Low Performer", "Average", "Bestseller"]))
})


def validate_product_performance_output_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the output of the product performance dataset against a predefined schema.
    """
    return product_sales_ranking_schema.validate(df)