"""
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

"""

import numpy as np
from scipy.optimize import fmin
TRADING_DAYS = 252


fmt = [('date', int), ('symbol', 'S4'), ('open', float),
       ('high', float), ('low', float), ('close', float),
       ('volume', int)]


def read_data(filename):
    """Read all historical price data in filename into a structured
    numpy array with fields:

    date, symbol, open, high, low, close, volume
    """
    # converter functions    
    types = [int, str, float, float, float, float, int]
    datafile = open(filename)
    newdata = []
    for line in datafile:
        converted = [types[i](x) for i,x in enumerate(line.split(','))]
        newdata.append(tuple(converted))
    return np.array(newdata, dtype=fmt)

def read_symbol(filename, symbol):
    """Read all historical price data for a particular symbol in filename
    into a structured numpy array with fields:

    date, symbol, open, high, low, close, volume
    """
    # converter functions
    types = [int, str, float, float, float, float, int]
    datafile = open(filename)
    newdata = []
    for line in datafile:
        if symbol not in line:
            continue
        converted = [types[i](x) for i,x in enumerate(line.split(','))]
        newdata.append(tuple(converted))
    return np.array(newdata, dtype=fmt)

def volatility(S, periods=4, repeat=False):
    """Estimate of volatility using the entire data set
    divided into periods.  If repeat is True, then copy the
    estimate so that len(sigma) == len(S)-1
    """
    N = len(S)
    div = N//periods
    S = S[:periods*div]
    # place each quarter on its own row
    S = S.reshape(periods,-1)
    # Compute u
    u = np.log(S[:,1:]/S[:,:-1])
    # Estimate volatility per annum
    #   by adjusting daily volatility calculation
    sigma = np.sqrt(u.var(axis=-1)*TRADING_DAYS)
    if repeat:
        sigma = sigma.repeat(S.shape[-1])
    return sigma[1:]

def sigmasq_g(usq, alpha, beta):
    """sigma_n**2 assuming the GARCH(1,1) model of::

        sigma_n**2 = gamma*VL + alpha*sigma_n**2 + beta*u_n**2

    where gamma + alpha + beta = 1
    and  VL = mean(usq)
    """
    sigmasq = np.empty_like(usq)
    VL = usq.mean()
    sigmasq[0] = VL
    omega = VL*(1-alpha-beta)
    for i in range(1, len(usq)):
        sigmasq[i] = omega + alpha*sigmasq[i-1] + beta * usq[i-1]
    return sigmasq

# Function to minimize to find parameters of GARCH model.
def _minfunc(x, usq):
    alpha, beta = x
    sigsq = sigmasq_g(usq, alpha, beta)
    return (np.log(sigsq) + usq / sigsq).sum()

def garch_volatility(S):
    """Volatility per annum for each day computed from historical
    close price information using the GARCH(1,1) and maximum
    likelihood estimation of the parameters.
    """
    x0 = [0.5, 0.5]
    usq = np.log(S[1:]/S[:-1])**2
    xopt = fmin(_minfunc, x0, args=(usq,))
    sigmasq = sigmasq_g(usq, *xopt)
    print "alpha = ", xopt[0]
    print "beta = ", xopt[1]
    print "V_L = ", usq.mean()
    return np.sqrt(sigmasq*TRADING_DAYS)


if __name__ == "__main__":
    from matplotlib.pyplot import plot, title, xlabel, ylabel, legend, show
    
    stock = 'MSFT'
    data = read_symbol('sp500hst.txt', stock)
    S = data['close']
    sig_4 = volatility(S, 4, repeat=True)
    sig_12 = volatility(S, 12, repeat=True)
    sig_g = garch_volatility(S)
    plot(sig_g,label='GARCH(1,1)')
    plot(sig_12,label='Monthly average')
    plot(sig_4, label='Quarterly average')
    title('Volatility estimates')
    xlabel('trading day')
    ylabel('volatility per annum')
    legend(loc='best')
    show()
