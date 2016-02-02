"""
Near Star Catalog
-----------------

Read data into a list of classes and sort in various ways.

The file `stars.dat` contains data about some of the nearest stars.  Data is
arranged in the file in fixed-width fields::

    0:17    Star name
    18:28   Spectral class
    29:34   Apparent magnitude
    35:40   Absolute magnitude
    41:46   Parallax in thousandths of an arc second

A typical line looks like::

    Proxima Centauri  M5  e      11.05 15.49 771.8

This module also contains a Star class with attributes for each of those
data items.

1. Write a function `parse_stars` which returns a list of Star instances,
    one for each star in the file `stars.dat`.

2. Sort the list of stars by apparent magnitude and print names and apparent
    magnitudes of the 10 brightest stars by apparent magnitude (lower numbers
    are brighter).

3. Sort the list of stars by absolute magnitude and print names, spectral class
    and absolute magnitudes the 10 faintest stars by absolute magnitude (lower
    numbers are brighter).

4. The distance of a star from the Earth in light years is given by::

        1/parallax in arc seconds * 3.26163626

    Sort the list by distance from the Earth and print names, spectral class
    and distance from Earth of the 10 closest stars.

Bonus
~~~~~

Spectral classes are codes of a form like 'M5', consisting of a letter and
a number, plus additional data about luminosity and abnormalities in the
spectrum.  Informally, the initial part of the code gives information about
the surface temperature and colour of the star.  From hottest to coldest, the
initial letter codes are 'OBAFGKM', with 'O' blue and 'M' red.  The number
indicates a relative position between the lettes, so 'A2' is hotter than 'A3'
which is in turn hotter than 'F0'.

Sort the list of stars and print the names, spectral classes and distances
of the 10 hottest stars in the list.

(Ignore stars with no spectral class or a spectral class that doesn't start
with 'OBAFGKM'.)


Notes
~~~~~

Data from:

    Preliminary Version of the Third Catalogue of Nearby Stars
    GLIESE W., JAHREISS H.
    Astron. Rechen-Institut, Heidelberg (1991)


See :ref:`sort-stars-solution`.

"""

from __future__ import with_statement

SPECTRAL_CODES = 'OBAFGKM'


class Star(object):
    """ An class which holds data about a star"""
    def __init__(self, name, spectral_class, app_mag, abs_mag, parallax):
        self.name = name
        self.spectral_class = spectral_class
        self.app_mag = app_mag
        self.abs_mag = abs_mag
        self.parallax = parallax

    def distance(self):
        """ The distance of the star from the earth in light years"""
        return 1 / self.parallax * 3.26163626


def parse_stars(filename):
    """Create a list of Star objects from a data file"""
    with open(filename) as star_file:
        stars = []
        for line in star_file.read().split('\n'):
            if line.strip() == '':
                continue
            name = line[:17].strip()
            spectral_class = line[18:28].strip()
            app_mag = float(line[29:34])
            abs_mag = float(line[35:40])
            parallax = float(line[41:46]) / 1000.0
            stars.append(Star(name=name, spectral_class=spectral_class,
                              app_mag=app_mag, abs_mag=abs_mag,
                              parallax=parallax))
    return stars


def key_app_mag(star):
    """Extract the apparent magnitude"""
    return star.app_mag


def key_abs_mag(star):
    """Extract the absolute magnitude"""
    return star.abs_mag


def key_distance(star):
    """Extract the distance"""
    return star.distance()


def key_spectral_class(star):
    """Return a tuple of numbers that orders spectral classes

    Returns a tuple (a, b), where a=0 if class is O, a=1 if class is B, etc
    and b is the numerical part of the code.
    """
    if not star.spectral_class:
        return (7, 0)
    code = star.spectral_class.split()[0]
    letter = code[0]
    if letter not in SPECTRAL_CODES:
        return (7, 0)
    letter_index = SPECTRAL_CODES.find(letter)
    if not code[1:]:
        return (7, 0)
    number = float(code[1:])
    return (letter_index, number)


if __name__ == "__main__":
    stars = parse_stars('stars.dat')

    print "10 brightest stars by apparent magnitude"
    stars.sort(key=key_app_mag)
    for star in stars[:10]:
        print "  %-17s %5.2f" % (star.name, star.app_mag)
    print

    print "10 faintest stars by absolute magnitude"
    stars.sort(key=key_abs_mag)
    stars.reverse()
    for star in stars[:10]:
        print "  %-17s %-10s %5.2f" % (star.name, star.spectral_class,
                                       star.abs_mag)
    print

    print "10 closest stars"
    stars.sort(key=key_distance)
    for star in stars[:10]:
        print "  %-17s %-10s %6.3f" % (star.name, star.spectral_class,
                                       star.distance())
    print

    print "10 hottest stars"
    stars.sort(key=key_spectral_class)
    for star in stars[:10]:
        print "  %-17s %-10s %6.3f" % (star.name, star.spectral_class,
                                       star.distance())
    print
