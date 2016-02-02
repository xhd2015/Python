""" Demo using latex for fancy formatting of the titles, and labels in 
Matplotlib. 

Source: http://matplotlib.org/users/usetex.html
"""
from numpy import arange, cos, pi
from matplotlib.pyplot import plot, xlabel, ylabel, title, show
from matplotlib import rc

rc('text', usetex=True)
t = arange(0.0, 1.0 + 0.01, 0.01)
s = cos(2 * 2 * pi * t) + 2
plot(t, s)
xlabel(r'\textbf{time (s)}')
ylabel(r'\textit{voltage (mV)}', fontsize=16)
title(r"\TeX\ is Number $\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!", fontsize=16, color='r')
show()
