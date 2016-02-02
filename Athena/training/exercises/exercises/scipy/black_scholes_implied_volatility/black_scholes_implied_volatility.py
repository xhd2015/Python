"""
Black-Scholes Implied Volatility
--------------------------------

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

1. The one parameter in the Black-Scholes formula that is not
   readily available is *sigma*.  Suppose you observe that the price
   of a call option is *cT*.  The value of *sigma* that would produce
   the observed value of *cT* is called the "implied volatility".
   Construct a function that calculates the implied volatility from
   *S0*, *K*, *T*, *r*, and *cT*.

   Hint:  Use a root-finding technique such as scipy.optimize.fsolve.
   (or scipy.optimize.brentq since this is a one-variable root-finding problem).

2. Repeat #1, but use the observed put option price to calculate
   implied volatility.

3. Bonus:  Make the implied volatility functions work for vector inputs (at
   least on the call and put prices)
   
See: :ref:`black_scholes-implied-volatility-solution`
"""

# Ensure integer values for prices, etc. will work correctly.
from __future__ import division

from numpy import log, exp, sqrt, ones_like

from scipy.stats import norm
from scipy.optimize import fsolve


def imp_volatility_call(S0, K, T, r, cT):
    """Implied volatility from actual call price

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
    cT :
        Observed price of the call option at maturity

    Returns
    -------
    sigma :
        Implied volatility that gives a Black-Scholes call
          option price equal to the observed price

    Notes
    -----
    r and T must be expressed in consistent units of time    
    """
    pass

def imp_volatility_put(S0, K, T, r, pT):
    """Implied volatility from actual call price

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
    pT :
        Observed price of the put option at maturity

    Returns
    -------
    sigma :
        Implied volatility that gives a Black-Scholes call
          option price equal to the observed price

    Notes
    -----
    r and T must be expressed in consistent units of time          
    """
    pass


