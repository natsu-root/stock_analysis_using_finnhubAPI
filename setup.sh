#!/bin/bash

# Stock Analysis Setup Script
echo "🚀 Setting up Stock Analysis Application..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python $(python3 --version) detected"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Navigate to stock_predictor directory
cd stock_predictor

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit stock_predictor/.env and add your Finnhub API key"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Get your free API key from https://finnhub.io/"
echo "2. Edit stock_predictor/.env and add your API key"
echo "3. Run: cd stock_predictor && streamlit run dashboard.py"
echo ""
