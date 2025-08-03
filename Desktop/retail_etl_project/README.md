Initial Configurations
========


- wsl
  - mkdir retail_etl_project
  - cd retail_etl_project
  - astro dev init
- Pycharm > File > Open -> Ubuntu > root > retail_etl_project > terminal:
  - m venv .venv
  - source .venv/bin/activate
  - pip install apache-airflow apache-airflow-core apache-airflow-providers-amazon==9.9.0 apache-airflow-providers-common-compat==1.7.1 apache-airflow-providers-common-io==1.6.0 apache-airflow-providers-common-sql==1.27.2 apache-airflow-providers-http==5.3.1 apache-airflow-providers-smtp==2.1.0 apache-airflow-providers-snowflake==6.4.0 apache-airflow-providers-standard==1.3.0 apache-airflow-task-sdk==1.0.2 boto3==1.38.44 botocore==1.38.44 jsonpath-ng==1.7.0 jsonschema==4.24.0 jsonschema-specifications==2025.4.1 numpy==1.26.4 pandas==2.1.4 pandera==0.24.0
snowflake-connector-python==3.15.0 snowflake-sqlalchemy==1.7.5 SQLAlchemy==1.4.54 SQLAlchemy-JSONField==1.0.2 SQLAlchemy-Utils==0.41.2 s3fs==2025.7.0 snowflake-connector-python==3.15.0 pyarrow==18.0.0
  - pip freeze > requirements.txt
  - deleting the versions of apache-airflow and apache-airflow-core in requirements.txt
  - Dockerfile > FROM astrocrpublic.azurecr.io/runtime:3.0-3
  - astro dev start
  
***

Snowflake:
================

CREATE DATABASE SALES_PRODUCTS_DB;



CREATE ROLE analyst_role;



CREATE SCHEMA IF NOT EXISTS SALES_PRODUCTS_DB.CLEANSED_LAYER;

CREATE SCHEMA IF NOT EXISTS SALES_PRODUCTS_DB.BUSINESS_LAYER;

CREATE SCHEMA IF NOT EXISTS SALES_PRODUCTS_DB.PRESENTATION_LAYER;


-- For bigger tasks
CREATE OR REPLACE WAREHOUSE snowflake_warehouse_manual
WITH
  WAREHOUSE_SIZE = 'LARGE',     
  AUTO_SUSPEND = 300,          
  AUTO_RESUME = TRUE;


GRANT USAGE ON DATABASE SALES_PRODUCTS_DB TO ROLE analyst_role;


GRANT USAGE ON WAREHOUSE COMPUTE_WH TO ROLE analyst_role;

GRANT USAGE ON WAREHOUSE snowflake_warehouse_manual TO ROLE analyst_role;


GRANT USAGE ON SCHEMA SALES_PRODUCTS_DB.CLEANSED_LAYER TO ROLE analyst_role;

GRANT USAGE ON SCHEMA SALES_PRODUCTS_DB.BUSINESS_LAYER TO ROLE analyst_role;

GRANT USAGE ON SCHEMA SALES_PRODUCTS_DB.PRESENTATION_LAYER TO ROLE analyst_role;




GRANT INSERT, SELECT
ON ALL TABLES IN SCHEMA SALES_PRODUCTS_DB.CLEANSED_LAYER TO ROLE analyst_role;

GRANT INSERT, SELECT
ON ALL TABLES IN SCHEMA SALES_PRODUCTS_DB.BUSINESS_LAYER TO ROLE analyst_role;

GRANT INSERT, SELECT
ON ALL TABLES IN SCHEMA SALES_PRODUCTS_DB.PRESENTATION_LAYER TO ROLE analyst_role;



CREATE TABLE SALES_PRODUCTS_DB.CLEANSED_LAYER.SALES_DATA (
    sales_id INTEGER,
    product_id INTEGER,
    region VARCHAR,
    quantity INTEGER,
    price DOUBLE,
    timestamp DATETIME,
    discount DOUBLE,
    order_status VARCHAR,
    total_sales DOUBLE
);


