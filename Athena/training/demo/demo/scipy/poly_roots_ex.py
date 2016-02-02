from numpy import poly1d, r_
import pylab as plt

p = poly1d([1.3,4,.6]) 
x = r_[-4:1:0.05] 
y = p(x) 
plt.plot(x,y,'-')
plt.hold('on')
r = p.roots
s = p(r) 
print "roots:", r
plt.plot(r.real, s.real,'ro')
plt.show()
