import pandas as pd
import logging

def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the raw data and applies necessary transformations.
    """
    if df.empty:
        logging.warning("Empty DataFrame received. Skipping transformation.")
        return df

    logging.info("Transforming data...")
    
    # Select relevant columns
    cols_to_keep = ['id', 'symbol', 'name', 'current_price', 'market_cap', 
                    'market_cap_rank', 'total_volume', 'high_24h', 'low_24h', 'last_updated']
    
    # Ensure columns exist before filtering
    available_cols = [col for col in cols_to_keep if col in df.columns]
    df_clean = df[available_cols].copy()
    
    # Handle missing values
    df_clean.fillna(0, inplace=True)
    
    # Add a derived column for price spread
    if 'high_24h' in df_clean.columns and 'low_24h' in df_clean.columns:
        df_clean['price_spread_24h'] = df_clean['high_24h'] - df_clean['low_24h']
    
    # Convert 'last_updated' to datetime
    if 'last_updated' in df_clean.columns:
        df_clean['last_updated'] = pd.to_datetime(df_clean['last_updated'])
        
    logging.info(f"Transformation complete. Resulting shape: {df_clean.shape}")
    return df_clean
