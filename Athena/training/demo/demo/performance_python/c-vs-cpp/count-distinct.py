#!/usr/bin/env python
from sys import stdin

words = set()
for line in stdin:
    words.update(line.split())
print "Words:", len(words)
