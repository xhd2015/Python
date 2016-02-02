"""
Black-Scholes Models
--------------------

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

1. Create a function that returns the call and put options prices
   for using the Black-Scholes formula and the inputs of
   *S0*, *K*, *T*, *r*, and *sigma*.

   Hint:  You will need scipy.special.ndtr or scipy.stats.norm.cdf.
   Notice that N(x) + N(-x) = 1.
 
2. The one parameter in the Black-Scholes formula that is not
   readily available is *sigma*.  Suppose you observe that the price
   of a call option is *cT*.  The value of *sigma* that would produce
   the observed value of *cT* is called the "implied volatility".
   Construct a function that calculates the implied volatility from
   *S0*, *K*, *T*, *r*, and *cT*.

  Hint:  Use a root-finding technique such as scipy.optimize.fsolve.
  (or scipy.optimize.brentq since this is a one-variable root-finding problem).

3. Repeat #2, but use the observed put option price to calculate
   implied volatility.

4) Bonus:  Make the implied volatility functions work for vector inputs (at
   least on the call and put prices)

See: :ref:`black-scholes-solution`.
"""

# Ensure integer values for prices, etc. will work correctly.
from __future__ import division

from numpy import log, exp, sqrt

from scipy.stats import norm

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
    
    x0 = sigma * sqrt(T)
    erT = exp(-r*T)
    d1 = (log(S0/K) + (r + sigma**2 / 2) * T) / x0
    d2 = d1 - x0
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    c = S0*Nd1 - K*erT*Nd2
    p = K*erT*(1-Nd2) - S0*(1-Nd1)
    return c, p


if __name__ == "__main__":
    S0 = 100   # $100 stock price
    K = 105    # $105 strike price
    T = 3/12   # 3 month period
    r = 0.004  # 3 month T-bill
    sigma = .3 # 30% per annum
    call, put = bsprices(S0, K, T, r, sigma)
    print "Call and Put Prices: %3.2f, %3.2f" % (call, put) 