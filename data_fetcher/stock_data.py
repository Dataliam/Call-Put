# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:25:34 2024

@author: liamb
"""

# stock_data.py
import yfinance as yf
import numpy as np

def fetch_stock_data(ticker, start_date, end_date, interval='1d'):
    """
    Fetch historical stock data using yfinance.

    :param ticker: The stock ticker symbol.
    :param start_date: Start date in 'YYYY-MM-DD' format.
    :param end_date: End date in 'YYYY-MM-DD' format.
    :param interval: Data interval ('1d' for daily, '1wk' for weekly, etc.).
    :return: A pandas DataFrame containing the stock data.
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(start=start_date, end=end_date, interval=interval)
    return hist
def calculate_volatility(stock_data):
    """
    Calculate the annualized volatility of a stock based on historical prices.

    :param stock_data: DataFrame containing the stock's historical prices.
    :return: Annualized volatility as a decimal.
    """
    # Calcul des rendements logarithmiques
    log_returns = np.log(stock_data['Close'] / stock_data['Close'].shift(1))
    
    # Calcul de la volatilité annuelle (écart-type des rendements logarithmiques)
    volatility = log_returns.std() * np.sqrt(252)  # 252 jours de trading par an
    return volatility