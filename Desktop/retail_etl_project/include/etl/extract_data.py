import io
import logging
import pandas as pd

from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.sdk.bases.operator import AirflowException

logger = logging.getLogger(__name__)


def extract_data_from_s3(bucket: str, folder: str, aws_conn_id: str, file_type: str = "csv") -> dict:
    """
    Extract files of a specified type from an s3 bucket provided and loads them into a pandas dataframe
    """
    logger.info(f"Connection to S3 bucket {bucket} using connection id {aws_conn_id}")
    s3_hook = S3Hook(aws_conn_id=aws_conn_id)
    keys = s3_hook.list_keys(bucket_name=bucket, prefix=folder)

    if not keys:
        logger.error(f"No files found in bucket {bucket} with prefix {folder}")
        raise AirflowException(f"No files found in bucket {bucket} with prefix {folder}")

    dfs = {}
    logger.info(f"Found {len(keys)} files in bucket {bucket}/{folder}")
    for key in keys:
        if not key.lower().endswith(f".{file_type}"):
            continue

        logger.info(f"Processing file {key}")
        s3_obj = s3_hook.get_key(key=key, bucket_name=bucket)
        content = s3_obj.get()['Body'].read().decode('utf-8')

        try:
            if file_type == "csv":
                df = pd.read_csv(io.StringIO(content))
            elif file_type == "json":
                df = pd.read_json(io.StringIO(content))
            else:
                logger.error(f"Unsupported file type: {file_type}")
                raise AirflowException(f"Unsupported file type: {file_type}")
        except Exception:
            logger.exception(f"Failed to load {file_type} file from {key}")
            raise

        dfs[key] = df
    logger.info(f"Successfully loaded {len(dfs)} file from {file_type} file")
    return dfs