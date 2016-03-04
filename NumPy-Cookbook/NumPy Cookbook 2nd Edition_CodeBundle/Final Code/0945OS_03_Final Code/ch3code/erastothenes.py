from __future__ import print_function
import numpy as np

LIM = 10 ** 6
N = 10 ** 9
P = 10001
primes = []
p = 2

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

def sieve_primes(a, p):
   #2. Sieve out multiples of p
   a = a[a % p != 0]

   return a

for i in xrange(3, N, LIM):
   #1. Create a list of consecutive integers
   a = np.arange(i, i + LIM, 2)

   while len(primes) < P:
      a = sieve_primes(a, p)
      primes.append(p)

      p = a[0]

print(len(primes), primes[P-1])
