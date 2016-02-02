#!/usr/bin/env python3
"""Functional Python Programming

Chapter 9, Example Set 1
"""
import time
from PIL import Image

from collections import namedtuple
Color= namedtuple("Color", ("rgb","name"))

from itertools import *
import csv
def get_colors():
    with open("crayola.gpl") as source:
        rdr= csv.reader( source, delimiter='\t' )
        rows = dropwhile( lambda row: row[0] != '#', rdr )
        color_rows = islice( rows, 1, None )
        colors = tuple( Color(tuple(map(int,color.split())), name) for color, name in color_rows )
    return colors

def pixel_iter( img ):
    w, h = img.size
    return ((c,img.getpixel(c)) for c in product(range(w), range(h)))

import math
def euclidean( pixel, color ):
   return math.sqrt( sum( map( lambda x,y: (x-y)**2, pixel, color.rgb ) ) )

def manhattan( pixel, color ):
    return sum( map( lambda x,y: abs(x-y), pixel, color.rgb ) )

def max_d( pixel, color ):
    return max( map( lambda x,y: abs(x-y), pixel, color.rgb ) )

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


def matching_1( pixels, colors ):
    xy= lambda xyp_c: xyp_c[0][0]
    p= lambda xyp_c: xyp_c[0][1]
    c= lambda xyp_c: xyp_c[1]

    distances= ( (xy(item), p(item), c(item), euclidean(p(item), c(item)))
        for item in product(pixels, colors) )
    for _, choices in groupby(distances, key=lambda xy_p_c_d: xy_p_c_d[0]):
        yield min(choices, key=lambda xypcd: xypcd[3] )

test_matching_1="""
>>> img= Image.open("IMG_2705.jpg")
>>> print(img) # doctest: +ELLIPSIS
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3648x2736 at ...

>>> colors= get_colors()
>>> color_subset= list(islice(colors,0,None,len(colors)//6))
>>> print( color_subset )
[Color(rgb=(239, 222, 205), name='Almond'), Color(rgb=(255, 255, 153), name='Canary'), Color(rgb=(28, 172, 120), name='Green'), Color(rgb=(48, 186, 143), name='Mountain Meadow'), Color(rgb=(255, 73, 108), name='Radical Red'), Color(rgb=(253, 94, 83), name='Sunset Orange'), Color(rgb=(255, 174, 66), name='Yellow Orange')]

>>> pixel_subset= tuple(take(10,pixel_iter(img)))

>>> print( list(matching_1(pixel_subset, color_subset)))
[((0, 0), (92, 139, 195), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.75868534480233), ((0, 1), (92, 139, 195), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.75868534480233), ((0, 2), (92, 139, 195), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.75868534480233), ((0, 3), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 4), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 5), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 6), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 7), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 8), (92, 139, 195), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.75868534480233), ((0, 9), (93, 140, 196), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 83.36666000266533)]

"""

test_matching_1_full="""
Takes a loooong time -- don't actually do this:

>>> colors= get_colors()
>>> img= Image.open("IMG_2705.jpg")
>>> revised= list( matching_1(pixel_iter(img), colors))
"""

def matching_2(  pixels, colors ):
    for xy, pixel in pixels:
        choices= map(
            lambda color: (xy, pixel,
                color, euclidean(pixel, color)),
            colors )
        yield min(choices, key=lambda xypcd: xypcd[3] )

test_matching_2="""
>>> img= Image.open("IMG_2705.jpg")
>>> print(img) # doctest: +ELLIPSIS
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3648x2736 at ...

>>> colors= get_colors()
>>> color_subset= list(islice(colors,0,None,len(colors)//6))
>>> print( color_subset )
[Color(rgb=(239, 222, 205), name='Almond'), Color(rgb=(255, 255, 153), name='Canary'), Color(rgb=(28, 172, 120), name='Green'), Color(rgb=(48, 186, 143), name='Mountain Meadow'), Color(rgb=(255, 73, 108), name='Radical Red'), Color(rgb=(253, 94, 83), name='Sunset Orange'), Color(rgb=(255, 174, 66), name='Yellow Orange')]

>>> pixel_subset= tuple(take(10,pixel_iter(img)))

>>> print( list(matching_2(pixel_subset, color_subset)))
[((0, 0), (92, 139, 195), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.75868534480233), ((0, 1), (92, 139, 195), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.75868534480233), ((0, 2), (92, 139, 195), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.75868534480233), ((0, 3), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 4), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 5), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 6), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 7), (91, 138, 194), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.18272324521742), ((0, 8), (92, 139, 195), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.75868534480233), ((0, 9), (93, 140, 196), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 83.36666000266533)]

"""

