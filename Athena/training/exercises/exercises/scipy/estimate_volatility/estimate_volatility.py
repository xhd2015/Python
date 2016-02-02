"""
Estimate Volatility
-------------------

Background
~~~~~~~~~~

A standard model of stock price fluctuation is::

   dS/S = mu dt + sigma * epsilon * sqrt(dt)
 
where:
    
* *S* is the stock price.
* *dS* is the change in stock price.
* *mu* is the rate of return.
* *dt* is the time interval.
* *epsilon* is a normal random variable with mean 0 and variance 1 that is
  uncorrelated with other time intervals.
* *sigma* is the volatility.

It is desired to make estimates of *sigma* from historical price information.
There are simple approaches to do this that assume volatility is constant over a
period of time. It is more accurate, however, to recognize that *sigma* changes
with each day and therefore should be estimated at each day. To effectively do
this from historical price data alone, some kind of model is needed.

The GARCH(1,1) model for volatility at time *n*, estimated from data
available at the end of time *n-1* is::

   sigma_n**2 = gamma V_L + alpha u_{n-1}**2 + beta sigma_{n-1}**2

where:

* *V_L* is long-running volatility
* ``alpha+beta+gamma = 1``
* ``u_n = log(S_n / S_{n-1})`` or ``(S_n - S_{n-1})/S_{n-1}``

Estimating *V_L* can be done as the mean of ``u_n**2`` (variance of *u_n*).
Estimating parameters *alpha* and *beta* is done by finding the parameters that
maximize the likelihood that the data *u_n* would be observed. If it is assumed
that the *u_n* are normally distributed with mean 0 and variance *sigma_n*, this
is equivalent to finding *alpha* and *beta* that minimize::

   L(alpha, beta) = sum_{n}(log(sigma_n**2) + u_n**2 / sigma_n**2)

where ``sigma_n**2`` is computed as above. 
   
Problem
~~~~~~~

1) Create a function to read in daily data from :file:`sp500hst.txt` for the
   S&P 500 for a particular stock. The file format is::
       
       date, symbol, open, high, low, close, volume
 
2) Create a function to estimate volatility per annum for a specific
   number of periods (assume 252 trading days in a year).

3) Create a function to compute ``sigma**2_n` for each *n* from *alpha* and 
   *beta* and ``u_n**2`` (you may need to use a for loop for this).  Use *V_L*
   to start the recursion.

4) Create a function that will estimate volatility using GARCH(1,1)
   approach by minimizing ``L(alpha, beta)``.

5) Use the functions to construct a plot of volatility per annum for a
   stock of your choice (use 'AAPL' if you don't have a preference)
   using quarterly, monthly, and GARCH(1,1) estimates.

You may find the repeat method useful to extend quarterly and monthly
estimates to be the same size as GARCH(1,1) estimates.

See :ref:`estimate-volatility-solution`.
"""
import numpy as np
from scipy.optimize import fmin
TRADING_DAYS = 252

