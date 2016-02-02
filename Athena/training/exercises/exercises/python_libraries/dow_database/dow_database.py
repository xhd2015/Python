"""
Dow Database
-------------

Topics: Database DB-API 2.0

The database table in the file 'dow2008.csv' has records holding the
daily performance of the Dow Jones Industrial Average from the
beginning of 2008.  The table has the following columns (separated by
a comma).

DATE        OPEN      HIGH      LOW       CLOSE     VOLUME      ADJ_CLOSE
2008-01-02  13261.82  13338.23  12969.42  13043.96  3452650000  13043.96
2008-01-03  13044.12  13197.43  12968.44  13056.72  3429500000  13056.72
2008-01-04  13046.56  13049.65  12740.51  12800.18  4166000000  12800.18
2008-01-07  12801.15  12984.95  12640.44  12827.49  4221260000  12827.49
2008-01-08  12820.9   12998.11  12511.03  12589.07  4705390000  12589.07
2008-01-09  12590.21  12814.97  12431.53  12735.31  5351030000  12735.31

1. Create a new sqlite database. Create a table that has the same
   structure (use real for all the columns except the date column).

2. Insert all the records from dow.csv into the database.

3. Select (and print out) the records from the database that have a volume
   greater than 5.5 billion.   How many are there?

Bonus
~~~~~
1. Select the records which have a spread between high and low that is greater
   than 4% and sort them in order of that spread.

2. Select the records which have an absolute difference between open and close
   that is greater than 1% (of the open) and sort them in order of that spread.

See :ref:`dow-database-solution`.
"""
import sqlite3 as db
