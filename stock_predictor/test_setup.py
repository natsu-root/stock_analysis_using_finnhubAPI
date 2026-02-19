import sys
import os
import pandas as pd
import numpy as np

# Add current directory to path
sys.path.append(os.getcwd())

from feature_engineering import FeatureEngineer
from model import ModelTrainer
from predictor import StockPredictor

def test_feature_engineering():
    print("Testing Feature Engineering...")
    # Create dummy data
    dates = pd.date_range(start='2023-01-01', periods=100)
    data = {
        'Time': dates,
        'Open': np.random.rand(100) * 100,
        'High': np.random.rand(100) * 100,
        'Low': np.random.rand(100) * 100,
        'Close': np.random.rand(100) * 100,
        'Volume': np.random.randint(100, 1000, 100)
    }
    df = pd.DataFrame(data)
    
    fe = FeatureEngineer()
    full_df, train_df = fe.prepare_data(df)
    
    assert 'RSI' in full_df.columns
    assert 'SMA_20' in full_df.columns
    assert 'Target' in train_df.columns
    print("Feature Engineering: PASSED")

def test_model_training():
    print("Testing Model Training...")
    # Create dummy data with features
    features = ['RSI', 'SMA_20', 'SMA_50', 'Returns', 'Volume_Change']
    data = {
        'Target': np.random.randint(0, 2, 100)
    }
    for f in features:
        data[f] = np.random.rand(100)
        
    df = pd.DataFrame(data)
    
    mt = ModelTrainer()
    model, acc = mt.train(df)
    
    assert model is not None
    assert 0 <= acc <= 1
    print("Model Training: PASSED")

def test_predictor_mock():
    print("Testing Predictor (Mock)...")
    # We can't easily test the full fetch without an API key, 
    # but we can test if the predictor class instantiates and has methods
    predictor = StockPredictor(api_key="dummy_key")
    assert hasattr(predictor, 'analyze_stock')
    print("Predictor Instantiation: PASSED")

if __name__ == "__main__":
    try:
        test_feature_engineering()
        test_model_training()
        test_predictor_mock()
        print("\nALL SYSTEM TESTS PASSED ✅")
    except Exception as e:
        print(f"\nTEST FAILED ❌: {e}")
        sys.exit(1)
