""" Example of using a regex to generate a structured numpy array
    from an apache log file.
"""
from numpy import fromregex, int32, int64

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
         
ary = fromregex('access_log', regex_str,
                [('host', object), 
                 ('user', object),
                 ('time', object),
                 ('request', object),
                 ('status', int32), # I *think* this is guaranteed to be an int32...
                 ('size', object), # Since this can be '-', it can't be a number.
                 ('referer', object),
                 ('agent', object),
                ])
                
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
