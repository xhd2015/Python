"""
Statistics Functions
--------------------

1. Import stats from scipy, and look at its docstring to see
   what is available in the stats module::

       In [1]: from scipy import stats
       In [2]: stats?

2. Look at the docstring for the normal distribution::

       In [3]: stats.norm?

   You'll notice it has these parameters:

      loc: 
        This variable shifts the distribution left or right.
        For a normal distribution, this is the mean.  It defaults to 0. 
      scale:
        For a normal distribution, this is the standard deviation.

3. Create a single plot of the pdf of a normal distribution with mean=0
   and standard deviation ranging from 1 to 3.  Plot this on the range
   from -10 to 10.

4. Create a "frozen" normal distribution object with mean=20.0,
   and standard deviation=3::

       my_distribution = stats.norm(20.0, 3.0)

5. Plot this distribution's pdf and cdf side by side in two
   separate plots.

6. Get 5000 random variable samples from the distribution, and use
   the stats.norm.fit method to estimate its parameters.
   Plot the histogram of the random variables as well as the
   pdf for the estimated distribution. (Try using stats.histogram.
   There is also pylab.hist which makes life easier.)

See: :ref:`stats-functions-solution`.   
"""
from numpy import linspace, arange
from scipy.stats import norm, histogram

from matplotlib.pyplot import plot, clf, show, figure, legend, title, subplot, \
                              bar, hist
