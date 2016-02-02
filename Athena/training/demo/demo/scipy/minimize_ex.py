from scipy import special, r_, optimize
import pylab as plt

x = r_[2:7.1:.1]
j1x = special.j1(x)
plt.plot(x,j1x,'-')
plt.hold('on')
x_min = optimize.fminbound(special.j1,4,7)
plt.plot([x_min], [special.j1(x_min)],'ro')
plt.hold('off')
plt.show()
