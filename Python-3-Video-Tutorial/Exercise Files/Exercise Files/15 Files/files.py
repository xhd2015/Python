#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC
from builtins import print


def main():
    f = open('lines.txt')
    for line in f:
        print(line, end = '')
    print('{2} is sum of {1} and {0}'.format(6,4,10))
if __name__ == "__main__": main()
