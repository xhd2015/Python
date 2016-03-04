from factorial import ramanujan_factorial
from factorial import stirling_factorial
import numpy as np
import matplotlib.pyplot as plt

N = 50
numbers = np.arange(1, N)
factorials = np.cumprod(numbers, dtype=float)

def error(approximations):
   return (factorials - approximations)/factorials

plt.plot(error(ramanujan_factorial(numbers)), 'b-', label='Ramanujan')
plt.plot(error(stirling_factorial(numbers)), 'ro', label='Stirling')
plt.title('Factorial approximation relative errors')
plt.xlabel('n')
plt.ylabel('Relative error')
plt.grid()
plt.legend(loc='best')
plt.show()
