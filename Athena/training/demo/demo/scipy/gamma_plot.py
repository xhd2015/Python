
import numpy as np
from scipy.stats import gamma
from pylab import subplot, plot, title, suptitle, xticks, grid, show

x = np.linspace(0, 5, 250)

# Shape parameter k
k = 4
# Scale parameter theta
theta = 0.5

# "Frozen" distribution
gm = gamma(k, scale=theta)

pdf = gm.pdf(x)
cdf = gm.cdf(x)
sf = gm.sf(x)

subplot(3,1,1)
plot(x, pdf)
title("Probability Density Function (pdf)")
grid(True)
t, lbls = xticks()
xticks(t, [])

subplot(3,1,2)
plot(x, cdf)
title("Cumulative Distribution Function (cdf)")
grid(True)
t, lbls = xticks()
xticks(t, [])

subplot(3,1,3)
plot(x, sf)
title("Survival Function (sf)")
grid(True)
#t, lbls = xticks()
#xticks(t, [])

suptitle(r"Gamma distribution, k = %g, $\theta$ = %g" % (k, theta),
            fontsize=14)

show()