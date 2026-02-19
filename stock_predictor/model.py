import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np
import os
import joblib

class ModelTrainer:
    def __init__(self):
        self.model = xgb.XGBClassifier(
            objective='binary:logistic',
            n_estimators=100,
            learning_rate=0.1,
            max_depth=3,
            random_state=42,
            eval_metric='logloss'
        )
        self.features = ['RSI', 'SMA_20', 'SMA_50', 'Returns', 'Volume_Change']

    def train(self, df):
        """
        Train the XGBoost model.
        """
        X = df[self.features]
        y = df['Target']
        
        # Time-series split (no shuffle)
        # Use first 80% for train, last 20% for test to simulate real world scenario
        split_idx = int(len(df) * 0.8)
        X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
        y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]
        
        self.model.fit(X_train, y_train)
        
        # Evaluate
        preds = self.model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"Model Accuracy: {acc:.4f}")
        # print(classification_report(y_test, preds))
        
        return self.model, acc

    def save_model(self, path='model.pkl'):
        joblib.dump(self.model, path)
        
    def load_model(self, path='model.pkl'):
        if os.path.exists(path):
            self.model = joblib.load(path)
            return True
        return False

    def predict_proba(self, X):
        # inputs X should be a dataframe with the same feature columns
        return self.model.predict_proba(X[self.features])[:, 1]

if __name__ == "__main__":
    # Mock usage
    pass
