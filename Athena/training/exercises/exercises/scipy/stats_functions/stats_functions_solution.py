"""
1. Import stats from scipy, and look at its docstring to see
   what is available in the stats module::

       In [1]: from scipy import stats
       In [2]: stats?

2. Look at the docstring for the normal distribution::

       In [3]: stats.norm?

   You'll notice it has these parameters:

      loc: 
        This variable shifts the distribution left or right.
        For a normal distribution, this is the mean.  It defaults to 0. 
      scale:
        For a normal distribution, this is the standard deviation.

3. Create a single plot of the pdf of a normal distribution with mean=0
   and standard deviation ranging from 1 to 3.  Plot this on the range
   from -10 to 10.

4. Create a "frozen" normal distribution object with mean=20.0,
   and standard deviation=3::

       my_distribution = stats.norm(20.0, 3.0)

5. Plot this distribution's pdf and cdf side by side in two
   separate plots.

6. Get 5000 random variable samples from the distribution, and use
   the stats.norm.fit method to estimate its parameters.
   Plot the histogram of the random variables as well as the
   pdf for the estimated distribution. (Try using stats.histogram.
   There is also pylab.hist which makes life easier.)

"""

from numpy import linspace, arange
from scipy.stats import norm, histogram

from matplotlib.pyplot import plot, clf, show, figure, legend, title, subplot, \
                  bar, hist

x = linspace(-10,10, 1001)

# 2. Create a single plot with the pdf of a normal distribution with
#    mean=0 and std ranging from 1 to 3.  Plot this on the range from
#    -10 to 10.

for std in linspace(1, 3, 5):
    plot(x, norm.pdf(x, scale=std), label="std=%s" % std)
legend()    
title("Standard Deviation")    

    
#    3. Create a "frozen" normal distribution object with mean=20.0,
#       and standard devation=3.
       
my_dist = norm(20.0, 3.0)
   
   
# 4. Plot this distribution's pdf and cdf side by side in two
#    separate plots.
x = linspace(0, 40, 1001)

figure()
subplot(1,2,1)
plot(x, my_dist.pdf(x))
title("PDF of norm(20, 3)")
    
subplot(1,2,2)
plot(x, my_dist.cdf(x))
title("CDF of norm(20, 3)")


# 5. Get 5000 random variable samples from the distribution, and use
#    the stats.norm.fit method to estimate its parameters.
#    Plot the histogram of the random variables as well as the
#    pdf for the estimated distribution.

random_values = my_dist.rvs(5000)

# Calculate the histogram using stats.histogram.
num_bins = 50
bin_counts, min_bin, bin_width, outside = histogram(random_values, 
                                                    numbins=num_bins)
bin_x = min_bin + bin_width * arange(num_bins)
# Normalize the bin counts so that they integrate to 1.0 like
# a pdf would.
hist_pdf = bin_counts/(len(random_values)*bin_width)
 
mean_est, std_est = norm.fit(random_values)
print "estimate of mean, std:", mean_est, std_est

# Plotting.
figure()
bar(bin_x, hist_pdf, width=bin_width)

# or for the lazy, use pylab.hist...
#hist(random_values, bins=50, normed=True)

plot(bin_x, norm(mean_est, std_est).pdf(bin_x), 'r', linewidth=2)
show()

