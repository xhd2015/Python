#import numpy as np
from scipy import stats
from pylab import step, plot, grid, show, axis, xlim, ylim

# Make some data to demo.
x = stats.gamma.rvs(4.0, 0.5, size=500)
x.sort()
ecdf = stats.rankdata(x) / len(x)

# Make the Q-Q plot against a normal dist.
ncdf = stats.norm.cdf(x, loc=x.mean(), scale=x.std())
step(ncdf, ecdf)

# Plot y = x
plot([0,1], [0,1], 'k:')
grid(True)
#axis('equal')
xlim(0,1)
ylim(0,1)
show()
