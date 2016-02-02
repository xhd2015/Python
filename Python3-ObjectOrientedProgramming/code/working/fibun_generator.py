__author__ = 'Plamen'


def fib(N):
    a, b = 0, 1
    for count in range(N):
        yield b
        a, b = b, a + b


def main():
    x = []
    for f in fib(8):
        x.append(f)
    print x

if __name__ == "__main__":
    main()
