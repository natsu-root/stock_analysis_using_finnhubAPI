# Documentation Index

Welcome to the Stock Analysis Using Finnhub API documentation! This page serves as a directory to all documentation resources.

## 📖 Main Documentation

### Getting Started
- **[README.md](README.md)** - Complete project overview, features, and detailed documentation
- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes with quick setup guide

### Project Information
- **[LICENSE](LICENSE)** - MIT License terms and conditions
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guidelines for contributing to the project

## 🏗️ Project Architecture

### Core Components

1. **Dashboard (`stock_predictor/dashboard.py`)**
   - Streamlit web interface
   - Real-time data visualization
   - Interactive stock analysis

2. **Predictor (`stock_predictor/predictor.py`)**
   - Main prediction pipeline
   - Orchestrates data fetching, feature engineering, and model prediction

3. **Data Fetcher (`stock_predictor/data_fetcher.py`)**
   - Finnhub API integration
   - Historical stock data retrieval
   - Mock data generation for testing

4. **Feature Engineering (`stock_predictor/feature_engineering.py`)**
   - Technical indicators calculation (RSI, SMA, Volume)
   - Target variable creation
   - Data preparation for ML

5. **Model (`stock_predictor/model.py`)**
   - XGBoost classifier training
   - Model evaluation
   - Prediction generation

## 📚 Key Concepts

### Technical Indicators

- **RSI (Relative Strength Index)**: Measures momentum, ranges 0-100
  - Above 70: Overbought
  - Below 30: Oversold

- **SMA (Simple Moving Average)**: Average price over a period
  - SMA 20: Short-term trend (20 days)
  - SMA 50: Medium-term trend (50 days)

- **Volume Change**: Trading volume variations
- **Returns**: Daily percentage price changes

### Machine Learning Model

- **Algorithm**: XGBoost (Gradient Boosting)
- **Task**: Binary Classification (Price Up vs Down)
- **Features**: RSI, SMA_20, SMA_50, Returns, Volume_Change
- **Target**: Whether price increases in next 3 days
- **Training**: 80/20 time-series split

### Signal Generation

```
Probability > 0.6  → BUY  (Bullish)
Probability < 0.4  → SELL (Bearish)
0.4 ≤ Probability ≤ 0.6 → HOLD (Neutral)
```

## 🔧 Configuration

### Environment Variables
Create `.env` file in `stock_predictor/` directory:
```
FINNHUB_API_KEY=your_api_key_here
```

### Model Parameters (in `model.py`)
```python
{
    'objective': 'binary:logistic',
    'n_estimators': 100,
    'learning_rate': 0.1,
    'max_depth': 3,
    'random_state': 42
}
```

## 🛠️ Installation Methods

### Method 1: Automated Setup Script
```bash
./setup.sh
```

### Method 2: Manual Installation
```bash
cd stock_predictor
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API key
streamlit run dashboard.py
```

### Method 3: Using setup.py
```bash
pip install -e .
cd stock_predictor
streamlit run dashboard.py
```

## 📊 Usage Examples

### Basic Usage
```python
from stock_predictor.predictor import StockPredictor

predictor = StockPredictor(api_key='your_key')
result = predictor.analyze_stock('AAPL')
print(f"Signal: {result['signal']}")
print(f"Confidence: {result['probability']:.2%}")
```

### Running the Dashboard
```bash
cd stock_predictor
streamlit run dashboard.py
```

Access at: http://localhost:8501

## 🧪 Testing

### Test Scripts
- `test_setup.py` - Verify installation and setup
- `test_full_key.py` - Test with full API key
- `verify_key.py` - Verify API key validity

### Running Tests
```bash
cd stock_predictor
python test_setup.py
python verify_key.py
```

## 🚨 Troubleshooting

### Common Issues

1. **API Rate Limits**
   - Free tier has limited requests
   - Use mock data mode for testing
   - Wait before retrying

2. **Missing Dependencies**
   - Run: `pip install -r requirements.txt`
   - Ensure Python 3.7+

3. **Invalid Stock Symbol**
   - Use valid ticker symbols
   - Check symbol on financial websites

4. **Data Issues**
   - Some stocks lack historical data
   - Try popular stocks (AAPL, MSFT, TSLA)

## 📞 Support & Community

- **Issues**: [GitHub Issues](https://github.com/natsu-root/stock_analysis_using_finnhubAPI/issues)
- **Source Code**: [GitHub Repository](https://github.com/natsu-root/stock_analysis_using_finnhubAPI)
- **Contributions**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## ⚖️ Legal & Disclaimer

This software is provided for **educational purposes only**. Stock market predictions are inherently uncertain and should not be used as the sole basis for investment decisions.

**Always**:
- Do your own research
- Consult qualified financial advisors
- Understand the risks involved
- Never invest more than you can afford to lose

See [LICENSE](LICENSE) for full terms.

## 🗺️ Roadmap

Potential future enhancements:
- Additional technical indicators (MACD, Bollinger Bands)
- Multiple time frame predictions
- Backtesting framework
- Alert notifications
- Portfolio tracking
- Model comparison tools
- More data sources

## 📝 Changelog

### Version 1.0.0 (Current)
- Initial release
- XGBoost prediction model
- Streamlit dashboard
- Finnhub API integration
- RSI, SMA, Volume indicators
- Mock data support
- Comprehensive documentation

---

**Last Updated**: February 2026  
**Version**: 1.0.0  
**Maintained by**: [@natsu-root](https://github.com/natsu-root)
