import os
import finnhub
import pandas as pd
import datetime
import time
from dotenv import load_dotenv

load_dotenv()

class DataFetcher:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("FINNHUB_API_KEY")
        self.use_mock = False
        if not self.api_key:
            print("Warning: No API key found. Using MOCK DATA mode.")
            self.use_mock = True
        else:
            self.client = finnhub.Client(api_key=self.api_key)

    def fetch_candles(self, symbol, resolution='D', count=200):
        """
        Fetch historical candle data from Finnhub or generate mock data.
        """
        if self.use_mock:
            return self._generate_mock_data(symbol, count)

        try:
            # Calculate start and end times
            end = int(time.time())
            # Approximate start time based on resolution (simplification for daily 'D')
            start = end - (count * 86400 * 2) 
            
            res = self.client.stock_candles(symbol, resolution, start, end)
            
            if res is None or res.get('s') == 'no_data':
                return None
                
            df = pd.DataFrame({
                'Time': pd.to_datetime(res['t'], unit='s'),
                'Open': res['o'],
                'High': res['h'],
                'Low': res['l'],
                'Close': res['c'],
                'Volume': res['v']
            })
            
            return df
            
        except Exception as e:
            print(f"Finnhub Error ({symbol}): {e}")
            print(f"Falling back to MOCK DATA for {symbol} due to API restriction/error.")
            return self._generate_mock_data(symbol, count)

    def _generate_mock_data(self, symbol, count):
        import numpy as np
        # Generate realistic-looking random stock data
        dates = pd.date_range(end=datetime.datetime.now(), periods=count)
        base_price = 150.0  # arbitrary base
        
        # Random walk
        changes = np.random.randn(count) * 2
        prices = base_price + np.cumsum(changes)
        
        # Ensure positive
        prices = np.maximum(prices, 1.0)
        
        df = pd.DataFrame({
            'Time': dates,
            'Open': prices + np.random.randn(count)*0.5,
            'High': prices + np.abs(np.random.randn(count)*1.0),
            'Low': prices - np.abs(np.random.randn(count)*1.0),
            'Close': prices,
            'Volume': np.random.randint(100000, 5000000, count)
        })
        return df

    def get_current_price(self, symbol):
        if self.use_mock:
            return 150.25
        try:
            quote = self.client.quote(symbol)
            return quote['c']
        except Exception as e:
            print(f"Error fetching quote for {symbol}: {e}")
            return None

if __name__ == "__main__":
    fetcher = DataFetcher()
    df = fetcher.fetch_candles('AAPL')
    if df is not None:
        print(df.tail())
        print(f"Current Price: {fetcher.get_current_price('AAPL')}")
