"""
data_fetcher.py
---------------
Fetches historical stock data using yfinance API.
"""

import yfinance as yf
import pandas as pd
from src.utils import log


class DataFetcher:
    """Handles fetching stock price data."""

    @staticmethod
    def fetch_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        log(f"Fetching data for {ticker} from {start_date} to {end_date}")
        stock = yf.download(ticker, start=start_date, end=end_date)
        if stock.empty:
            log("No data found. Check ticker symbol or date range.")
        else:
            log(f"Fetched {len(stock)} records for {ticker}.")
        return stock.reset_index()

