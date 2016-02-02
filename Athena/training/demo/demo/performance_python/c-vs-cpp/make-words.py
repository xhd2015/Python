#!/usr/bin/env python
import sys
from time import clock
from random import randrange

def main(words_fh, output_fh, time_limit):

    words = [w for w in words_fh.read().split() if len(w) > 3]

    size = len(words)
    chunk = size / 100 or size
    otime = clock()

    while clock() - otime < time_limit:
        owords = [words[randrange(size)] for _ in range(chunk)]
        output_fh.write(' '.join(owords))
        output_fh.write('\n')
    output_fh.flush()

if __name__ == '__main__':
    main(sys.stdin, sys.stdout, time_limit=10)
