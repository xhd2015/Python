#!/usr/bin/env python3
"""Functional Python Programming

Chapter 8, Example Set 1
"""

from Chapter_6.ch06_ex3 import row_iter_kml
from Chapter_4.ch04_ex1 import legs, haversine
import urllib.request

from collections import namedtuple
Leg = namedtuple( "Leg", ("order", "start", "end", "distance") )
Point = namedtuple( "Point", ("latitude", "longitude") )

def pick_lat_lon( lon, lat, alt ):
    return lat, lon

def float_lat_lon( row_iter ):
    return (
        Point( *map(float, pick_lat_lon(*row)) )
        for row in row_iter )

def ordered_leg_iter( pair_iter ):
    for order, pair in enumerate( pair_iter ):
        start, end = pair
        yield Leg(order, start, end, round(haversine(start, end),4))

test_parser= """
>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...    path_iter = float_lat_lon(row_iter_kml(source))
...    pair_iter = legs(path_iter)
...    trip_iter = ordered_leg_iter( pair_iter )
...    trip= tuple(trip_iter)

>>> len(trip)
73
>>> trip[0]
Leg(order=0, start=Point(latitude=37.54901619777347, longitude=-76.33029518659048), end=Point(latitude=37.840832, longitude=-76.273834), distance=17.7246)
>>> trip[-1]
Leg(order=72, start=Point(latitude=38.330166, longitude=-76.458504), end=Point(latitude=38.976334, longitude=-76.473503), distance=38.8019)

"""

__test__ = {
    "test_parser": test_parser,
}

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
