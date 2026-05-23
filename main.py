from src.extract import fetch_crypto_data
from src.transform import clean_and_transform
from src.load import load_to_database
import logging

def run_etl_pipeline():
    logging.info("Starting ETL Pipeline...")
    
    # Extract
    raw_data = fetch_crypto_data(limit=100)
    
    # Transform
    transformed_data = clean_and_transform(raw_data)
    
    # Load
    load_to_database(transformed_data)
    
    logging.info("ETL Pipeline finished successfully.")

if __name__ == "__main__":
    run_etl_pipeline()
