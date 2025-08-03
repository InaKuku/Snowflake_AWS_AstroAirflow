import logging
import pandas as pd

from include.validations.products_schema import validate_input_product_schema, validate_output_product_schema
from include.validations.sales_schema import validate_input_sales_schema, validate_output_sales_schema
from include.validations.merge_schema import validate_output_merge_schema
from include.validations.enriched_schema import validate_enrich_output_merge_schema
from include.validations.peak_hours_sales_trends_schema import validate_peak_hours_sales_trends_output_schema
from include.validations.product_sales_ranking_schema import validate_product_performance_output_schema
from include.validations.seasonal_sales_patterns_schema import validate_seasonal_sales_patterns_output_schema
from include.validations.region_revenue_concentration_schema import validate_region_revenue_concentration_output_schema
from include.validations.order_status_breakdown_over_time import validate_order_status_output_schema

logger = logging.getLogger(__name__)


def transform_sales_data(sales_df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and transforms raw sales data for further processing and analysis
    """
    logger.info("Starting sales data transformations.")
    sales_df = validate_input_sales_schema(sales_df)
    sales_df.columns = sales_df.columns.str.strip().str.lower().str.replace(' ', '_')
    sales_df["region"] = sales_df["region"].str.strip().str.lower()
    sales_df = sales_df.rename(columns={"time_stamp": "timestamp", "qty": "quantity"})
    sales_df = sales_df[(sales_df["price"] > 0) & (sales_df["quantity"] > 0)]
    sales_df = sales_df.drop_duplicates()
    sales_df["timestamp"] = pd.to_datetime(sales_df["timestamp"], errors='coerce')
    sales_df = sales_df.dropna()
    sales_df["total_sales"] = (sales_df["price"] * (1-sales_df["discount"])) * sales_df["quantity"]

    logger.info("Finished sales data transformations.")
    return validate_output_sales_schema(sales_df)



def transform_products_data(products_df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and transforms raw products data for further processing and analysis
    """
    logger.info("Starting products data transformations.")
    products_df = validate_input_product_schema(products_df)
    products_df.columns = products_df.columns.str.strip().str.lower().str.replace(' ', '_')
    products_df["brand"] = products_df["brand"].str.upper()
    products_df["category"] = products_df["category"].str.lower()
    products_df["launch_date"] = pd.to_datetime(products_df["launch_date"], errors='coerce')
    products_df = products_df.dropna()
    products_df = products_df.drop_duplicates()
    logger.info("Finished products data transformations.")
    return validate_output_product_schema(products_df)


def merge_sales_and_products(sales_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merges two pandas DataFrames, sales_df and products_df, and validates the output.
    """
    logger.info("Merging sales data and products data.")
    merge_df = sales_df.merge(products_df, on="product_id", how="inner")
    merge_df["launch_date"] = pd.to_datetime(merge_df["launch_date"], errors="coerce") # During merging Pandas cast it to object
    logger.info("Finished merging sales data and products data.")
    return validate_output_merge_schema(merge_df)


def enrich_merged_data(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Takes the merged DataFrame and adds several new columns by exracting month, weekday, and an hour
    from the timestamp column and categorizes sales into buckets
    """
    logger.info("Enriching merged data")
    merged_df["month"] = merged_df["timestamp"].dt.to_period('M').astype(str)
    merged_df["weekday"] = merged_df["timestamp"].dt.day_name()
    merged_df["hour"] = merged_df["timestamp"].dt.hour.astype("int64")
    merged_df["sales_bucket"] = pd.cut(
        merged_df["total_sales"],
        bins=[0, 100, 500, float("inf")],
        labels=["Low", "Medium", "High"],
    )
    merged_df["launch_date"] = pd.to_datetime(merged_df["launch_date"], errors="coerce") # During enriching Pandas cast it to object
    logger.info("Finished enriching merged data.")
    enrich_df = validate_enrich_output_merge_schema(merged_df)
    return enrich_df


def peak_hours_sales_trends_by_region_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates enriched data to identify the single peak sales hour for each region–category pair.
    """
    logger.info("Calculating peak hours sales trends by category and region.")
    hourly_sales = df.groupby(["region", "category", "hour"])[["total_sales"]].sum().reset_index()
    peak_hours = (
        hourly_sales
            .sort_values(["region", "category", "total_sales"], ascending=[True, True, False])
            .groupby(["region", "category"], as_index=False)
            .first()
    )

    logger.info("Finished calculating peak hours sales trends by category and region.")

    return validate_peak_hours_sales_trends_output_schema(peak_hours)


def product_sales_ranking(sales_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    """
    - Shows total revenue and units sold for each product.
    - Merges with products metadata (category, brand, rating).
    - Classifies products into performance tiers using defined revenue ranges.
    """
    logger.info("Calculating product_sales_ranking.")
    agg_sales_by_product = (
        sales_df.groupby("product_id", as_index=False)
            .agg(
            total_revenue=("total_sales", "sum"),
            total_units_sold=("quantity", "sum")
        )
    )

    agg_sales_product_metadata = agg_sales_by_product.merge(
        products_df[["product_id", "category", "brand", "rating"]].drop_duplicates(),
        on="product_id",
        how="left"
    )

    agg_sales_product_metadata["performance_tier"] = pd.cut(
        agg_sales_product_metadata["total_revenue"],
        bins=[0, 20000, 50000, float("inf")],
        labels=["Low Performer", "Average", "Bestseller"]
    )

    logger.info("Finished calculating product_sales_ranking.")
    return validate_product_performance_output_schema(agg_sales_product_metadata)


def seasonal_sales_patterns(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates quarterly sales by product category
    """
    logger.info("Calculating seasonal_sales_patterns.")
    merged_df["quarter"] = merged_df["timestamp"].dt.to_period("Q").astype(str)
    seasonal_sales = (
        merged_df.groupby(["quarter", "category"], as_index=False)
            .agg(
            total_revenue=("total_sales", "sum"),
            total_units_sold=("quantity", "sum")
        )
    )
    logger.info("Finished calculating seasonal_sales_patterns.")
    return validate_seasonal_sales_patterns_output_schema(seasonal_sales)



def revenue_concentration_by_region(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    - Aggregates revenue by region
    - Calculates revenue share of each region
    - Sorts by revenue (descending) and compute cumulative share
    """
    logger.info("Calculating revenue_concentration_by_region.")
    revenue_by_region = (
        merged_df.groupby("region", as_index=False)
            .agg(total_revenue=("total_sales", "sum"))
    )

    total_revenue = revenue_by_region["total_revenue"].sum()
    revenue_by_region["revenue_share"] = revenue_by_region["total_revenue"] / total_revenue
    revenue_by_region = revenue_by_region.sort_values("total_revenue", ascending=False)
    revenue_by_region["cumulative_share"] = revenue_by_region["revenue_share"].cumsum()
    logger.info("Finished calculating revenue_concentration_by_region.")
    return validate_region_revenue_concentration_output_schema(revenue_by_region)


def order_status_breakdown_over_time(sales_df: pd.DataFrame) -> pd.DataFrame:
    """
    - Extracts the week from the timestamp
    - Groups by week and order_status, counting orders
    - Pivot to have each status as a column
    """
    logger.info("Calculating order_status_breakdown_over_time.")
    sales_df["week"] = sales_df["timestamp"].dt.to_period("W").astype(str)

    status_counts = (
        sales_df.groupby(["week", "order_status"])
        .size()
        .reset_index(name="order_count")
    )

    pivot_df = status_counts.pivot(index="week", columns="order_status", values="order_count").fillna(0).reset_index()
    cols_to_int = [col for col in pivot_df.columns if col != "week"]
    pivot_df[cols_to_int] = pivot_df[cols_to_int].astype(int)
    logger.info("Finished calculating order_status_breakdown_over_time.")
    return validate_order_status_output_schema(pivot_df)

