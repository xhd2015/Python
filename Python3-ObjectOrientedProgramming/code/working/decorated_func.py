__author__ = 'Plamen'


def plus_one(f):
    def new_func(x):
        return f(x) + 1

    return new_func


def times_two(f):
    def new_func(x):
        return f(x) * 2

    return new_func


@plus_one
@times_two
def foo(x):
    return int(x)


def main():
    a = foo(13)
    print a


if __name__ == "__main__":
    main()
