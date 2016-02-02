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


class Star(object):
    def __init__(self, name, spectral_class, app_mag, abs_mag, parallax):
        self.name = name
        self.spectral_class = spectral_class
        self.app_mag = app_mag
        self.abs_mag = abs_mag
        self.parallax = parallax


def parse_stars(filename):
    pass


def key_app_mag(star):
    pass


if __name__ == "__main__":
    stars = parse_stars('stars.dat')
