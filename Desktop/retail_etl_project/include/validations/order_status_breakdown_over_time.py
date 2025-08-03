import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, Check

order_status_breakdown_over_time_schema = pa.DataFrameSchema({
    "week": Column(str),
    "Pending": Column(int, Check.ge(0), nullable=False),
    "Shipped": Column(int, Check.ge(0), nullable=False),
    "Returned": Column(int, Check.ge(0), nullable=False),
})

def validate_order_status_output_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the output of the order_status_breakdown_over_time function against a predefined schema.
    """
    return order_status_breakdown_over_time_schema.validate(df)