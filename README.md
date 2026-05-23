# Crypto ETL Data Pipeline

An End-to-End Automated Data Pipeline that extracts live cryptocurrency market data, transforms it for analysis, and loads it into a local SQLite database.

## Architecture

1. **Extract**: Pulls top cryptocurrencies by market cap from the [CoinGecko API](https://www.coingecko.com/en/api).
2. **Transform**: Cleans the data using `pandas`, handles missing values, and engineers new features (e.g., `price_spread_24h`).
3. **Load**: Inserts the cleaned data into a `SQLite` database using `sqlalchemy` for downstream analytics.

## Tech Stack
- Python 3.10+
- Pandas
- SQLAlchemy
- SQLite
- Requests

## How to Run

1. Clone the repository and navigate to the folder:
   ```bash
   cd crypto-etl-pipeline
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the pipeline:
   ```bash
   python main.py
   ```

## Output
The pipeline will generate a `data/crypto_data.db` SQLite database file. You can query the `market_data` table to analyze the data.
