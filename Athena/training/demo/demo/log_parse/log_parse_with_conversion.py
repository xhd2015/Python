""" Example of using a regex to generate a structured numpy array
    from an apache log file.
"""
from numpy import fromregex, int16, int64

from itertools import izip
import re
import numpy as np

def fromregex(file, regexp, dtype, **kw):
    """
    Construct an array from a text file, using regular-expressions parsing.

    Array is constructed from all matches of the regular expression
    in the file. Groups in the regular expression are converted to fields.

    Parameters
    ----------
    file : str or file
        File name or file object to read.
    regexp : str or regexp
        Regular expression used to parse the file.
        Groups in the regular expression correspond to fields in the dtype.
    dtype : dtype or dtype list
        Dtype for the structured array

    Examples
    --------
    >>> f = open('test.dat', 'w')
    >>> f.write("1312 foo\\n1534  bar\\n444   qux")
    >>> f.close()
    >>> np.fromregex('test.dat', r"(\\d+)\\s+(...)",
    ...              [('num', np.int64), ('key', 'S3')])
    array([(1312L, 'foo'), (1534L, 'bar'), (444L, 'qux')],
          dtype=[('num', '<i8'), ('key', '|S3')])

    """
    if not hasattr(file, "read"):
        file = open(file,'r')
    if not hasattr(regexp, 'match'):
        regexp = re.compile(regexp)
    if not isinstance(dtype, np.dtype):
        dtype = np.dtype(dtype)

    seq = regexp.findall(file.read())
    if seq and not isinstance(seq[0], tuple):
        # make sure np.array doesn't interpret strings as binary data
        # by always producing a list of tuples
        seq = [(x,) for x in seq]

    if len(kw) != 0:
        converter_dict = kw
        converters = [converter_dict.get(name, lambda x: x) for name in dtype.names]
        for index in range(len(seq)):
            seq[index] = tuple(conv(value) for conv, value in izip(converters, seq[index]))
    output = np.array(seq, dtype=dtype)
    return output

#----------------------------------------------------------------------------
# Build a regular expression to parse an apache log file.
# It is borrowed from here, http://seehuhn.de/blog/52, and modified to
# not just match at the end of the line.
#----------------------------------------------------------------------------
parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]

regex_str = r'\s+'.join(parts)+r'\s*'

#----------------------------------------------------------------------------
# Read the access_log file and create an array with fields based
# on the groups found in the regular expression.
# 
# Hmm.  It would be nice if you could supply an extra factory conversion
# function for each field to create a datetime object for example...
#----------------------------------------------------------------------------
def size_converter(value):
    """ Convert a string to an int.  If the string is a '-', return 0.
    """  
    if value == '-':
        result = 0
    else:
        result = float(value)
       
    return result

import time, datetime

class Timezone(datetime.tzinfo):

    def __init__(self, name="+0000"):
        self.name = name
        seconds = int(name[:-2])*3600+int(name[-2:])*60
        self.offset = datetime.timedelta(seconds=seconds)

    def utcoffset(self, dt):
        return self.offset

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return self.name

def time_converter(value):
    date_and_time = value[:-6]
    timezone == value[-5:]    
    tt = time.strptime(date_and_time, "%d/%b/%Y:%H:%M:%S")
    tt = list(tt[:6]) + [ 0, Timezone(timezone) ]
    result = datetime.datetime(*tt)
    return result

import datetime

# This is aparently 10x or so faster than the above (need to add time zone...
month_map = {'Jan': 1, 'Feb': 2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 
    'Aug':8, 'Sept':7, 'Oct':9, 'Nov': 11, 'Dec': 12}

def apache_time(s):
    year = int(s[7:11])
    month = month_map[s[3:6]]
    day = int(s[0:2])
    hours = int(s[12:14])    
    minutes = int(s[15:17])
    seconds = int(s[18:20])
    timezone = Timezone(s[-5:])
    date_time = datetime.datetime(year, month, day, hours, minutes, seconds, 0, timezone)
    return date_time
         
ary = fromregex('access_log', regex_str,
                [('host', object), 
                 ('user', object),
                 ('time', object),
                 ('request', object),
                 ('status', int16), # I *think* this is guaranteed to be an int32...
                 ('size', int64), # Since this can be '-', it can't be a number.
                 ('referer', object),
                 ('agent', object),
                ], size=size_converter, time=apache_time)
                
#----------------------------------------------------------------------------
# Find all the requests that generated a 404
#----------------------------------------------------------------------------
ary404 = ary[ary['status'] == 404]
ary404['request']
requests404 = set(ary404['request'])

#----------------------------------------------------------------------------
# Generate a report on requests that generated 404 codes.
#----------------------------------------------------------------------------
print '-' * 50
print "Requests generating a 404 code:"
for request in requests404:
    print ' '*4, request
print '-' * 50

#----------------------------------------------------------------------------
# Unique hosts
#----------------------------------------------------------------------------
print 'Finding host names:'
import socket

addr_cache = {}
def reverse_dns(addr):
    
    if addr not in addr_cache:
        try:
            print 'looking up addr:', addr
            full_name, dummy, dummy2 = socket.gethostbyaddr(addr)
            # Chop off the leading part of the names.  The last two sections
            # are the best for grouping 'mit.edu', 'shell.com', etc.
            name_list = full_name.split('.')
            name = '.'.join(name_list[-2:])
        except socket.herror:
            # reverse lookup failed, we'll just use our address.
            name = addr    
        # Update the global cache so that we won't have to look this
        # address up later.
        addr_cache[addr] = name
    else:
        name = addr_cache[addr]
                
    return name

names = [reverse_dns(addr) for addr in ary['host']]

print '-' * 50
print "Requests generating a 404 code:"
for name in sorted(set(names)):
    print ' '*4, name
print '-' * 50            