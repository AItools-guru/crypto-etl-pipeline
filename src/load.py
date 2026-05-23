import pandas as pd
from sqlalchemy import create_engine
import logging
import os

def load_to_database(df: pd.DataFrame, db_name='crypto_data.db', table_name='market_data'):
    """
    Loads the transformed data into a SQLite database.
    """
    if df.empty:
        logging.warning("Empty DataFrame received. Skipping database load.")
        return

    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    db_path = f'sqlite:///data/{db_name}'
    
    logging.info(f"Connecting to database at {db_path}...")
    engine = create_engine(db_path)
    
    try:
        # Write records stored in a DataFrame to a SQL database.
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Successfully loaded {len(df)} rows into table '{table_name}'.")
    except Exception as e:
        logging.error(f"Failed to load data into database: {e}")