test_matching_2_full="""
Takes a loooong time -- don't actually do this:

>>> colors= get_colors()
>>> img= Image.open("IMG_2705.jpg")
>>> revised= list( matching_2(pixel_iter(img), colors))
"""

def performance():
    import timeit

    perf= timeit.timeit(
    """
euclidean( (92, 139, 195), Color(rgb=(239, 222, 205), name='Almond') )
    """,
    setup= """
from collections import namedtuple
Color= namedtuple("Color", ("rgb","name"))
import math
def euclidean( pixel, color ):
   return math.sqrt( sum( map( lambda x,y: (x-y)**2, pixel, color.rgb ) ) )
    """
    )
    print( "Euclidean", perf )

    perf= timeit.timeit(
    """
manhattan( (92, 139, 195), Color(rgb=(239, 222, 205), name='Almond') )
    """,
    setup= """
from collections import namedtuple
Color= namedtuple("Color", ("rgb","name"))
def manhattan( pixel, color ):
    return sum( map( lambda x,y: abs(x-y), pixel, color.rgb ) )
    """
    )
    print( "Manhattan", perf )

    perf= timeit.timeit( """
min(choices, key=lambda xypcd: xypcd[3] )
    """,
    setup="""
from collections import namedtuple
Color= namedtuple("Color", ("rgb","name"))
choices= (((0, 0), (92, 139, 195), Color(rgb=(239, 222, 205), name='Almond'), 169.10943202553784), ((0, 0), (92, 139, 195), Color(rgb=(255, 255, 153), name='Canary'), 204.42357985320578), ((0, 0), (92, 139, 195), Color(rgb=(28, 172, 120), name='Green'), 103.97114984456024), ((0, 0), (92, 139, 195), Color(rgb=(48, 186, 143), name='Mountain Meadow'), 82.75868534480233), ((0, 0), (92, 139, 195), Color(rgb=(255, 73, 108), name='Radical Red'), 196.19887869200477), ((0, 0), (92, 139, 195), Color(rgb=(253, 94, 83), name='Sunset Orange'), 201.2212712413874), ((0, 0), (92, 139, 195), Color(rgb=(255, 174, 66), name='Yellow Orange'), 210.7961100210343))
    """
    )
    print( "min(choices,...)", perf )

def gather_data():
    img= Image.open("IMG_2705.jpg")

    from collections import defaultdict, Counter
    palette= defaultdict(list)
    for xy_p in pixel_iter(img):
        xy, p = xy_p
        palette[p].append( xy )

    w, h = img.size
    print( "total pixels", w*h )
    print( "total colors", len(palette) )

    masks = [ 0b11100000, 0b11110000, 0b11111000, 0b11111100 ]
    subsets= dict( (m,Counter()) for m in masks)
    for c in palette:
        for m in masks:
            masked_color= tuple(map(lambda x: x&m, c))
            subsets[m][masked_color] += 1
    for m in masks:
        print( bin(m), len(subsets[m]) )

def make_color_map():
    colors= get_colors()
    bit3= range(0,256,0b100000)

    best= (min( (euclidean(rgb, c), rgb, c ) for c in colors )
           for rgb in product(bit3, bit3, bit3) )
    color_map = dict( (b[1], b[2].rgb) for b in best )
    return color_map

test_make_color_map="""
>>> m= make_color_map()
>>> len(m)
512
>>> m[(0,0,0)]
(0, 0, 0)
>>> m[(224,224,224)]
(219, 215, 210)

"""

def clone_picture( color_map, filename="IMG_2705.jpg" ):
    img= Image.open(filenmame)
    clone = img.copy()
    for xy, p in pixel_iter(img):
        r, g, b = p
        repl = color_map[ (0b11100000&r, 0b11100000&g, 0b11100000&b) ]
        clone.putpixel( xy, repl )
    clone.show()

def demo():
    start = time.perf_counter()
    color_map= make_color_map()
    clone_picture( color_map )
    print( time.perf_counter()-start, "seconds" )

__test__ = {
    "test_matching_1": test_matching_1,
    # skip: "test_matching_1_full": test_matching_1_full,
    "test_matching_2": test_matching_2,
    # skip: "test_matching_2_full": test_matching_2_full,
    "test_make_color_map": test_make_color_map,
}

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
    #gather_data()
    #performance()
    #demo()
