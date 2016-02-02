#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    try:
        for i in inclusive_range(10): print(i, end=' ')
    except TypeError as e:
        print(e)
    else:
        print('\nDone!')

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1:
            raise TypeError('at least one parameter requires')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args[0], args[1]
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args[0], args[1], args[2]
        else:
            raise TypeError('maximum 3 parameters required, got {}'.format(numargs))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


if __name__ == "__main__": main()
