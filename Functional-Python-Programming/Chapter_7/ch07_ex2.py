#!/usr/bin/env python3
"""Functional Python Programming

Chapter 7, Example Set 2
"""
from Chapter_3.ch03_ex5 import series, head_map_filter, row_iter

def rank_y( iterable ):
    return enumerate( sorted( iterable, key=lambda p: p.y ) )

def rank_x( ranked_iterable ):
    return enumerate( sorted( ranked_iterable, key=lambda rank: rank[1].x ) )

test_ranking= """
>>> with open("Anscombe.txt") as source:
...    data = tuple(head_map_filter(row_iter(source)))
...    series_I= tuple(series(0,data))
...    series_II= tuple(series(1,data))
...    series_III= tuple(series(2,data))
...    series_IV= tuple(series(3,data))

>>> y_rank= tuple( rank_y( series_I) )
>>> print( y_rank )
((0, Pair(x=4.0, y=4.26)), (1, Pair(x=7.0, y=4.82)), (2, Pair(x=5.0, y=5.68)), (3, Pair(x=8.0, y=6.95)), (4, Pair(x=6.0, y=7.24)), (5, Pair(x=13.0, y=7.58)), (6, Pair(x=10.0, y=8.04)), (7, Pair(x=11.0, y=8.33)), (8, Pair(x=9.0, y=8.81)), (9, Pair(x=14.0, y=9.96)), (10, Pair(x=12.0, y=10.84)))
>>> xy_rank= tuple( rank_x( y_rank) )
>>> print( xy_rank )
((0, (0, Pair(x=4.0, y=4.26))), (1, (2, Pair(x=5.0, y=5.68))), (2, (4, Pair(x=6.0, y=7.24))), (3, (1, Pair(x=7.0, y=4.82))), (4, (3, Pair(x=8.0, y=6.95))), (5, (8, Pair(x=9.0, y=8.81))), (6, (6, Pair(x=10.0, y=8.04))), (7, (7, Pair(x=11.0, y=8.33))), (8, (10, Pair(x=12.0, y=10.84))), (9, (5, Pair(x=13.0, y=7.58))), (10, (9, Pair(x=14.0, y=9.96))))

"""

__test__ = {
    "test_ranking": test_ranking,
}

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
