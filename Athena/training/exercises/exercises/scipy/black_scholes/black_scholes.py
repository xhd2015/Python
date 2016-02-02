"""
Black-Scholes Pricing
---------------------

Background
~~~~~~~~~~
The Black-Scholes option pricing models for European-style options on
a non-dividend paying stock are::

    c = S0 * N(d1) - K * exp(-r*T)* N(d2)  for a call option and

    p = K*exp(-r*T)*N(-d2) - S0 * N(-d1)   for a put option

where::
     
    d1 = (log(S0/K) + (r + sigma**2 / 2)*T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

Also:

* :func:`log` is the natural logarithm.
* ``N(x)`` is the cumulative density function of a standardized normal distribution.
* *S0* is the current price of the stock.
* *K* is the strike price of the option.
* *T* is the time to maturity of the option.
* *r* is the (continuously-compounded) risk-free rate of return.
* *sigma* is the stock price volatility.

Problem
~~~~~~~

Create a function that returns the call and put options prices
for using the Black-Scholes formula and the inputs of
*S0*, *K*, *T*, *r*, and *sigma*.

Hint:  You will need scipy.special.ndtr or scipy.stats.norm.cdf.
Notice that N(x) + N(-x) = 1.
 

See: :ref:`black-scholes-prices-solution`.
"""
# Ensure integer values for prices, etc. will work correctly.
from __future__ import division

from numpy import log, exp, sqrt

from scipy.stats import norm
from scipy.optimize import fsolve

def bsprices(S0, K, T, r, sigma):
    """Black-Scholes call and put option pricing

    Parameters
    ----------
    S0 :
        Current price of the underlying stock
    K :
        Strike price of the option
    T :
        Time to maturity of the option
    r :
        Risk-free rate of return (continuously-compounded)
    sigma :
        Stock price volatility

    Returns
    -------
    c :
        Call option price
    p :
        Put option price

    Notes
    -----
    r, T, and sigma must be expressed in consistent units of time
    """
    pass

    

    
    
