"""
1. Define a function with four arguments, x, a, b, and c, that computes::
   
       y = a*exp(-b*x) + c

   (This is done for you in the code below.)
    
   Then create an array x of 75 evenly spaced values in the interval
   0 <= x <= 5, and an array y = f(x,a,b,c) with a=2.0, b = 0.76, c=0.1.

2. Now use scipy.stats.norm to create a noisy signal by adding Gaussian
   noise with mean 0.0 and standard deviation 0.2 to y.

3. Calculate 1st, 2nd and 3rd degree polynomial functions to fit to the data.
   Use the polyfit and poly1d functions from scipy.

4. Do a least squares fit to the orignal exponential function using 
   scipy.curve_fit.

"""

from matplotlib.pyplot import plot, title, show, hold, legend, subplot
from numpy import exp, linspace
from scipy import polyfit, poly1d
from scipy.stats import norm
from scipy.optimize import curve_fit

# 1. Define the function and create the signal.

def function(x, a, b, c):
    y = a*exp(-b*x) + c
    return y

a = 2.0
b = 0.76
c = 0.1
x = linspace(0, 5.0, 75)
y = function(x, a, b, c)

# 2. Now add some noise.

noisy_y = y + norm.rvs(loc=0, scale=0.2, size=y.shape)

subplot(1, 3, 1)
plot(x, noisy_y, '.', label="Noisy")
plot(x, y, label="Original", linewidth=2)
title("$%3.2fe^{-%3.2fx}+%3.2f$" % (a,b,c))
legend()

# 3. polynomial fit for 1st, 2nd, and 3rd degree.

subplot(1, 3, 2)
plot(x, noisy_y, '.')
hold('on')
for deg in [1,2,3]:
    # Compute the coefficients of the polynomial function of degree deg.
    coef = polyfit(x, noisy_y, deg)
    # Create a python function `poly` that computes values of the polynomial.
    poly = poly1d(coef)
    # Evalate the polynomial at x and plot it.
    poly_y = poly(x)
    plot(x, poly_y, linewidth=2, label="order=%d" % deg)
title("Polynomial Fit")
legend()

# 4. Use scipy.curve_fit to fit the actual function.

best, pcov = curve_fit(function, x, noisy_y)

fit_y = function(x, *best)

subplot(1, 3, 3)
plot(x, noisy_y, 'b.', label="Noisy")
plot(x, y, label="Original", linewidth=2)
label = r"$%3.2fe^{-%3.2fx}+%3.2f$" % tuple(best)
plot(x, fit_y, label=label, linewidth=2) 
title("Exponential Fit")
legend()
show()
