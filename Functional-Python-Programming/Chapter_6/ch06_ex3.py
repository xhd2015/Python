#!/usr/bin/env python3
"""Functional Python Programming

Chapter 6, Example Set 3
"""
from Chapter_4.ch04_ex1 import haversine
import urllib.request
import xml.etree.ElementTree as XML
import re

def pick_lat_lon( lon, lat, alt ):
    return lat, lon
def comma_split( text ):
    return text.split(",")

def float_lat_lon3(file_obj):
    """
    Less than ideal parser: does too much in one hard-to-tweak step.

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
    >>> list(float_lat_lon3( doc ))
    [(37.54901619777347, -76.33029518659048)]
    """
    ns_map= {
        "ns0": "http://www.opengis.net/kml/2.2",
        "ns1": "http://www.google.com/kml/ext/2.2"}
    doc= XML.parse( file_obj )
    return (tuple(
        map( float, pick_lat_lon(*comma_split(coordinates.text)) ))
            for coordinates in
            doc.findall("./ns0:Document/ns0:Folder/"
            "ns0:Placemark/ns0:Point/ns0:coordinates", ns_map) )

test_float_lan_lon3= """
>>> import urllib.request
>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...    trip= tuple(float_lat_lon3(source))
>>> len(trip)
74
>>> trip[0]
(37.54901619777347, -76.33029518659048)
>>> trip[-1]
(38.976334, -76.473503)

"""

def comma_split( text ):
    return text.split(",")

def row_iter_kml( file_obj ):
    """
    More consistent with CSV parsing.
    Low-level produces rows of tuples of text.
    High-level produces application objects.

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

def float_lat_lon( row_iter ):
    return (
        tuple( map(float, pick_lat_lon(*row)) )
        for row in row_iter )

test_row_iter_kml= """
>>> import urllib.request
>>> with urllib.request.urlopen("file:./Winter%202012-2013.kml") as source:
...     trip = tuple( float_lat_lon(row_iter_kml(source)) )
>>> len(trip)
74
>>> trip[0]
(37.54901619777347, -76.33029518659048)
>>> trip[-1]
(38.976334, -76.473503)

"""

from collections import namedtuple
Color = namedtuple( "Color", ("red","green","blue","name") )

def row_iter_gpl( file_obj ):
    header_pat= re.compile(r"GIMP Palette\nName:\s*(.*?)\nColumns:\s*(.*?)\n#\n", re.M)
    def read_head( file_obj ):
        match= header_pat.match("".join( file_obj.readline() for _ in range(4)))
        return (match.group(1), match.group(2)), file_obj
    def read_tail( headers, file_obj ):
        return headers, (next_line.split() for next_line in file_obj)
    return read_tail( *read_head(file_obj) )

def color_palette( headers, row_iter ):
    name, columns = headers
    colors = tuple(
        Color(int(r), int(g), int(b), " ".join(name))
        for r,g,b,*name in row_iter )
    return name, columns, colors

test_row_iter_gpl="""
>>> with open("crayola.gpl") as source:
...     name, columns, colors = color_palette( *row_iter_gpl(source) )
>>> name
'Crayola'
>>> columns
'16'
>>> len(colors)
133
"""

__test__ = {
    "test_float_lan_lon3": test_float_lan_lon3,
    "test_row_iter_kml": test_row_iter_kml,
    "test_row_iter_gpl": test_row_iter_gpl,
}

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
