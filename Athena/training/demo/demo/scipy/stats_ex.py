# Examples of how to use statistics distribution objects

from scipy import stats
from numpy import r_
import pylab as plt

x = r_[-5:5:100j]

# sample the distribution for random variables.
rvs = stats.norm.rvs(size=100) 
print rvs.shape
plt.subplot(2,2,1)
plt.plot(rvs)
plt.title("Normal Random Variables")

pdf = stats.norm.pdf(x)
plt.subplot(2,2,2)
plt.plot(x, pdf)
plt.title("Probability Density Function")

cdf = stats.norm.cdf(x)
plt.subplot(2,2,3)
plt.plot(x, cdf)
plt.title("Cumulative Distribution Function")

ppf = stats.norm.ppf(x)
plt.subplot(2,2,4)
plt.plot(x, ppf)
plt.title("Percent Point Function")

plt.show()



