""" Efficient computation and delivery of the Fibonnaci series.
"""

def fib(elements=1000):
    a, b = 0, 1
    for count in range(elements):
        yield b
        a, b = b, a+b

fib_gen = fib()

for value in fib_gen:
    print value