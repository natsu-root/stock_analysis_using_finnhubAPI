from data_fetcher import DataFetcher
import sys
import finnhub

# Combinations to test
keys = [
    "d6bg6upr01qp4lhvamo0", # First part
    "d6bg6upr01qp4lhvamog", # Second part
]

for k in keys:
    print(f"\n--- Testing Key: {k} ---")
    try:
        # Override key
        fetcher = DataFetcher(api_key=k)
        fetcher.use_mock = False 
        
        # Test 1: Quote (Simplest, usually free)
        print("Attempting to fetch QUOTE for AAPL...")
        quote = fetcher.client.quote('AAPL')
        print(f"Quote Result: {quote}")
        
        if quote and quote['c'] != 0:
             print(f"✅ QUOTE SUCCESS with key: {k}")
        else:
             print(f"⚠️ QUOTE returned generic/empty data.")

        # Test 2: Candles
        print("Attempting to fetch CANDLES for AAPL...")
        df = fetcher.fetch_candles('AAPL', count=5)
        if df is not None and not df.empty:
            print(f"✅ CANDLES SUCCESS with key: {k}")
            # If we get here, this is the winning key
            with open('.env', 'w') as f:
                f.write(f"FINNHUB_API_KEY={k}")
            print("Updated .env with working key.")
            sys.exit(0)
        else:
             print(f"❌ CANDLES FAILED (No Data) with key: {k}")
             
    except Exception as e:
        print(f"❌ FAILED with key: {k}")
        print(f"Error Details: {e}")

print("\nAll keys failed to fetch candles.")
sys.exit(1)
