""" 
Gaussian Kernel Density Estimation
----------------------------------

Estimate a probability density function for a set of random
samples using a Gaussian Kernel Density estimator.

Create 100 normally distributed samples with mean=1.0
and std=0.0 using the stats.norm.rvs method.

Use stats.kde.gaussian_kde to estimate the pdf for the
distribution of these samples.  Compare that to the analytic
pdf for the distribution as well as the histogram of the
actual samples over the interval -3, 10.

Bonus:
    
Construct a set of samples (200 or so) from two different normal 
distributions, mean=0.0, std=0.5 and mean=5.0, std=1.0.
As with the first example, compare this against the analytic
pdf as well as the histogram of the actual samples over the
interval -3, 10.

See: :ref:`gaussian-kde-solution`.
"""

from numpy import linspace, concatenate
from scipy import stats
from matplotlib.pyplot import figure, plot, hold, legend, show, hist

# Create a normal distribution object and get 100
# samples from it.
N = 100
dist = stats.norm(0.0, 1.0)
samples = dist.rvs(size=N)

# Create gaussian_kde object with the given samples.          

# Evaluate the pdf using the gaussian_kde object as well
# as the analytic solution available on the stats.norm

# Display the results
