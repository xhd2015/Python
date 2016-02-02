#!/usr/bin/env python3
"""Functional Python Programming

Chapter 10, Example Set 5
"""

from itertools import groupby

from collections import defaultdict
def partition( iterable, key=lambda x:x ):
    """Sort not required."""
    pd = defaultdict(list)
    for row in iterable:
        pd[key(row)].append( row )
    for k in sorted(pd):
        yield k, iter(pd[k])

def partition_s( iterable, key= lambda x:x ):
    """Sort required"""
    return groupby( iterable, key )


test_data = """
>>> data = [('4', 6.1), ('1', 4.0), ('2', 8.3), ('2', 6.5), ('1', 4.6),
... ('2', 6.8), ('3', 9.3), ('2', 7.8), ('2', 9.2), ('4', 5.6),
... ('3', 10.5), ('1', 5.8), ('4', 3.8), ('3', 8.1), ('3', 8.0),
... ('1', 6.9), ('3', 6.9), ('4', 6.2), ('1', 5.4), ('4', 5.8)]

>>> for group, group_iter in partition( list(data), key=lambda x:x[0] ):
...     print( group, tuple(group_iter) )
1 (('1', 4.0), ('1', 4.6), ('1', 5.8), ('1', 6.9), ('1', 5.4))
2 (('2', 8.3), ('2', 6.5), ('2', 6.8), ('2', 7.8), ('2', 9.2))
3 (('3', 9.3), ('3', 10.5), ('3', 8.1), ('3', 8.0), ('3', 6.9))
4 (('4', 6.1), ('4', 5.6), ('4', 3.8), ('4', 6.2), ('4', 5.8))
>>> for group, group_iter in partition_s( sorted(data), key=lambda x:x[0] ):
...     print( group, tuple(group_iter) )
1 (('1', 4.0), ('1', 4.6), ('1', 5.4), ('1', 5.8), ('1', 6.9))
2 (('2', 6.5), ('2', 6.8), ('2', 7.8), ('2', 8.3), ('2', 9.2))
3 (('3', 6.9), ('3', 8.0), ('3', 8.1), ('3', 9.3), ('3', 10.5))
4 (('4', 3.8), ('4', 5.6), ('4', 5.8), ('4', 6.1), ('4', 6.2))

"""

mean= lambda seq: sum(seq)/len(seq)
var= lambda mean, seq: sum( (x-mean)**2/mean for x in seq)

def summarize( key_iter ):
    key, item_iter= key_iter
    values= tuple((v for k,v in item_iter))
    μ= mean(values)
    return key, μ, var(μ, values)

test_summarize="""
>>> data = [('4', 6.1), ('1', 4.0), ('2', 8.3), ('2', 6.5), ('1', 4.6),
... ('2', 6.8), ('3', 9.3), ('2', 7.8), ('2', 9.2), ('4', 5.6),
... ('3', 10.5), ('1', 5.8), ('4', 3.8), ('3', 8.1), ('3', 8.0),
... ('1', 6.9), ('3', 6.9), ('4', 6.2), ('1', 5.4), ('4', 5.8)]

>>> partition1= partition( list(data), key=lambda x:x[0] )
>>> groups1= map( summarize, partition1 )
>>> for g, s, s2 in groups1:
...     print( g, round(s,2), round(s2,2) )
1 5.34 0.93
2 7.72 0.63
3 8.56 0.89
4 5.5 0.7

>>> partition2= partition_s( sorted(data), key=lambda x:x[0] )
>>> groups2= map( summarize, partition2 )
>>> for g, s, s2 in groups2:
...     print( g, round(s,2), round(s2,2) )
1 5.34 0.93
2 7.72 0.63
3 8.56 0.89
4 5.5 0.7


"""

__test__ = {
    "test_data": test_data,
    "test_summarize": test_summarize,
}

def test():
    import doctest
    doctest.testmod( verbose=1 )

if __name__ == "__main__":
    test()
    #performance()