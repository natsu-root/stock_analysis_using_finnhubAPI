# 📈 Stock Analysis Using Finnhub API

An AI-powered stock price prediction dashboard that uses machine learning to forecast stock movements for the next 3 days. Built with XGBoost, Finnhub API, and Streamlit.

## 📚 Documentation

- **[Quick Start Guide](QUICKSTART.md)** - Get started in 5 minutes
- **[Full Documentation](DOCS.md)** - Complete documentation index
- **[Contributing Guidelines](CONTRIBUTING.md)** - How to contribute

## 🌟 Features

- **Real-time Stock Data**: Fetches live stock data from Finnhub API
- **AI-Powered Predictions**: Uses XGBoost machine learning model for price movement predictions
- **Technical Indicators**: Analyzes RSI, SMA (20 & 50), volume changes, and returns
- **Interactive Dashboard**: Beautiful Streamlit web interface with live charts
- **Multiple Stock Analysis**: Analyze multiple stocks simultaneously
- **Signal Generation**: Provides BUY, SELL, or HOLD signals based on predictions
- **Auto-refresh**: Option to automatically refresh data at configurable intervals
- **Mock Data Mode**: Works without API key using generated mock data for testing

## 📊 Technical Indicators Used

- **RSI (Relative Strength Index)**: Momentum indicator measuring speed and magnitude of price changes
- **SMA (Simple Moving Averages)**: 20-day and 50-day moving averages for trend analysis
- **Volume Changes**: Tracks trading volume variations
- **Returns**: Daily percentage price changes

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup Instructions

**Option 1: Quick Setup (Linux/Mac)**
```bash
./setup.sh
```

**Option 2: Manual Setup (All Platforms)**

1. **Clone the repository**
   ```bash
   git clone https://github.com/natsu-root/stock_analysis_using_finnhubAPI.git
   cd stock_analysis_using_finnhubAPI
   ```

2. **Install dependencies**
   ```bash
   cd stock_predictor
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   
   Get your free API key from [Finnhub.io](https://finnhub.io/)
   
   Create a `.env` file in the `stock_predictor` directory:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API key:
   ```
   FINNHUB_API_KEY=your_api_key_here
   ```

4. **Run the Dashboard**
   ```bash
   streamlit run dashboard.py
   ```
   
   The dashboard will open in your browser at `http://localhost:8501`

## 📖 Usage

### Running the Dashboard

```bash
cd stock_predictor
streamlit run dashboard.py
```

### Using the Interface

1. **Enter API Key**: You can enter your Finnhub API key in the sidebar, or it will use the key from `.env` file
2. **Add Stock Symbols**: Enter comma-separated stock symbols (e.g., `AAPL, MSFT, TSLA, NVDA`)
3. **Configure Refresh Rate**: Set auto-refresh interval (30-300 seconds)
4. **Analyze Stocks**: Click "Analyze All" to fetch data and generate predictions

### Command Line Usage

You can also use the predictor programmatically:

```python
from predictor import StockPredictor

predictor = StockPredictor(api_key='your_api_key')
result = predictor.analyze_stock('AAPL')

if 'error' not in result:
    print(f"Symbol: {result['symbol']}")
    print(f"Current Price: ${result['current_price']:.2f}")
    print(f"Signal: {result['signal']}")
    print(f"Confidence: {result['probability']:.2%}")
else:
    print(f"Error: {result['error']}")
```

## 📁 Project Structure

```
stock_analysis_using_finnhubAPI/
├── stock_predictor/
│   ├── dashboard.py            # Streamlit web dashboard
│   ├── predictor.py           # Main prediction pipeline
│   ├── data_fetcher.py        # Finnhub API integration
│   ├── feature_engineering.py # Technical indicators calculation
│   ├── model.py               # XGBoost model training
│   ├── requirements.txt       # Python dependencies
│   ├── .env.example          # Example environment variables
│   └── test_*.py             # Test scripts
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following:

```
FINNHUB_API_KEY=your_finnhub_api_key
```

### Model Parameters

The XGBoost model uses the following parameters (configurable in `model.py`):

- **objective**: binary:logistic
- **n_estimators**: 100
- **learning_rate**: 0.1
- **max_depth**: 3
- **eval_metric**: logloss

### Signal Thresholds

- **BUY**: Probability > 0.6 (60% confidence of price increase)
- **SELL**: Probability < 0.4 (60% confidence of price decrease)
- **HOLD**: Probability between 0.4 and 0.6

## 🎯 How It Works

1. **Data Fetching**: Retrieves 300 days of historical stock data from Finnhub API
2. **Feature Engineering**: Calculates technical indicators (RSI, SMA, volume changes)
3. **Model Training**: Trains XGBoost classifier on historical data with 80/20 train/test split
4. **Prediction**: Predicts if the stock price will increase in the next 3 days
5. **Signal Generation**: Generates BUY/SELL/HOLD signals based on prediction confidence

## 📊 Model Performance

The model reports accuracy on historical backtesting data. Performance varies by stock and market conditions.

**Note**: This is for educational purposes only. Predictions are probabilistic and should not be considered financial advice.

## 🛠️ Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **xgboost**: Gradient boosting machine learning
- **scikit-learn**: Machine learning utilities
- **ta**: Technical analysis library
- **streamlit**: Web dashboard framework
- **python-dotenv**: Environment variable management
- **finnhub-python**: Finnhub API client
- **plotly**: Interactive charting

## ⚠️ Important Notes

- **Free API Limits**: Finnhub free tier has rate limits. The app includes mock data mode as fallback.
- **Market Hours**: Real-time data is only available during market hours.
- **Educational Purpose**: This tool is for learning and experimentation, not financial advice.
- **Data Delay**: Free API may have delayed data.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Natsu**
- GitHub: [@natsu-root](https://github.com/natsu-root)

## 🙏 Acknowledgments

- [Finnhub API](https://finnhub.io/) for providing stock market data
- [XGBoost](https://xgboost.readthedocs.io/) for the machine learning framework
- [Streamlit](https://streamlit.io/) for the dashboard framework
- [TA-Lib](https://github.com/bukosabino/ta) for technical analysis indicators

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

**Disclaimer**: This software is for educational purposes only. Stock predictions are inherently uncertain. Do not use this as the sole basis for investment decisions. Always consult with a qualified financial advisor before making investment choices.
