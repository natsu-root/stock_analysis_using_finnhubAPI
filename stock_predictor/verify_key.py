from data_fetcher import DataFetcher
import sys

try:
    fetcher = DataFetcher()
    print(f"Testing Key: {fetcher.api_key}")
    df = fetcher.fetch_candles('AAPL', count=5)
    if df is not None and not df.empty:
        print("SUCCESS: Data fetched successfully!")
        print(df.head())
    else:
        print("FAILURE: No data returned.")
except Exception as e:
    print(f"ERROR: {e}")
