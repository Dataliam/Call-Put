# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:18:46 2024

@author: liamb
"""
import numpy as np
# main.py
from data_fetcher.stock_data import fetch_stock_data, calculate_volatility
from options_calculator.black_scholes import black_scholes_call, black_scholes_put

def main():
    # Récupération des inputs de l'utilisateur
    ticker = input("Enter the stock ticker: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    interval = input("Enter the data interval (1d, 1wk, etc.): ")
    
    # Récupération des données d'action
    stock_data = fetch_stock_data(ticker, start_date, end_date, interval)
    print(stock_data.head())  # Affiche les premières lignes des données récupérées

    # Calcul de la volatilité à partir des données récupérées
    sigma = calculate_volatility(stock_data)
    print(f"Calculated Volatility: {sigma}")

    # Continuation de la récupération des inputs de l'utilisateur pour le calcul des options
    S = float(input("Enter the current stock price: "))
    K = float(input("Enter the strike price: "))
    T = float(input("Enter the time to maturity (in years): "))
    r = float(input("Enter the risk-free interest rate (as a decimal): "))
    
    # Calcul et affichage des prix des options Call et Put
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)

    print(f"Call Option Price: {call_price}")
    print(f"Put Option Price: {put_price}")

if __name__ == "__main__":
    main()
