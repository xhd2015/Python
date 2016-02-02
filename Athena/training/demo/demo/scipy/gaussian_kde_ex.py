from numpy import hstack, linspace
from scipy import stats
from scipy.stats.kde import gaussian_kde
from pylab import hist, plot, show, stem, figure

# Sample two normal distributions
# and create a bi-modal distribution
rv1 = stats.norm()
rv2 = stats.norm(2.0, 0.8)
samples = hstack([rv1.rvs(size=100), 
                    rv2.rvs(size=100)])

# Use a Gaussian kernel density to 
# estimate the PDF for the samples.
approximate_pdf = gaussian_kde(samples)
x = linspace(-3, 6, 200)

# Compare the histogram of the samples to
# the PDF approximation.
figure(1)
hist(samples, bins=25, normed=True)
plot(x, approximate_pdf(x), 'r')

# Example 2: A bunch of points at 0, one at 1.
samples2 = [0.0]*10 + [1.0]
pdf2 = gaussian_kde(samples2)
x2 = linspace(-1.0, 2, 500)

figure(2)
plot(x2, pdf2(x2), 'r')
stem([0,1], [1, 0.1])

show()
