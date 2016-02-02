
from scipy.integrate import odeint
from numpy import linspace
from pylab import (plot, xlabel, legend, title, show)

def vanderpolsys(w,t,mu):
    """van der Pol system vector field."""
    x,y = w
    f = [ y, -mu*(x**2-1)*y - x]
    return f

t = linspace(0,30.0,301)
mu = 0.5
init = [0.25,0.0]
sol = odeint(vanderpolsys,init,t,args=(mu,),
                    atol=1.0e-8,rtol=1.0e-10)
                    
plot(t,sol[:,0],label='x')
plot(t,sol[:,1],label='y')
xlabel('t')
legend()
title('van der Pol, $\mu$=%g' % mu)
show()
