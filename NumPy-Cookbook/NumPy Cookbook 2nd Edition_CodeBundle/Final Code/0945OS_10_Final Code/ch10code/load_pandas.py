from __future__ import print_function
import statsmodels.api

# See https://github.com/statsmodels/statsmodels/tree/master/statsmodels/datasets
data = statsmodels.api.datasets.copper.load_pandas()

x, y = data.exog, data.endog

fit = statsmodels.api.OLS(y, x).fit()
print("Fit params", fit.params)
print()
print("Summary")
print()
print(fit.summary())
