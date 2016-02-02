#!/usr/bin/env python3
"""Functional Python Programming

Chapter 4, Example Set 1
"""

import urllib.request
import xml.etree.ElementTree as XML

def comma_split( text ):
    return text.split(",")

def row_iter_kml( file_obj ):
    """Iterate over rows in a KML file.

    >>> import io
    >>> doc= io.StringIO('''<?xml version="1.0" encoding="UTF-8"?>
    ... <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    ... <Document>
    ...	    <Folder>
    ...		<name>Waypoints.kml</name>
    ...		<open>1</open>
    ...		<Placemark>
    ...			<Point>
    ...				<coordinates>-76.33029518659048,37.54901619777347,0</coordinates>
    ...			</Point>
    ...		</Placemark>
    ...    </Folder>
    ... </Document>
    ... </kml>''')
    >>> list(row_iter_kml( doc ))
    [['-76.33029518659048', '37.54901619777347', '0']]
    """
    ns_map= {
        "ns0": "http://www.opengis.net/kml/2.2",
        "ns1": "http://www.google.com/kml/ext/2.2"}
    doc= XML.parse( file_obj )
    return (comma_split(coordinates.text)
            for coordinates in
            doc.findall("./ns0:Document/ns0:Folder/"
            "ns0:Placemark/ns0:Point/ns0:coordinates", ns_map) )

def pick_lat_lon( lon, lat, alt ):
    return lat, lon

def float_lat_lon_a( row_iter ):
    """
    >>> data= [['-76.33029518659048', '37.54901619777347', '0']]
    >>> list(float_lat_lon_a( data ))
    [('37.54901619777347', '-76.33029518659048')]
    """
    return (
        pick_lat_lon(*row)
        for row in row_iter )

def float_lat_lon( row_iter ):
    """
    >>> data= [['-76.33029518659048', '37.54901619777347', '0']]
    >>> list(float_lat_lon( data ))
    [(37.54901619777347, -76.33029518659048)]
    """
    return (
        tuple( map(float, pick_lat_lon(*row)) )
        for row in row_iter )

def lat_lon_csv( source ):
    """Lat_lon values built from a CSV source.
    """
    rdr= csv.reader(source)
    header= next(rdr)
    return rdr.rows()

def float_from_pair( lat_lon_iter ):
    """Create float lat-lon pairs from string lat-lon pairs.

    >>> trip = [ ("1", "2"), ("2.718", "3.142") ]
    >>> tuple( float_from_pair( trip ) )
    ((1.0, 2.0), (2.718, 3.142))
    """
    return ( (float(lat), float(lon)) for lat,lon in lat_lon_iter )

def legs( lat_lon_iter ):
    """We can think of this as yielding list[0:1], list[1:2], list[2:3], ..., list[n-2,n-1]
    Another option is zip( list[0::2], list[1::2] )

    >>> trip = iter([ (0,0), (1,0), (1,1), (0,1), (0,0) ])
    >>> tuple( legs( trip ) )
    (((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((0, 1), (0, 0)))
    """
    start= next(lat_lon_iter)
    for end in lat_lon_iter:
        yield start, end
        start= end

def legs_filter(lat_lon_iter):
    begin= next(lat_lon_iter)
    for end in lat_lon_iter:
        if some_rule():
            continue
        yield begin, end
        begin= end

def pairs( iterable ):
    """Another way of pairing up values.

    >>> trip = iter([ (0,0), (1,0), (1,1), (0,1), (0,0) ])
    >>> tuple( pairs( trip ) )
    (((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((0, 1), (0, 0)))
    """
    def pair_from( head, iterable_tail ):
        nxt= next(iterable_tail)
        yield head, nxt
        # Doesn't consume the recursed iterable:
        #return pair_from( nxt, iterable_tail )
        # Pre Python 3.3
        #for pairs in pair_from( nxt, iterable_tail ):
        #    yield pairs
        # Python 3.3 yield from
        yield from pair_from( nxt, iterable_tail )
    try:
        return pair_from( next(iterable), iterable )
    except StopIteration:
        return

from math import radians, sin, cos, sqrt, asin

MI= 3959
NM= 3440
KM= 6371

def haversine( point1, point2, R=NM ):
    """Distance between points.
    point1 and point2 are two-tuples of latitude and longitude.
    R is radius, R=MI computes in miles.

    >>> round(haversine((36.12, -86.67), (33.94, -118.40), R=6372.8), 5)
    2887.25995
    """
    lat_1, lon_1= point1
    lat_2, lon_2= point2

    Δ_lat = radians(lat_2 - lat_1)
    Δ_lon = radians(lon_2 - lon_1)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)

    a = sin(Δ_lat/2)**2 + cos(lat_1)*cos(lat_2)*sin(Δ_lon/2)**2
    c = 2*asin(sqrt(a))

    return R * c

