#!/usr/bin/env python3
"""Functional Python Programming

Chapter 16, Example Set 2

See  http://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm
"""

# Original data.
# Three rows for each shift.
# Four columns for each defect.
expected_defects = [
    [15, 21, 45, 13],
    [26, 31, 34, 5],
    [33, 17, 49, 20],
]

# Raw data reader based on qa_data.csv file.

import csv
from collections import Counter
from types import SimpleNamespace


def defect_reduce(input):
    """
    >>> with open("../qa_data.csv", newline="" ) as input:
    ...     defects= defect_reduce( input )
    >>> len(defects)
    12
    >>> sum( defects.values() )
    309
    """
    rdr = csv.DictReader(input)
    assert sorted(rdr.fieldnames) == ["defect_type", "serial_number", "shift"]
    rows_ns = (SimpleNamespace(**row) for row in rdr)
    defects = ((row.shift, row.defect_type)
               for row in rows_ns
               if row.defect_type)
    tally = collections.Counter(defects)
    return tally


# Alternative reader based on summaries instead of details

import collections
import csv


def defect_counts(source):
    """
    >>> import io
    >>> source= io.StringIO('''shift,defect_code,count
    ... 1,A,15
    ... 2,A,26
    ... 3,A,33
    ... 1,B,21
    ... 2,B,31
    ... 3,B,17
    ... 1,C,45
    ... 2,C,34
    ... 3,C,49
    ... 1,D,13
    ... 2,D,5
    ... 3,D,20''' )
    >>> defects= defect_counts( source )
    >>> len(defects)
    12
    >>> sum( defects.values() )
    309
    """
    rdr = csv.DictReader(source)
    assert rdr.fieldnames == ["shift", "defect_code", "count"]
    convert = map(
        lambda d: ((d['shift'], d['defect_code']), int(d['count'])),
        rdr)
    return collections.Counter(dict(convert))


def chi2_eval(defects):
    """
    >>> with open("../qa_data.csv", newline="" ) as input:
    ...     defects= defect_reduce( input )
    >>> chi2= chi2_eval(defects) #doctest: +NORMALIZE_WHITESPACE
    Total 309
    Shift Total (('1', 94), ('2', 96), ('3', 119))
    Type Total (('A', 74), ('B', 69), ('C', 128), ('D', 38))
    Prob(shift) of defect (('1', Fraction(94, 309)), ('2', Fraction(32, 103)), ('3', Fraction(119, 309)))
    Prob(type) of defect (('A', Fraction(74, 309)), ('B', Fraction(23, 103)), ('C', Fraction(128, 309)), ('D', Fraction(38, 309)))
    <BLANKLINE>
    Contingency Table
    obs exp    obs exp    obs exp    obs exp
     15 22.51   21 20.99   45 38.94   13 11.56   94
     26 22.99   31 21.44   34 39.77    5 11.81   96
     33 28.50   17 26.57   49 49.29   20 14.63  119
     74         69        128         38        309
    >>> chi2.limit_denominator(100)
    Fraction(1400, 73)
    """
    total = sum(defects.values())
    print("Total {0}".format(total))

    shift_totals = sum((collections.Counter({s: defects[s, d]})
                        for s, d in defects), collections.Counter())
    print("Shift Total {0}".format(
        tuple((s, shift_totals[s])
              for s in sorted(shift_totals))))

    type_totals = sum((collections.Counter({d: defects[s, d]})
                       for s, d in defects), collections.Counter())
    print("Type Total {0}".format(
        tuple((t, type_totals[t])
              for t in sorted(type_totals))))

    from fractions import Fraction
    P_shift = dict((shift, Fraction(shift_totals[shift], total))
                   for shift in sorted(shift_totals))
    print("Prob(shift) of defect {0}".format(
        tuple((s, P_shift[s]) for s in sorted(P_shift))))

    P_type = dict((type, Fraction(type_totals[type], total)) for type in sorted(type_totals))
    print("Prob(type) of defect {0}".format(
        tuple((t, P_type[t]) for t in sorted(P_type))))

    expected = dict(
        ((s, t), P_shift[s] * P_type[t] * total)
        for t in P_type
        for s in P_shift
    )

    print("\nContingency Table")
    print("obs exp    " * len(type_totals))
    for s in sorted(shift_totals):
        pairs = ["{0:3d} {1:5.2f}".format(
            defects[s, t], float(expected[s, t]))
                 for t in sorted(type_totals)]
        print("{0}  {1:3d}".format(
            "  ".join(pairs), shift_totals[s]))
    footers = ["{0:3d}      ".format(type_totals[t]) for t in sorted(type_totals)]
    print("{0}  {1:3d}".format("  ".join(footers), total))

    # Difference

    diff = lambda e, o: (e - o) ** 2 / e

    chi2 = sum(diff(expected[s, t], defects[s, t])
               for s in shift_totals
               for t in type_totals
               )
    return chi2


def demo():
    with open("../qa_data.csv", newline="") as input:
        defects = defect_reduce(input)
    chi2 = chi2_eval(defects)
    print("χ² = {0:.2f}".format(float(chi2)))
    ## print( "χ² = {0:.2f}, P = {1:.5f}".format(chi2, cdf(chi2, 6) ) )


def test():
    import doctest
    doctest.testmod(verbose=1)


if __name__ == "__main__":
    #test()
    demo()
