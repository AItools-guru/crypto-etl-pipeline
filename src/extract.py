import requests
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_crypto_data(currency='usd', limit=50):
    """
    Fetches the top cryptocurrency data by market cap from CoinGecko API.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': currency,
        'order': 'market_cap_desc',
        'per_page': limit,
        'page': 1,
        'sparkline': False
    }
    
    logging.info(f"Fetching top {limit} cryptocurrencies in {currency.upper()}...")
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        logging.info("Successfully fetched data from CoinGecko.")
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return pd.DataFrame()
