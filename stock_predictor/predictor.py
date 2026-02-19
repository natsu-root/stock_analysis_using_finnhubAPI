import pandas as pd
import numpy as np
from data_fetcher import DataFetcher
from feature_engineering import FeatureEngineer
from model import ModelTrainer
import os

class StockPredictor:
    def __init__(self, api_key=None):
        self.fetcher = DataFetcher(api_key)
        self.fe = FeatureEngineer()
        self.trainer = ModelTrainer()
        self.model_path = 'trained_model.pkl'

    def analyze_stock(self, symbol):
        """
        Full pipeline: Fetch -> Feature Eng -> Train/Load Model -> Predict
        """
        # 1. Fetch Data
        try:
            df = self.fetcher.fetch_candles(symbol, count=300) # Fetch enough for indicators
            if df is None:
                return {'error': 'No data returned from API (Check symbol or date range)'}
        except Exception as e:
            return {'error': str(e)}
            
        # 2. Feature Engineering
        full_df, train_df = self.fe.prepare_data(df)
        
        if train_df.empty:
             return {'error': 'Not enough data for indicators'}

        # 3. Train Model (In a real app, we might load a pre-trained model or retrain periodically)
        # For this dashboard, we'll retrain on the historical data of the specific stock 
        # to adapt to its specific behavior (simplification).
        model, acc = self.trainer.train(train_df)
        
        # 4. Predict on latest data
        # We need the *latest* row that has all indicators calculated
        # The 'full_df' has NaN targets for the last 3 rows (because of shift(-3))
        # But it HAS indicators for those rows.
        last_row = full_df.iloc[[-1]] 
        
        # Check if last_row has NaNs in features (it shouldn't if we have enough history)
        if last_row[self.trainer.features].isnull().values.any():
             return {'error': 'Latest data insufficient for indicators'}

        prob = self.trainer.predict_proba(last_row)[0]
        
        # 5. Logic
        signal = "HOLD"
        if prob > 0.6:
            signal = "BUY"
        elif prob < 0.4:
            signal = "SELL"
            
        return {
            'symbol': symbol,
            'current_price': last_row['Close'].values[0],
            'probability': prob,
            'signal': signal,
            'data': full_df, # sending full data for plotting
            'latest_time': last_row['Time'].values[0],
            'accuracy': acc
        }

if __name__ == "__main__":
    predictor = StockPredictor()
    result = predictor.analyze_stock('AAPL')
    if 'error' not in result:
        print(f"Prediction for {result['symbol']}: {result['signal']} ({result['probability']:.2f})")
    else:
        print(result['error'])
