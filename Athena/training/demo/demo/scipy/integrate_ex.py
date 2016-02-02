from scipy import integrate 
from numpy import pi, vectorize, r_, sin, cos
from matplotlib import pylab as plt

def func(x):
    # Return the integral of cos from 0->x
    return integrate.quad(cos,0,x)[0]

vecfunc = vectorize(func)

x = r_[0:2*pi:100j]
x2 = x[::5]
y = sin(x)
y2 = vecfunc(x2)
plt.plot(x,y,x2,y2,'rx')
plt.show()

