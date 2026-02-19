# Contributing to Stock Analysis Using Finnhub API

First off, thank you for considering contributing to this project! It's people like you that make this tool better for everyone.

## Code of Conduct

By participating in this project, you are expected to uphold a respectful and constructive environment for all contributors.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, screenshots, etc.)
- **Describe the behavior you observed and what you expected**
- **Include your environment details** (Python version, OS, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any examples of where this enhancement exists elsewhere**

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** with clear, concise commits
3. **Follow the existing code style**
4. **Test your changes** thoroughly
5. **Update documentation** if needed
6. **Submit a pull request** with a clear description

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/stock_analysis_using_finnhubAPI.git
   cd stock_analysis_using_finnhubAPI
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   cd stock_predictor
   pip install -r requirements.txt
   ```

4. Set up your API key:
   ```bash
   cp .env.example .env
   # Edit .env and add your Finnhub API key
   ```

## Coding Standards

- **Python Style**: Follow PEP 8 guidelines
- **Docstrings**: Use clear docstrings for functions and classes
- **Comments**: Comment complex logic, but prefer self-documenting code
- **Variable Names**: Use descriptive variable names
- **Type Hints**: Use type hints where appropriate

## Testing

Before submitting a pull request:

1. Test your changes manually:
   ```bash
   streamlit run dashboard.py
   ```

2. Verify the predictor works:
   ```bash
   python predictor.py
   ```

3. Check for any Python errors or warnings

## Project Structure

- `dashboard.py` - Main Streamlit web interface
- `predictor.py` - Core prediction pipeline
- `data_fetcher.py` - API integration and data fetching
- `feature_engineering.py` - Technical indicator calculations
- `model.py` - Machine learning model training and prediction

## Areas for Contribution

We welcome contributions in these areas:

- **Additional Technical Indicators**: Add more indicators (MACD, Bollinger Bands, etc.)
- **Model Improvements**: Better ML models, hyperparameter tuning
- **UI Enhancements**: Improve the dashboard design and user experience
- **Testing**: Add unit tests and integration tests
- **Documentation**: Improve documentation and examples
- **Performance**: Optimize data fetching and processing
- **Error Handling**: Better error messages and edge case handling
- **Features**: Add new features like alerts, watchlists, backtesting, etc.

## Commit Messages

Write clear commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add Bollinger Bands indicator

- Implement Bollinger Bands calculation in feature_engineering.py
- Add visualization in dashboard
- Update documentation

Fixes #123
```

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉
