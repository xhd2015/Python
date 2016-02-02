"""
Monte Carlo Options
-------------------

Background
~~~~~~~~~~

One approach to pricing options is to simulate the instrument price over the
lifetime of the option using Monte Carlo simulation (assuming some model). The
resulting random walk of the stock price can be used to determine the option
pay-off.

The option price is then usually calculated as the average value of the
simulated pay-offs discounted at the risk-free rate of return (exp(-r*T)).

An often-used model for the stock price at time *T* is that it is log-normally
distributed where log(ST) is normally distributed with::

     mean - log(S0) + (mu-sigma**2 / 2) * T 
     
and::
    
     variance - sigma**2 * T

This implies that the *ST* is log-normally distributed with shape parameter
``sigma * sqrt(T)`` and scale parameter ``S0*exp((mu-sigma**2/2)*T)``. 
     
For option pricing, *mu* is the risk-free rate of return and *sigma* is
the volatility.

The value of a call option at maturity is ST-K if ST>K and 0 if ST<K.

The value of a put option at maturity is K-ST if K>ST and 0 if ST>K.

Problem
~~~~~~~

1) Create a function that uses a Monte Carlo method to price vanilla
   call and put options, by drawing samples from a log-normal distribution.

2) Create a function that uses a Monte-Carlo method to price vanilla
   call and put options, by drawing samples from a normal distribution.

3) Bonus, compare 1 and 2 against the Black-Scholes method of pricing.

See :ref:`montecarlo-options-solution`.
"""
from numpy import exp, sqrt, maximum
from scipy.stats import lognorm, norm


def mcprices(S0, K, T, r, sigma, N=5000):
    """
    Call and put option prices using log-normal Monte-Carlo method

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
    N :
        Number of stock prices to simulate

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