import itertools
def limits( iterable ):
    """A possible way to get limits from an iterable.
    This has unpleasant consequences on the original iterable, though,
    since this functions consumes it.

    >>> data = iter( [1,9,2,8,3,7,4,6,5] )
    >>> limits(data)
    (9, 1)
    >>> list(data)
    []
    """
    max_tee, min_tee = itertools.tee( iterable, 2 )
    return max(max_tee), min(min_tee)

def group_sort1( trip ):
    """Group legs into bins with distances 5 nm or less.

    >>> trip = [ ('s1', 'e1', 1), ('s4', 'e4', 4.9), ('s5', 'e5', 5), ('s6', 'e6', 6)]
    >>> group_sort1(trip)
    {0: 2, 5: 2}
    """
    def group( data ):
        previous, count = None, 0
        for d in sorted(data):
            if d == previous:
                count += 1
            elif previous is not None: # and d != previous
                yield previous, count
                previous, count = d, 1
            elif previous is None:
                previous, count = d, 1
            else:
                raise Exception( "Bad bad design problem." )
        yield previous, count
    quantized= (5*(dist//5) for start,stop,dist in trip)
    return dict( group(quantized) )

    # return sorted(tuple(group(quantized)),
    #    key=lambda x:x[1], reverse=True )

def group_sort2( trip ):
    """Group legs into bins with distances 5 nm or less.

    >>> trip = [ ('s1', 'e1', 1), ('s4', 'e4', 4.9), ('s5', 'e5', 5), ('s6', 'e6', 6)]
    >>> group_sort2(trip)
    {0: 2, 5: 2}
    """
    def group( data ):
        sorted_data= iter(sorted(data))
        previous, count = next(sorted_data), 1
        for d in sorted_data:
            if d == previous:
                count += 1
            elif previous is not None: # and d != previous
                yield previous, count
                previous, count = d, 1
            else:
                raise Exception( "Bad bad design problem." )
        yield previous, count
    quantized= (5*(dist//5) for start,stop,dist in trip)
    try:
        return dict( group(quantized) )
    except StopIteration:
        return dict()

    # return sorted(tuple(group(quantized)),
    #    key=lambda x:x[1], reverse=True )

from collections import Counter
def group_Counter( trip ):
    """Group legs into bins with distances 5 nm or less.

    >>> trip = [ ('s1', 'e1', 1), ('s4', 'e4', 4.9), ('s5', 'e5', 5), ('s6', 'e6', 6)]
    >>> group_Counter(trip)
    [(0, 2), (5, 2)]
    """
    quantized= (5*(dist//5) for start,stop,dist in trip)
    return Counter( quantized ).most_common()

test_parse_1 = """
>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...     v0= list(row_iter_kml(source))
>>> len(v0)
74
>>> v0[0]
['-76.33029518659048', '37.54901619777347', '0']
>>> v0[-1]
['-76.47350299999999', '38.976334', '0']

>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...     v1= tuple(float_lat_lon_a(row_iter_kml(source)))
>>> len(v1)
74
>>> v1[0]
('37.54901619777347', '-76.33029518659048')
>>> v1[-1]
('38.976334', '-76.47350299999999')

>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...     v2= tuple(float_lat_lon(row_iter_kml(source)))
>>> len(v2)
74
>>> v2[0]
(37.54901619777347, -76.33029518659048)
>>> v2[-1]
(38.976334, -76.473503)
"""

test_parse_2 = """
>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...     v0= tuple(legs(float_lat_lon(row_iter_kml(source)) ) )
>>> len(v0)
73
>>> v0[0]
((37.54901619777347, -76.33029518659048), (37.840832, -76.273834))
>>> v0[-1]
((38.330166, -76.458504), (38.976334, -76.473503))

>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...     v1= tuple(pairs(float_lat_lon(row_iter_kml(source)) ) )
>>> len(v1)
73
>>> v1[0]
((37.54901619777347, -76.33029518659048), (37.840832, -76.273834))
>>> v1[-1]
((38.330166, -76.458504), (38.976334, -76.473503))

>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...     v2= tuple(legs( float_from_pair(float_lat_lon(row_iter_kml(source)))))
>>> len(v2)
73
>>> v2[0]
((37.54901619777347, -76.33029518659048), (37.840832, -76.273834))
>>> v2[-1]
((38.330166, -76.458504), (38.976334, -76.473503))

"""

test_parse_3= """
>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...     flt= tuple( (float(lat), float(lon)) for lat,lon in float_lat_lon(row_iter_kml(source)) )
>>> len(flt)
74
>>> flt[0]
(37.54901619777347, -76.33029518659048)
>>> flt[-1]
(38.976334, -76.473503)

"""

trip1= """
>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...     trip= tuple( (start, end, round(haversine(start, end),4))
...         for start,end in legs( float_from_pair(float_lat_lon(row_iter_kml(source)))) )
>>> start, end, dist = trip[0]
>>> start, end, dist
((37.54901619777347, -76.33029518659048), (37.840832, -76.273834), 17.7246)
>>> start, end, dist = trip[-1]
>>> start, end, dist
((38.330166, -76.458504), (38.976334, -76.473503), 38.8019)

>>> lat_iter = (lat1 for lat1, lon1 in (start for start,stop,dist in trip) )
>>> north, south = limits( lat_iter )
>>> dist_iter= (dist for start,stop,dist in trip)
>>> total= sum( dist_iter )
>>> average = total/len(trip)

>>> print( "south", south )
south 23.9555
>>> print( "north", north )
north 38.992832
>>> print( "total", total )
total 2481.3662
>>> print( "average", round(average,3) )
average 33.991

>>> print( "Mode1", group_sort1(trip) )
Mode1 {0.0: 4, 65.0: 1, 35.0: 5, 5.0: 5, 70.0: 2, 40.0: 3, 10.0: 5, 45.0: 3, 15.0: 9, 80.0: 1, 50.0: 3, 115.0: 1, 20.0: 5, 85.0: 1, 55.0: 1, 25.0: 5, 60.0: 3, 125.0: 1, 30.0: 15}
>>> print( "Mode2", group_sort2(trip) )
Mode2 {0.0: 4, 65.0: 1, 35.0: 5, 5.0: 5, 70.0: 2, 40.0: 3, 10.0: 5, 45.0: 3, 15.0: 9, 80.0: 1, 50.0: 3, 115.0: 1, 20.0: 5, 85.0: 1, 55.0: 1, 25.0: 5, 60.0: 3, 125.0: 1, 30.0: 15}
>>> print( "Mode3", group_Counter(trip) )
Mode3 [(30.0, 15), (15.0, 9), (35.0, 5), (5.0, 5), (10.0, 5), (20.0, 5), (25.0, 5), (0.0, 4), (40.0, 3), (45.0, 3), (50.0, 3), (60.0, 3), (70.0, 2), (65.0, 1), (80.0, 1), (115.0, 1), (85.0, 1), (55.0, 1), (125.0, 1)]
"""

trip2= """
If we modify this demo so that path is an iterable, not a materialized tuple,
we'll see that the ``limit()`` function doesn't really do what we hoped.

>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...    path= tuple(float_from_pair(float_lat_lon(row_iter_kml(source))))
>>> north, south = limits( path )

>>> trip= tuple( (start, end, round(haversine(start, end),4))
...     for start,end in legs(iter(path)) )

>>> start, end, dist = trip[0]
>>> start, end, dist
((37.54901619777347, -76.33029518659048), (37.840832, -76.273834), 17.7246)
>>> start, end, dist = trip[-1]
>>> start, end, dist
((38.330166, -76.458504), (38.976334, -76.473503), 38.8019)

>>> dist_iter= (dist for start,stop,dist in trip)
>>> total= sum( dist_iter )
>>> average = total/len(trip)

>>> print( "south", south )
south (23.9555, -76.31633)
>>> print( "north", north )
north (38.992832, -76.451332)
>>> print( "total", total )
total 2481.3662
>>> print( "average", round(average,3) )
average 33.991
"""

__test__ = {
    'basic parse': test_parse_1,
    'pairs of legs': test_parse_2,
    'another basic parse': test_parse_3,
    'trip1 demo': trip1,
    'trip2 demo': trip2,
}


def test():
    """
    >>> trip = iter([ (0,0), (1,0), (1,1), (0,1), (0,0) ]) # about 240 NM
    >>> [ (lat, lon, round(haversine(lat, lon),4)) for lat,lon in legs(trip) ]
    [((0, 0), (1, 0), 60.0393), ((1, 0), (1, 1), 60.0302), ((1, 1), (0, 1), 60.0393), ((0, 1), (0, 0), 60.0393)]
    """
    import doctest
    doctest.testmod(verbose=2)

if __name__ == "__main__":
    test()
