import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

class FeatureEngineer:
    def __init__(self):
        pass

    def prepare_data(self, df):
        """
        Add technical indicators and create target variable.
        """
        if df is None or df.empty:
            return None
            
        df = df.copy()
        
        # 1. RSI (14)
        rsi = RSIIndicator(close=df['Close'], window=14)
        df['RSI'] = rsi.rsi()
        
        # 2. Moving Averages
        sma20 = SMAIndicator(close=df['Close'], window=20)
        df['SMA_20'] = sma20.sma_indicator()
        
        sma50 = SMAIndicator(close=df['Close'], window=50)
        df['SMA_50'] = sma50.sma_indicator()
        
        # 3. Returns
        df['Returns'] = df['Close'].pct_change()
        
        # 4. Volume Change
        df['Volume_Change'] = df['Volume'].pct_change()
        
        # 5. Target: 1 if Close(t+3) > Close(t), else 0
        # We shift prediction target backwards because we want to predict FUTURE using CURRENT data
        # Target for row `i` is based on comparision between `i+3` and `i`
        df['Future_Close'] = df['Close'].shift(-3)
        df['Target'] = (df['Future_Close'] > df['Close']).astype(int)
        
        # Drop rows with NaNs created by indicators and shifting
        # We need to be careful not to drop the *last* rows if we want to run inference on them,
        # but for TRAINING we must have targets.
        
        # For training, drop all NaNs
        df_train = df.dropna().copy()
        
        return df, df_train

if __name__ == "__main__":
    # Mock data for testing
    data = {
        'Close': np.random.rand(100) * 100,
        'Volume': np.random.randint(100, 1000, 100),
        'Time': pd.date_range(start='1/1/2022', periods=100)
    }
    df = pd.DataFrame(data)
    fe = FeatureEngineer()
    full_df, train_df = fe.prepare_data(df)
    print("Full DF columns:", full_df.columns)
    print("Train DF shape:", train_df.shape)
