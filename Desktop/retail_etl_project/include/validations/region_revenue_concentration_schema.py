import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, Check

region_revenue_concentration_schema = pa.DataFrameSchema({
    "region": Column(str),
    "total_revenue": Column(float, Check.greater_than(0)),
    "revenue_share": Column(float, Check.in_range(0, 1)),
    "cumulative_share": Column(float, Check.in_range(0, 1))
})

def validate_region_revenue_concentration_output_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the output of the revenue_concentration_by_region function against a predefined schema.
    """
    return region_revenue_concentration_schema.validate(df)