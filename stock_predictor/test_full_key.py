from data_fetcher import DataFetcher
import sys

key = "d6bg6upr01qp4lhvamo0d6bg6upr01qp4lhvamog"

print(f"Testing Full Key: {key}")
try:
    fetcher = DataFetcher(api_key=key)
    fetcher.use_mock = False 
    
    quote = fetcher.client.quote('AAPL')
    print(f"Quote Result: {quote}")
    
    if quote and quote['c'] != 0:
            print(f"✅ SUCCESS with full key")
            sys.exit(0)
    else:
            print(f"❌ FAILED with full key")
except Exception as e:
    print(f"❌ FAILED with full key - Error: {e}")

sys.exit(1)
