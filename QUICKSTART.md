# Quick Start Guide

Get up and running with Stock Analysis in 5 minutes!

## 🚀 Quick Installation

### Option 1: Automated Setup (Linux/Mac)

```bash
./setup.sh
```

### Option 2: Manual Setup (All Platforms)

```bash
# 1. Navigate to the project directory
cd stock_predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up API key
cp .env.example .env
# Edit .env and add your Finnhub API key

# 4. Run the dashboard
streamlit run dashboard.py
```

## 🔑 Getting Your API Key

1. Visit [Finnhub.io](https://finnhub.io/)
2. Sign up for a free account
3. Copy your API key from the dashboard
4. Paste it into the `.env` file

## 🎯 First Analysis

1. Open the dashboard at `http://localhost:8501`
2. Enter your API key in the sidebar (or it will use the .env file)
3. Keep the default stock symbols or add your own
4. Click "Analyze All"
5. View predictions, charts, and signals!

## 📊 Understanding the Signals

- **BUY 🟢**: Model predicts price will increase (>60% confidence)
- **SELL 🔴**: Model predicts price will decrease (>60% confidence)
- **HOLD 🟡**: Uncertain prediction (40-60% confidence)

## 💡 Tips

- Free API has rate limits - use mock data mode for testing
- Best results with stocks that have high trading volume
- Auto-refresh helps track changes during market hours
- Model retrains on each stock's historical data

## ⚠️ Important

This tool is for **educational purposes only**. Always do your own research and consult financial advisors before making investment decisions.

## 🆘 Troubleshooting

### "No data returned from API"
- Check your API key is correct
- Verify the stock symbol is valid
- Free API may have usage limits

### "Not enough data for indicators"
- Some stocks may not have enough historical data
- Try popular stocks like AAPL, MSFT, TSLA

### Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Use Python 3.7 or higher

## 📚 Learn More

- Read the full [README.md](README.md)
- Check out [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Review the code in `stock_predictor/` directory

---

Happy trading! 📈
