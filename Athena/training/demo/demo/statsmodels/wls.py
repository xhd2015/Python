"""
This script implements the calculations in Section 9.4 of Applied Regression
Analysis (3rd ed.) by Draper and Smith.

The example illustrates the use of Weighted Least Squares.
"""

import numpy as np
from statsmodels.api import add_constant, OLS, WLS
import matplotlib.pyplot as plt


# (x, y) is the set of observations.  w contains precomputed weights; we'll
# also compute these weights in this script.
x, y, w = np.loadtxt('draper_smith_table9p1.txt', unpack=True)

X = add_constant(x, prepend=True)

# --- OLS ---------------------------------------------------------------
# Ordinary least squares fit.
ols_result = OLS(y, X).fit()

print ols_result.summary()

# Make a plot of the OLS residuals vs y and vs x.
# The following recreates Fig. 9.1.
plt.figure(1)
plt.clf()
plt.subplot(2, 1, 1)
plt.plot(ols_result.fittedvalues, ols_result.resid, 'bo')
plt.title("OLS Residuals versus fitted values")
plt.xlabel('y')
plt.ylabel('e')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(x, ols_result.resid, 'bo')
plt.title("OLS Residuals versus x")
plt.xlabel("x")
plt.ylabel("e")
plt.grid()
plt.tight_layout()

# --- WLS ---------------------------------------------------------------
#
# To estimate the dependence of the variance on x, we follow Draper and Smith
# by computing the variance on the sets of repeats or near repeats.  In the
# data we see clusters around x=3, 5.4, 7.8, 9.1 and 10.2.  Let's do a little
# numpy magic to compute the mean x and the pure error mean square for these
# clusters.  Our goal is to reproduce the following numbers, from p. 228 of
# Draper and Smith:
#  \bar{X}_j    3.0      5.4      7.8     9.1     10.2
#  s^2_{e_j}    0.0072   0.3440   1.7404  0.8683  3.8964

# Our estimates of the locations of the clusters.
x_centers = np.array([3.0, 5.4, 7.8, 9.1, 10.2])
# x values within `threshold` of the value in x_centers will be considered
# part of the same group.
threshold = 0.333
selection = np.abs(x - x_centers.reshape(-1, 1)) <= threshold
cluster_stats = []
for mask in selection:
    xi = x[mask]
    yi = y[mask]
    xmean = xi.mean()
    ymean = yi.mean()
    yvar = yi.var(ddof=1)
    cluster_stats.append((xmean, yvar))
cluster_stats = np.array(cluster_stats)

# cluster_stats is now a 2D array.  The first column holds the mean of the
# x values in each cluster, and the second column holds the variance of the
# y values in the cluster.
# (Challenge: compute cluster_stats without using a for loop.)
# We'll now fit this data to a quadratic curve.  This will provide us with an
# estimator of the variance for any x.
# We're not going to investigate the "goodness" of this fit, so the simple
# function numpy.polyfit will do nicely here.
# Note: Draper and Smith use [3.0, 5.4, 7.8, 9.1, 10.2] for the
# x coordinates in the quadratic fit, but these are not the exact means of
# the x coordinates of the clusters.  To reproduce the coefficients of the
# quadratic fit shown in the text, uncomment the next line.
##cluster_stats[:,0] = x_centers

# Use polyfit to fit the data, and then pass the coefficients to
# poly1d, so we have a polynomial that can be evaluated easily.
coeffs = np.polyfit(cluster_stats[:, 0], cluster_stats[:, 1], deg=2)
print
print "Coefficients of the quadratic fit of the variance estimator:", coeffs
print

# Note: It appears that the coefficients of the quadratic function were
# truncated to four decimal place before evaluating the weights in the third
# column of Table 9.1.  To reproduce the data in table, use these values for
# the coefficients:
##coeffs = np.array([0.0883, -0.7334, 1.5329])

var_est = np.poly1d(coeffs)

# Plot the samples used to create the estimator of the variance, and the
# variance as a function of x.  This plot is not in Draper and Smith, but
# they say "A plot of these suggests a quadratic relationship...", so it is
# nice to see what they are talking about.
plt.figure(2)
plt.clf()
xx = np.linspace(x.min(), x.max(), 25)
plt.plot(xx, var_est(xx), 'b', label="Estimated variance (quadratic fit)")
plt.plot(cluster_stats[:, 0], cluster_stats[:, 1], 'ro',
                                        label="Cluster variances")
plt.xlabel('x')
plt.ylabel('$s^2$', fontsize=18)
plt.legend(loc='best', numpoints=1)

# The weights for weighted least squares are 1/(s^2).  If we use x_centers
# when doing the quadratic fit of var_est (see comment above), this array
# should match the third column of table 9.1 in Draper and Smith.
weights = 1.0 / var_est(x)

# Use the WLS class from statsmodels to do the weighted least squares fit:
wls_result = WLS(y, X, weights=weights).fit()
print wls_result.summary()

# The next set of plotting commands recreate Fig. 9.2.
plt.figure(3)
plt.clf()
plt.subplot(2, 1, 1)
plt.plot(np.sqrt(weights) * wls_result.fittedvalues, wls_result.wresid, 'bo')
plt.title("WLS Residuals versus weighted fitted values")
plt.xlabel('$\sqrt{w} y$', fontsize=18)
plt.ylabel('e')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(np.sqrt(weights) * x, wls_result.wresid, 'bo')
plt.title("WLS Residuals versus weighted x")
plt.xlabel("$\sqrt{w} x$", fontsize=18)
plt.ylabel("e")
plt.grid()
plt.tight_layout()
plt.show()
