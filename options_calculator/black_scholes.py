# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:26:15 2024

@author: liamb
"""

# black_scholes.py
from scipy.stats import norm
import numpy as np

def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes option price for a call option.

    :param S: Current stock price
    :param K: Strike price
    :param T: Time to maturity (in years)
    :param r: Risk-free interest rate (annual)
    :param sigma: Volatility of the stock price (annual)
    :return: Call option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = (S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))
    return call_price

def black_scholes_put(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes option price for a put option using put-call parity.

    :param S: Current stock price
    :param K: Strike price
    :param T: Time to maturity (in years)
    :param r: Risk-free interest rate (annual)
    :param sigma: Volatility of the stock price (annual)
    :return: Put option price
    """
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = call_price - S + K * np.exp(-r * T)
    return put_price
