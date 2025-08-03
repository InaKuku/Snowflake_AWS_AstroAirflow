import logging
import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, Check
from pandera.errors import SchemaError

logger = logging.getLogger(__name__)

product_input_schema = pa.DataFrameSchema({
    "product_id": Column(int),
    "category": Column(str),
    "brand": Column(str),
    "rating": Column(float),
    "in_stock": Column(pa.Bool, required=False, nullable=True),
    "launch_date": Column(str, required=False, nullable=True),
})

product_output_schema = pa.DataFrameSchema({
    "product_id": Column(int),
    "category": Column(str, Check(lambda s: s.str.islower())),
    "brand": Column(str, Check(lambda s: s.str.isupper())),
    "rating": Column(float),
    "in_stock": Column(pa.Bool, required=False, nullable=False), # all df null values should be dropped
    "launch_date": Column(pa.DateTime, required=False, nullable=False),   # all df null values should be dropped
})

def validate_input_product_schema(product_df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the input products DataFrame against a predefined schema.
    """
    try:
        return product_input_schema.validate(product_df)
    except SchemaError as e:
        logger.error(f"Pre-products schema validation failed: {e.failure_cases}")
        return product_df

def validate_output_product_schema(product_df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the output of the transformations done in transform_products_data(products_df) against a predefined schema.
    """
    return product_output_schema.validate(product_df)