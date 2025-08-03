import logging
import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, Check
from pandera.errors import SchemaError

logger = logging.getLogger(__name__)

sales_input_schema = pa.DataFrameSchema({
    "sales id": Column(int),
    "proDuct Id": Column(int),
    "Region": Column(str, nullable=True),
    "qty": Column(int),
    "Price": Column(float),
    "Time stamp": Column(str),
    "discount": Column(float),
    "order_status": Column(str)
})

sales_output_schema = pa.DataFrameSchema({
    "sales_id": Column(int),
    "product_id": Column(int),
    "region": Column(str),
    "quantity": Column(int, Check.greater_than(0)),
    "price": Column(float, Check.greater_than(0)),
    "timestamp": Column(pa.DateTime),
    "discount": Column(float, Check.greater_than_or_equal_to(0)),
    "order_status": Column(str),
    "total_sales": Column(float, Check.greater_than(0))
})

def validate_input_sales_schema(sales_df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the input sales DataFrame against a predefined schema.
    """
    try:
        return sales_input_schema.validate(sales_df)
    except SchemaError as e:
        logger.error(f"Pre-sales schema validation failed: {e.failure_cases}")
        return sales_df

def validate_output_sales_schema(sales_df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the output of the transformations done in transform_sales_data(sales_df) against a predefined schema.
    """
    return sales_output_schema.validate(sales_df)
