"""
Demonstrate OLS regression using statsmodels.

This script is based on version 0.5.0 of statsmodels.
"""

import numpy as np
import statsmodels.api as sm
from matplotlib.pyplot import plot, scatter, legend, xlabel, ylabel, show


# Make some noisy sample data.
n = 41
x = np.linspace(0, 10, n)
y = 2.5 + 0.5 * x + 0.45 * np.random.randn(n)

# Create the design matrix for a linear fit.
# add_constant(x) appends a column of 1s (for the intercept).
X = sm.add_constant(x, prepend=True)

# Fit the data, using Ordinary Least Squares regression.
results = sm.OLS(y, X).fit()
print results.summary()

# Plot the observations and the fitted curve.
scatter(x, y, label='Data')
Y = np.dot(X, results.params)
plot(x, Y, 'g-', linewidth=3, label='Linear fit')
legend(loc='best')
xlabel('x')
ylabel('y')
show()
