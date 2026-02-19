#!/usr/bin/env python3
"""
Setup script for Stock Analysis Using Finnhub API
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "stock_predictor" / "requirements.txt"
requirements = []
if requirements_file.exists():
    with open(requirements_file, "r", encoding="utf-8") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="stock-analysis-finnhub",
    version="1.0.0",
    author="Natsu",
    author_email="",
    description="AI-powered stock price prediction dashboard using Finnhub API and XGBoost",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/natsu-root/stock_analysis_using_finnhubAPI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="stock analysis prediction machine-learning finnhub xgboost streamlit",
    project_urls={
        "Bug Reports": "https://github.com/natsu-root/stock_analysis_using_finnhubAPI/issues",
        "Source": "https://github.com/natsu-root/stock_analysis_using_finnhubAPI",
    },
)
