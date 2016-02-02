"""Chi-square test of a contingency table (test of independence)."""

import numpy as np
# Requires scipy 0.10.0 or newer for chi2_contingency.
from scipy.stats import chi2_contingency


# Table of observed frequencies.
observed = np.array([
    [75, 25],
    [65, 35]
    ])

#observed = np.array([
#    [12, 5],
#    [10, 8]
#    ])

#observed = np.array([
#    [81, 144, 180],
#    [72, 108, 144]
#    ])

chi2, p, dof, expected = chi2_contingency(observed)

p_sig = 0.05

print
print "observed:"
print observed
print
print "expected, if independent:"
print expected
print
print "chi^2 = %g" % chi2
print "p = %10.8f" % p
print "dof =", dof
print
print "The null hypothesis is that the groups are independent." 
if p < p_sig:
    print "Using a level of significance of %4.2f, the null hypothesis is rejected." % p_sig
else:
    print "Using a level of significance of %4.2f, the null hypothesis can not be rejected." % p_sig
print
