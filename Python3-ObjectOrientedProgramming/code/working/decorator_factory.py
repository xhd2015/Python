__author__ = 'Plamen'


# Append a string to the function output - "decorator factory"
def append_str(s):
    def dec(f):
        def new_func(*args, **kwargs):
            new_s = f(*args, **kwargs) + s
            return new_s

        return new_func

    return dec


@append_str(", World")
def hello():
    return "Hello"


@append_str(", Moon")
def goodnight():
    return "Good Night"


def main():
    print hello()
    print goodnight()


if __name__ == "__main__":
    main()
