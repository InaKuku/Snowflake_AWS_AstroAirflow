import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, Check

peak_hours_sales_trends_output_schema = pa.DataFrameSchema({
        "region": Column(str),
        "category": Column(str),
        "hour": Column(int, pa.Check.in_range(0, 23)),
        "total_sales": Column(float, Check.greater_than(0))
})


def validate_peak_hours_sales_trends_output_schema(enriched_df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates the output of the peak sales hour table (for each region and category) against a predefined schema.
    """
    return peak_hours_sales_trends_output_schema.validate(enriched_df)