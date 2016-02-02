#!/usr/bin/env python3
"""Functional Python Programming

Chapter 7, Example Set 1
"""

from Chapter_6.ch06_ex3 import row_iter_kml
from Chapter_4.ch04_ex1 import legs, haversine

import urllib.request

first_leg = ((29.050501, -80.651169), (27.186001, -80.139503), 115.1751)

def selectors_index( leg ):
    """
    >>> first_leg = ((29.050501, -80.651169), (27.186001, -80.139503), 115.1751)
    >>> selectors_index( first_leg )
    29.050501
    """
    start= lambda leg: leg[0]
    end= lambda leg: leg[1]
    distance= lambda leg: leg[2]
    latitude= lambda pt: pt[0]
    longitude= lambda pt: pt[1]

    print( latitude( start( leg ) ) )

def selectors_args( leg ):
    """
    >>> first_leg = ((29.050501, -80.651169), (27.186001, -80.139503), 115.1751)
    >>> selectors_args( first_leg )
    29.050501
    """
    start= lambda start, end, distance: start
    end= lambda start, end, distance: end
    distance= lambda start, end, distance: distance
    latitude= lambda lat, lon: lat
    longitude= lambda lat, lon: lon

    print( latitude( *start( *leg ) ) )

from collections import namedtuple
Leg = namedtuple( "Leg", ("start", "end", "distance") )
Point = namedtuple( "Point", ("latitude", "longitude") )

def pick_lat_lon( lon, lat, alt ):
    return lat, lon

def float_lat_lon( row_iter ):
    return (
        Point( *map(float, pick_lat_lon(*row)) )
        for row in row_iter )

def get_trip( url="file:./Winter%202012-2013.kml" ):
    with urllib.request.urlopen(url) as source:
        path_iter = float_lat_lon(row_iter_kml(source))
        pair_iter = legs(path_iter)
        trip_iter = (Leg(start, end, round(haversine(start, end),4))
            for start,end in pair_iter)
        trip= tuple(trip_iter)
    return trip

def find_given_leg_demo():
    """
    >>> find_given_leg_demo()
    29.050501
    """
    trip= get_trip()
    leg= next(filter( lambda leg: int(leg.distance)==115, trip ))
    print( leg.start.latitude )

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
