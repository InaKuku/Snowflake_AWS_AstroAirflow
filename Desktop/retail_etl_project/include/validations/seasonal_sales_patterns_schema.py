import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, Check

seasonal_sales_patterns_schema = pa.DataFrameSchema({
        "quarter": Column(str),
        "category": Column(str),
        "total_revenue": Column(float, Check.greater_than(0)),
        "total_units_sold": Column(int, Check.greater_than(0))
})


def validate_seasonal_sales_patterns_output_schema(agg_df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the output of the seasonal_sales_patterns function against a predefined schema.
    """
    return seasonal_sales_patterns_schema.validate(agg_df)