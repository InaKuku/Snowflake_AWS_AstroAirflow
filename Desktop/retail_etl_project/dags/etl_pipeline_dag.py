import pandas as pd
from airflow.decorators import dag, task, task_group
from airflow.utils import yaml
from pendulum import datetime

from include.etl.extract_data import extract_data_from_s3
from include.etl.transform_data import transform_sales_data, transform_products_data, merge_sales_and_products, \
    enrich_merged_data, peak_hours_sales_trends_by_region_category, product_sales_ranking, seasonal_sales_patterns, \
    revenue_concentration_by_region, order_status_breakdown_over_time
from include.etl.load_data import load_data_to_snowflake

with open("include/config.yaml") as file:
    config = yaml.safe_load(file)

@dag(
    schedule=None,
    start_date=datetime(year=2025, month=1, day=1),
    catchup=False,
    tags=['retail'],
)
def retail_etl_pipeline():

    @task_group(group_id="extract_group")
    def extract_group():
        @task()
        def extract_csv_data(bucket: str, folder: str, aws_conn_id: str) -> dict:
            return extract_data_from_s3(bucket=bucket, folder=folder, aws_conn_id=aws_conn_id, file_type="csv")
        @task()
        def extract_json_data(bucket: str, folder: str, aws_conn_id: str) -> dict:
            return extract_data_from_s3(bucket=bucket, folder=folder, aws_conn_id=aws_conn_id, file_type="json")

        @task()
        def get_sales_file(files: dict) -> str:
            for key, df in files.items():
                if "sales" in key:
                    return df.to_json(orient="split", date_format="iso")
            raise AirflowException("Sales file not found")


        @task()
        def get_products_file(files: dict) -> str:
            for key, df in files.items():
                if "product" in key:
                    return df.to_json(orient="split", date_format="iso")
            raise AirflowException("Product file not found")

        sales_file = extract_csv_data(bucket=config["s3"]["bucket"], folder=config["s3"]["folder"], aws_conn_id=config["aws_conn_id"])
        products_file = extract_json_data(bucket=config["s3"]["bucket"], folder=config["s3"]["folder"], aws_conn_id=config["aws_conn_id"])
        sales_json = get_sales_file(sales_file)
        products_json = get_products_file(products_file)

        return {"sales_json": sales_json, "products_json": products_json}


    @task_group(group_id="transform_group")
    def transform_group(sales_json: str, products_json: str):
        @task()
        def transform_sales_data_task(sales_json: str) -> str:
            sales_df = pd.read_json(sales_json, orient="split")
            sales_df = transform_sales_data(sales_df)
            return sales_df.to_json(orient="split", date_format="iso")

        @task()
        def transform_products_data_task(products_json: str) -> str:
            product_df = pd.read_json(products_json, orient="split")
            cleaned_product_df = transform_products_data(product_df)
            return cleaned_product_df.to_json(orient="split", date_format="iso")

        @task()
        def merge_data_task(sales_json_cleaned: str, products_json_cleaned: str) -> str:
            sales_df = pd.read_json(sales_json_cleaned, orient="split")
            product_df = pd.read_json(products_json_cleaned, orient="split")
            merge_df = merge_sales_and_products(sales_df, product_df)
            return merge_df.to_json(orient="split", date_format="iso")

        @task()
        def enrich_data_task(merged_json: str) -> str:
            merged_df = pd.read_json(merged_json, orient="split")
            enriched_df = enrich_merged_data(merged_df)
            return enriched_df.to_json(orient="split", date_format="iso")

        cleansed_sales = transform_sales_data_task(sales_json)
        cleansed_products = transform_products_data_task(products_json)
        merged = merge_data_task(cleansed_sales, cleansed_products)
        enriched = enrich_data_task(merged)
        return {"cleansed_sales": cleansed_sales, "cleansed_products": cleansed_products, "merged": merged, "enriched": enriched}


    @task_group(group_id="analytics_group")
    def analytics_group(sales_json_cleaned: str, products_json_cleaned: str, merged_json: str, enriched_json: str):
        @task()
        def peak_hours_sales_trends_by_region_category_task(enriched_json: str) -> str:
            enriched_df = pd.read_json(enriched_json, orient="split")
            enriched_df = peak_hours_sales_trends_by_region_category(enriched_df)
            return enriched_df.to_json(orient="split", date_format="iso")

        @task()
        def product_sales_ranking_task(sales_json_cleaned: str, products_json_cleaned: str) -> str:
                sales_df = pd.read_json(sales_json_cleaned, orient="split")
                product_df = pd.read_json(products_json_cleaned, orient="split")
                aggregated_df = product_sales_ranking(sales_df, product_df)
                return aggregated_df.to_json(orient="split", date_format="iso")

        @task()
        def seasonal_sales_patterns_task(merged_json: str) -> str:
            merged_df = pd.read_json(merged_json, orient="split")
            aggregated_q_df = seasonal_sales_patterns(merged_df)
            return aggregated_q_df.to_json(orient="split")

        @task()
        def revenue_concentration_by_region_task(merged_json: str) -> str:
            merged_df = pd.read_json(merged_json, orient="split")
            region_revenue_df = revenue_concentration_by_region(merged_df)
            return region_revenue_df.to_json(orient="split")

        @task()
        def order_status_breakdown_over_time_task(sales_json_cleaned: str) -> str:
                sales_df = pd.read_json(sales_json_cleaned, orient="split")
                breakd_df = order_status_breakdown_over_time(sales_df)
                return breakd_df.to_json(orient="split")



        peak_hours_sales_df = peak_hours_sales_trends_by_region_category_task(enriched_json)
        product_sales_df = product_sales_ranking_task(sales_json_cleaned, products_json_cleaned)
        seasonal_sales_df = seasonal_sales_patterns_task(merged_json)
        revenue_by_region_df = revenue_concentration_by_region_task(merged_json)
        order_status_df = order_status_breakdown_over_time_task(sales_json_cleaned)
        return {"peak_hours_sales_df": peak_hours_sales_df, "product_sales_df": product_sales_df, "seasonal_sales_df": seasonal_sales_df, \
                "revenue_by_region_df": revenue_by_region_df, "order_status_df": order_status_df}

    @task_group(group_id="load_group")
    def load_group(final_sales_json: str, final_products_json: str, final_merged_json, final_enriched_json, \
                   final_peak_hours_json: str, final_products_ranking_json: str, final_seasonal_patterns_json: str, \
                   final_revenue_region_json, final_order_status_json):
        @task()
        def load_to_snowflake(final_json: str, database: str, schema: str, table_name: str, snowflake_conn_id: str):
            final_df = pd.read_json(final_json, orient="split")
            load_data_to_snowflake(final_df, database, schema, table_name)

        targets = config["snowflake"]["targets"]
        conn_id = config["snowflake"]["conn_id"]
        db = config["snowflake"]["database"]

        load_to_snowflake(final_json=final_sales_json, database=db,
                          schema=targets["sales"]["schema"], table_name=targets["sales"]["table"],
                          snowflake_conn_id=conn_id)
        load_to_snowflake(final_json=final_products_json, database=db,
                          schema=targets["products"]["schema"], table_name=targets["products"]["table"],
                          snowflake_conn_id=conn_id)
        load_to_snowflake(final_json=final_merged_json, database=db,
                          schema=targets["merged"]["schema"], table_name=targets["merged"]["table"],
                          snowflake_conn_id=conn_id)
        load_to_snowflake(final_json=final_enriched_json, database=db,
                          schema=targets["enriched"]["schema"], table_name=targets["enriched"]["table"],
                          snowflake_conn_id=conn_id)
        load_to_snowflake(final_json=final_peak_hours_json, database=db,
                          schema=targets["peak_hours"]["schema"], table_name=targets["peak_hours"]["table"],
                          snowflake_conn_id=conn_id)
        load_to_snowflake(final_json=final_products_ranking_json, database=db,
                          schema=targets["products_ranking"]["schema"], table_name=targets["products_ranking"]["table"],
                          snowflake_conn_id=conn_id)
        load_to_snowflake(final_json=final_seasonal_patterns_json, database=db,
                          schema=targets["seasonal_patterns"]["schema"], table_name=targets["seasonal_patterns"]["table"],
                          snowflake_conn_id=conn_id)
        load_to_snowflake(final_json=final_revenue_region_json, database=db,
                          schema=targets["revenue_region"]["schema"],
                          table_name=targets["revenue_region"]["table"],
                          snowflake_conn_id=conn_id)
        load_to_snowflake(final_json=final_order_status_json, database=db,
                          schema=targets["order_status"]["schema"],
                          table_name=targets["order_status"]["table"],
                          snowflake_conn_id=conn_id)


    extracted = extract_group()
    transformed = transform_group(extracted["sales_json"], extracted["products_json"])
    analytics = analytics_group(transformed["cleansed_sales"], transformed["cleansed_products"], transformed["merged"], transformed["enriched"])
    load_group(
        final_sales_json = transformed["cleansed_sales"],
        final_products_json = transformed["cleansed_products"],
        final_merged_json = transformed["merged"],
        final_enriched_json = transformed["enriched"],
        final_peak_hours_json = analytics["peak_hours_sales_df"],
        final_products_ranking_json = analytics["product_sales_df"],
        final_seasonal_patterns_json = analytics["seasonal_sales_df"],
        final_revenue_region_json = analytics["revenue_by_region_df"],
        final_order_status_json = analytics["order_status_df"]
        )

retail_etl_pipeline()
