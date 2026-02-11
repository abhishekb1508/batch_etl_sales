import pandas as pd
from transform import transform_sales_data
from validation import validate_sales_data
from load import load_raw_data, load_processed_data
from logging_config import get_logger

logger = get_logger(__name__)

def run_pipeline():
    logger.info("ETL Pipeline started")

    df_raw = pd.read_csv("data/sales_raw.csv")
    load_raw_data(df_raw)

    df_processed = transform_sales_data(df_raw)
    validate_sales_data(df_processed)
    load_processed_data(df_processed)

    logger.info("ETL Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
