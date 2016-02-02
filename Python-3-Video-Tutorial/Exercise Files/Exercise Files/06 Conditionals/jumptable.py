#!/usr/bin/python3
# jumptable.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class jumptable():
    jumptable = dict()
    print(type(jumptable))

    def set(self, k, v):
        self.jumptable[k] = v

    def go(self, index):
        if index in self.jumptable:
            self.jumptable[index]()
        elif 'default' in self.jumptable:
            self.jumptable['default']()
        else:
            raise RuntimeError('undefined jump: {}'.format(index))


def main():
    j = jumptable()
    j.set('one', one)
    j.set('two', two)
    j.set('three', three)
    j.set('default', default)

    try:
        j.go('seven')
    except RuntimeError as e:
        print(e)


def one():
    print('This is the "one" function.')


def two():
    print('This is the "two" function.')


def three():
    print('This is the "three" function.')


def default():
    print('this is the default function.')


if __name__ == "__main__": main()
