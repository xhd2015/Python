#!/usr/bin/python3
# testimonials.py by Bill Weinman <http://bw.org/contact/>
# Copyright (c) 2010 The BearHeart Group, LLC
# created 2010-04-23
#

from bwDB import bwDB
from bwConfig import configFile
import random
import os

__version__ = "1.0.1"

g = dict(
    config_file = 'db.conf',
    table_name = 'testimonial'
)

def main():
    init()
    db = g['db']
    idlist = []

    # build a list of ids
    for r in db.sql_query(' SELECT id FROM {} '.format(g['table_name'])):
        idlist.append(r[0])

    # get the count of records to display
    try: count = int(os.environ.get('QUERY_STRING', 3))
    except ValueError: error("Invalid query string, must be a number")
    idcount = len(idlist)

    # check that the count is not too big
    maxcount = idcount // 4
    if count > maxcount:
        error('There are {} records in the database. '.format(idcount) +
            'For good randomness, you cannot display more than {} at a time.'.format( maxcount )
        )

    # build the list of random ids
    result_ids = []
    while len(result_ids) < count:
        randindex = random.randint(0, len(idlist) - 1)
        randid = idlist[randindex]
        del idlist[randindex]   # don't use that one again
        result_ids += [ randid ]

    # display them
    for id in result_ids:
        printrec(id)

def printrec(id):
    db = g['db']
    rec = db.getrec(id)
    print('<div class="testimonial">')
    print('<p class="testimonial">{}</p>'.format(rec['testimonial']))
    print('<p class="byline">&mdash;{}</p>'.format(rec['byline']))
    print('</div>')


def init():
    send_header()
    g['config'] = configFile(g['config_file']).recs()
    g['db'] = bwDB(filename = g['config']['db'], table = g['table_name'])

def send_header():
    print('Content-type: text/html\n\n', end = '')

def error(e):
    print(e)
    exit(0)

if __name__ == "__main__": main()