CREATE TABLE SALES_PRODUCTS_DB.CLEANSED_LAYER.PRODUCT_DATA (
    product_id INTEGER,
    category VARCHAR,
    brand VARCHAR,
    rating DOUBLE,
    in_stock BOOLEAN,
    launch_date DATETIME
);


CREATE TABLE SALES_PRODUCTS_DB.CLEANSED_LAYER.MERGED_DATA (
    sales_id INTEGER,
    product_id INTEGER,
    region VARCHAR,
    quantity INTEGER,
    price DOUBLE,
    timestamp DATETIME,
    discount DOUBLE,
    order_status VARCHAR,
    total_sales DOUBLE,
    category VARCHAR,
    brand VARCHAR,
    rating DOUBLE,
    in_stock BOOLEAN,
    launch_date DATETIME
);


CREATE TABLE SALES_PRODUCTS_DB.BUSINESS_LAYER.ENRICHED_DATA (
    sales_id INTEGER,
    product_id INTEGER,
    region VARCHAR,
    quantity INTEGER,
    price DOUBLE,
    timestamp DATETIME,
    discount DOUBLE,
    order_status VARCHAR,
    total_sales DOUBLE,
    category VARCHAR,
    brand VARCHAR,
    rating DOUBLE,
    in_stock BOOLEAN,
    launch_date DATETIME,
    month VARCHAR,
    weekday VARCHAR,
    hour INTEGER,
    sales_bucket VARCHAR
);


CREATE TABLE SALES_PRODUCTS_DB.PRESENTATION_LAYER.PEAK_HOURS_SALES_TRENDS (
    region VARCHAR,
    category VARCHAR,
    hour INTEGER,
    total_sales DOUBLE
);


CREATE TABLE SALES_PRODUCTS_DB.PRESENTATION_LAYER.PRODUCT_SALES_RANKING (
    product_id INTEGER,
    total_revenue DOUBLE,
    total_units_sold INTEGER,
    category VARCHAR,
    brand VARCHAR,
    rating DOUBLE,
    performance_tier VARCHAR
);


CREATE TABLE SALES_PRODUCTS_DB.PRESENTATION_LAYER.SEASONAL_SALES_PATTERNS (
    quarter VARCHAR,
    category VARCHAR,
    total_revenue DOUBLE,
    total_units_sold INTEGER
);


CREATE TABLE SALES_PRODUCTS_DB.PRESENTATION_LAYER.REVENUE_BY_REGION (
    region VARCHAR,
    total_revenue DOUBLE,
    revenue_share DOUBLE,
    cumulative_share DOUBLE
);


CREATE TABLE SALES_PRODUCTS_DB.PRESENTATION_LAYER.ORDER_STATUS_WEEKLY (
    week VARCHAR,
    Pending INTEGER,
    Shipped INTEGER,
    Returned INTEGER
);


GRANT ROLE analyst_role TO USER IKU;

USE ROLE analyst_role;



SELECT * FROM SALES_PRODUCTS_DB.CLEANSED_LAYER.SALES_DATA;

SELECT * FROM SALES_PRODUCTS_DB.CLEANSED_LAYER.PRODUCT_DATA;

SELECT * FROM SALES_PRODUCTS_DB.CLEANSED_LAYER.MERGED_DATA;



SELECT * FROM SALES_PRODUCTS_DB.BUSINESS_LAYER.ENRICHED_DATA;



SELECT * FROM SALES_PRODUCTS_DB.PRESENTATION_LAYER.PEAK_HOURS_SALES_TRENDS;

SELECT * FROM SALES_PRODUCTS_DB.PRESENTATION_LAYER.PRODUCT_SALES_RANKING;

SELECT * FROM SALES_PRODUCTS_DB.PRESENTATION_LAYER.SEASONAL_SALES_PATTERNS;

SELECT * FROM SALES_PRODUCTS_DB.PRESENTATION_LAYER.REVENUE_BY_REGION;

SELECT * FROM SALES_PRODUCTS_DB.PRESENTATION_LAYER.ORDER_STATUS_WEEKLY;