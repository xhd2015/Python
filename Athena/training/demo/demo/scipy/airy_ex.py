from scipy import special 
from numpy import r_, transpose
import pylab as plt
z = r_[-5:1.5:100j]
vals = special.airy(z)
plt.plot(z,transpose(vals))
plt.xlabel('z')
plt.title('Airy Functions and Derivatives')
plt.show()
