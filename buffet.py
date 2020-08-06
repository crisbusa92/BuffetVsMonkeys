import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import numpy as np
import math


def sp500_returns(symbols,period = '5y'):
    tickers_profit = []
    for x in symbols:
        ticker = yf.Ticker(x)
        hist = ticker.history(period=period).dropna()
        profit = (hist.loc[hist.index[len(hist)-1],
                    'Close']/hist.loc[hist.index[0], 'Close'])-1

        tickers_profit.append(profit)
    sp5y = pd.DataFrame()
    sp5y['Ticker'] = list(symbols)
    sp5y['5yr Return'] = tickers_profit
    

    return sp5y

"""
generate random portfolios with nmonkeys number 
of portfolios and nstocks number of stocks
"""

def dart_monkeys(symbols,nmonkeys = 10,nstocks = 30):
    #set random weights for each stock in monkey portfolio
    weights = []
    for i in range(nmonkeys):
        randomlist = rd.sample(range(1, 99), nstocks)
        dby = sum(randomlist)
        rws = []
        for x in randomlist:
            rw = x/dby
            rws.append(rw)
        weights.append(rws)
    #Select random stocks for each stock in monkey portfolio
    stocks = []
    for stock in range(nmonkeys):
        randomS = rd.sample(symbols, nstocks)
        stocks.append(randomS)
    out = []
    #Generate DICT list with random stocks and weights
    for i in range (nmonkeys):
        d = dict(zip(stocks[i],weights[i]))
        out.append(d)
    
    return out

def monkey_returns(DF,diclist):
    returns = []
    for x in diclist:
        #Obtaining Weights
        suma = 0
        for y in x.keys():
            #Sum 
            suma += float(DF[DF['Ticker'] == y]['5yr Return']) * x[y]
        returns.append(suma)

    return returns