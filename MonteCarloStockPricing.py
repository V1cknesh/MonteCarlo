import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def geometric_brownian_motion(Current_stock_price, r, sigma, t, steps):
    dt = t/steps
    W = np.random.standard_normal(steps+1)
    W = np.cumsum(W)*np.sqrt(dt)
    X = np.zeros(steps+1)
    X[0] = Current_stock_price
    for i in range(steps):
        X[i+1] = X[i]*np.exp((r-0.5*sigma**2)*dt+sigma*W[i+1])
    return np.exp(X)

def black_scholes_call(Current_stock_price, Strike_price, t, risk_free_rate, annual_divident_rate, sigma, steps):
    X = np.zeros(steps + 1)
    X[0] = Current_stock_price
    for i in range(steps):
        X[i+1] = X[i]*norm.cdf((np.log(Current_stock_price/Strike_price)+(risk_free_rate-annual_divident_rate+0.5*sigma**2)*t)/(sigma*np.sqrt(t)))-Strike_price*np.exp(-risk_free_rate*t)*norm.cdf((np.log(Current_stock_price/Strike_price)+(risk_free_rate-annual_divident_rate+0.5*sigma**2)*t)/(sigma*np.sqrt(t))-sigma*np.sqrt(t))
    return np.exp(X)

def black_scholes_put(Current_stock_price, Strike_price, t, risk_free_rate, annual_divident_rate, sigma,steps):
    X = np.zeros(steps + 1)
    X[0] = Strike_price
    for i in range(steps):
        X[i+1] = X[i]*np.exp(-risk_free_rate*t)*norm.cdf(-(np.log(Current_stock_price/Strike_price)+(risk_free_rate-annual_divident_rate+0.5*sigma**2)*t)/(sigma*np.sqrt(t))-sigma*np.sqrt(t))-Current_stock_price*norm.cdf(-(np.log(Current_stock_price/Strike_price)+(risk_free_rate-annual_divident_rate+0.5*sigma**2)*t)/(sigma*np.sqrt(t)))
    return np.exp(X)

if __name__ == "__main__":
    Current_stock_price = 100
    Strike_price = 110
    risk_free_rate = 0.05
    volatility = 0.2
    t = 1  # time to maturity
    steps = 10
    sigma = volatility / np.sqrt(t)  # standard deviation
    annual_divident_rate = 0.02
    paths = geometric_brownian_motion(Current_stock_price, risk_free_rate, sigma, t, steps)

    black_scholes_call_price = black_scholes_call(Current_stock_price, Strike_price, t, risk_free_rate, annual_divident_rate, sigma, steps)
    black_scholes_put_price = black_scholes_put(Current_stock_price, Strike_price, t, risk_free_rate, annual_divident_rate,sigma, steps)
    geometric_brownian_motion_price = geometric_brownian_motion(Current_stock_price, risk_free_rate, sigma, t, steps)

    print(black_scholes_call_price)
    print(black_scholes_put_price)
    print(geometric_brownian_motion_price)
