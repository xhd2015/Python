#!/usr/bin/env python3
# datetime.py by Bill Weinman <http://bw.org/contact/>
# Copyright (c) 2010 The BearHeart Group, LLC
# CGI/SSI version for bw.org
#

import time, saytime

t = time.localtime()
print("Content-type: text/html\n")
print(
    "In Phoenix, Arizona, it is now " +
    saytime.saytime_t(t).words() +
    time.strftime(', on %A, %d %B %Y.')
)


