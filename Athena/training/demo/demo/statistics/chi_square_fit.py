"""Elementary chi-square test (goodness of fit)."""

import numpy as np
from scipy.stats import chisquare

expected_distr = np.array([0.6, 0.2, 0.2])

# Observed counts:
observed = np.array([73, 10, 17])

# Expected counts:
expected = expected_distr * observed.sum()

chi2, p = chisquare(observed, expected)

p_sig = 0.05

print
print "expected distr: ", expected_distr
print
print "observed: ", observed, "(total = %d)" % observed.sum()
print "expected: ", expected
print
print "chi^2 = %g" % chi2
print "p = %6.4f" % p
print
print "The null hypothesis is that the population follows the expected distribution." 
if p < p_sig:
    print "Using a level of significance of %4.2f, the null hypothesis is rejected." % p_sig
else:
    print "Using a level of significance of %4.2f, the null hypothesis can not be rejected." % p_sig
print
