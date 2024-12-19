from datetime import datetime
from typing import List

import pandas
import requests
import yfinance as yf

from logger import LOGGER
from src import file_utils


def get_snp500_companies() -> List[str]:
    try:
        url = "https://stockanalysis.com/list/sp-500-stocks"
        response = requests.get(url)
        response.raise_for_status()
        df = pandas.read_html(response.content)[0].Symbol
        LOGGER.info(f"Found {len(df)} company symbols")
        df.to_csv(file_utils.get_data_folder() / "snp500.csv", index=False)
        return df.to_list()
    except Exception as e:
        LOGGER.warning("Failed to fetch S&P500 companies...", e)

    return []


def get_stock_daily_price(symbol: str, start_datetime: datetime, end_datetime: datetime) -> pandas.DataFrame:
    try:
        start_date = start_datetime.date()
        end_date = end_datetime.date()
        LOGGER.info(f"Collecting {symbol} between {start_date.isoformat()} and {end_date.isoformat()}")
        df = yf.download(tickers=[symbol], start=start_date, end=end_date, interval="1d")

        if df.empty:
            LOGGER.warning(
                f"No data found for {symbol} between {start_date.isoformat()} and {end_date.isoformat()}")
            return pandas.DataFrame()

        df.reset_index(inplace=True)

        if isinstance(df.columns, pandas.MultiIndex):
            df.columns = df.columns.droplevel(1)

        df.rename(lambda c: c.lower(), axis="columns", inplace=True)

        if "date" in df.columns:
            df["date"] = df["date"].dt.date

        df["symbol"] = symbol

        df["close"] = df["close"].astype(float)
        df["open"] = df["open"].astype(float)
        df["high"] = df["high"].astype(float)
        df["low"] = df["low"].astype(float)
        df["volume"] = df["volume"].astype(int)

        df.to_parquet(file_utils.get_symbols_folder() / f"{symbol}.parquet", index=False)
        return df
    except Exception as e:
        LOGGER.error(f"Error collecting data for {symbol}: {e}")

    return pandas.DataFrame()
