import numpy as np
import timeit
import matplotlib.pyplot as plt


# This program measures the performance of the NumPy sort function
# and plots time vs array size.
integers = []

def dosort():
   integers.sort()

def measure():
   timer = timeit.Timer('dosort()', 'from __main__ import dosort')

   return timer.timeit(10 ** 2)

powersOf2 = np.arange(0, 19)
sizes = 2 ** powersOf2

times = np.array([])

for size in sizes:
   integers = np.random.random_integers(1, 10 ** 6, size)
   times = np.append(times, measure())

fit = np.polyfit(sizes * powersOf2, times, 1)
print fit
plt.title("Sort array sizes vs execution times")
plt.xlabel("Size")
plt.ylabel("(s)")
plt.semilogx(sizes, times, 'ro')
plt.semilogx(sizes, np.polyval(fit, sizes * powersOf2))
plt.grid()
plt.show()
