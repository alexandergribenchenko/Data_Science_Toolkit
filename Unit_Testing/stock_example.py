import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo
import math
import numpy as np
from datetime import datetime

def stock_data(tickers, start_date, end_date):
    """
    use yfinance to get stock "Adj Close" data
    """
    return yf.download(tickers, start=start_date, end=end_date)['Adj Close']

tickers = ['GOOGL', 'TSLA'] 
start_date = '2020-01-02'
end_date = '2020-01-03'

df = stock_data(tickers, start_date, end_date) 

d = {
    'Date': [datetime(2020,1,2)], 
    'GOOGL': [68.43399810791016], 
    'TSLA': [86.052002]
    }
df_truth = pd.DataFrame(data=d).set_index('Date')

print(df)
print(df_truth)

print(df.columns==df_truth.columns)
print(df==df_truth)
print('-------------------------')
print(df.TSLA[0])
print(df_truth.TSLA[0])

# print(df_truth)
# print(df_truth.columns)

# print(df==df_truth)




# def main():
#     tickers = ['AAPL','GOOGL', 'TSLA']  
#     start_date = '2019-01-02'
#     end_date = '2020-01-03'

#     df = get_data(tickers, start_date, end_date)  

#     stock_plot(df).savefig('plot.png')
#     print(optimize_sharpe_ratio(df))

# if __name__ == "__main__":
#     main()




def stock_plot(price):
    fig, ax = plt.subplots()
    tickers = price.columns.to_list()
    for ticker in tickers:
        ax.plot(price[[ticker]], label=ticker)
    ax.set_xlabel('Date')
    ax.set_ylabel('Adjusted closing price')
    ax.legend()
    return fig

# def calculate_daily_returns(allocation, price):
#     """
#     Calculate daily return
#     allocation: allocation of the stocks in your portfolio
#     price: adj close price for the stocks
#     """
#     start_val = 1 #how much money we have to start with
#     normed = price/price.iloc[0] #normalize prices
#     allocated = normed * allocation
#     position = allocated * start_val
#     portfolio = position.sum(axis=1)
#     daily_returns = (portfolio/portfolio.shift(1)) - 1
#     return daily_returns

# def neg_sharpe_ratio(allocation, price):
#     """
#     Calculate negative of the simplified sharpe ratio
#     allocation: allocation of the stocks in your portfolio
#     price: adj close price for the stocks
#     """
#     daily_returns = calculate_daily_returns(allocation, price)
#     sharpe_ratio = (daily_returns.mean()/daily_returns.std()) 
#     return -sharpe_ratio

# def optimize_sharpe_ratio(price):    
#     """
#     optimizes sharpe ratio for best allocations
#     """
#     tickers = price.columns.to_list()
#     allocation = np.ones(len(tickers))/len(tickers)
#     bounds = [(0.0, 1.0) for i in range(len(tickers))]
#     constraints = (
#         { 'type': 'ineq', 'fun': lambda inputs: 1.0 - np.sum(inputs) },
#         { 'type': 'ineq', 'fun': lambda inputs:  np.sum(inputs)-1 })
#     result = spo.minimize(
#         neg_sharpe_ratio, allocation, args=price, method='SLSQP',
#         options={'disp':True},bounds=bounds,constraints=constraints)
#     allocations = result.x
#     return allocations

