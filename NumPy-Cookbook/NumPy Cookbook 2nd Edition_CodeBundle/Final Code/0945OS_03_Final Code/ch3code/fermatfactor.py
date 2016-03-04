from __future__ import print_function
import numpy as np

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


N = 600851475143
LIM = 10 ** 6

def factor(n):
   #1. Create array of trial values
   a = np.ceil(np.sqrt(n))
   lim = min(n, LIM)
   a = np.arange(a, a + lim)
   b2 = a ** 2 - n

   #2. Check whether b is a square
   fractions = np.modf(np.sqrt(b2))[0]

   #3. Find 0 fractions
   indices = np.where(fractions == 0)

   #4. Find the first occurrence of a 0 fraction
   a = np.ravel(np.take(a, indices))[0]
   # Or a = a[indices][0]

   a = int(a)
   b = np.sqrt(a ** 2 - n) 
   b = int(b)
   c = a + b
   d = a - b

   if c == 1 or d == 1:
      return

   print(c, d)
   factor(c)
   factor(d)

factor(N)
#1234169 486847
#1471 839
#6857 71
