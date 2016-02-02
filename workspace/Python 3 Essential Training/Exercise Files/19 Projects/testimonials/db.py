#!/usr/bin/python3
# db.py by Bill Weinman <http://bw.org/contact/>
# Copyright (c) 2010 The BearHeart Group, LLC
# created 2010-04-23
#

import sys, os
import sqlite3

from bwCGI import bwCGI
from bwDB import bwDB
from bwTL import tlFile
from bwConfig import configFile

__version__ = "1.1.3"

# namespace container for global variables
g = dict(
    VERSION = 'db.py version {}'.format(__version__),
    config_file = 'db.conf',
    template_ext = '.html',
    table_name = 'testimonial',
    stacks = dict(
        messages = [],
        errors = [],
        hiddens = []
    )
)

def main():
    init()
    if 'a' in g['vars']: dispatch()
    main_page()

def init():
    g['cgi'] = bwCGI()
    g['cgi'].send_header()
    g['vars'] = g['cgi'].vars()
    g['linkback'] = g['cgi'].linkback()
    g['config'] = configFile(g['config_file']).recs()
    g['tl'] = tlFile(None, showUnknowns = True)
    g['db'] = bwDB( filename = g['config']['db'], table = g['table_name'] )

def dispatch():
    v = g['vars']
    a = v.getfirst('a')
    if a == 'add':
        add()
    elif a == 'edit_del':
        if 'edit' in v: edit()
        elif 'delete' in v: delete_confirm()
        else: error("invalid edit_del")
    elif a == 'update':
        if 'cancel' in v:
            message('Edit canceled')
            main_page()
        else: update()
    elif a == 'delete_do':
        if 'cancel' in v:
            message('Delete canceled')
            main_page()
        else: delete_do()
    else:
        error("unhandled jump: ", a)
        main_page()

def main_page():
    listrecs()
    hidden('a', 'add')
    page('main', 'Enter a new testimonial')

def listrecs():
    ''' display the database content '''
    db = g['db']
    v = g['vars']
    sql_limit = int(g['config'].get('sql_limit', 25))

    # how many records do we have?
    count = db.countrecs()
    message('There are {} records in the database. Add some more!'.format(count or 'no'))

    # how many pages do we have?
    numpages = count // int(sql_limit)
    if count % int(sql_limit): numpages += 1

    # what page is this?
    curpage = 0
    if 'jumppage' in v:
        curpage = int(v.getfirst('jumppage'))
    elif 'nextpage' in v:
        curpage = int(v.getfirst('pageno')) + 1
    elif 'prevpage' in v:
        curpage = int(v.getfirst('pageno')) - 1

    pagebar = list_pagebar(curpage, numpages)

    a = ''
    q = '''
        SELECT * FROM {}
          ORDER BY byline
          LIMIT ?
          OFFSET ?
    '''.format(g['table_name'])
    for r in db.sql_query(q, [sql_limit, (curpage * sql_limit)]):
        set_form_vars(**r)
        a += getpage('recline')
    set_form_vars()
    var('CONTENT', pagebar + a + pagebar )

def list_pagebar(pageno, numpages):
    ''' return the html for the pager line '''

    prevlink = '<span class="n">&lt;&lt;</span>'
    nextlink = '<span class="n">&gt;&gt;</span>'
    linkback = g['linkback']

    if pageno > 0:
        prevlink = '<a href="{}?pageno={}&prevpage=1">&lt;&lt;</a>'.format(linkback, pageno)
    if pageno < ( numpages - 1 ):
        nextlink = '<a href="{}?pageno={}&nextpage=1">&gt;&gt;</a>'.format(linkback, pageno)

    pagebar = ''
    for n in range(0, numpages):
        if n is pageno: pagebar += '<span class="n">{}</span>'.format(n + 1)
        else: pagebar += '<a href="{}?jumppage={}">{}</a>'.format(linkback, n, n + 1)

    var('prevlink', prevlink)
    var('nextlink', nextlink)
    var('pagebar', pagebar)
    p = getpage('nextprev')
    return p

def page(pagename, title = ''):
    ''' display a page from html template '''
    tl = g['tl']
    htmldir = g['config']['htmlDir']
    file_ext = g['template_ext']
    var('pageTitle', title)
    var('VERSION', g['VERSION'])
    set_stack_vars()
    for p in ( 'header', pagename, 'footer' ):
        try: 
            tl.file(os.path.join(htmldir, p + file_ext))
            for line in tl.readlines(): print(line, end='') # lines are already terminated
        except IOError as e:
            errorexit('Cannot open file ({})'.format(e))
    exit()

def getpage(p):
    ''' return a page as text from an html template '''
    tl = g['tl']
    htmldir = g['config']['htmlDir']
    file_ext = g['template_ext']
    a = ''
    try: 
        tl.file(os.path.join(htmldir, p + file_ext))
        for line in tl.readlines(): a += line # lines are already terminated
    except IOError as e:
        errorexit('Cannot open file ({})'.format(e))
    return(a)

### actions
def add():
    db = g['db']
    v = g['vars']
    cgi = g['cgi']

    rec = dict(
        testimonial = cgi.entity_encode(v.getfirst('testimonial')),
        byline = cgi.entity_encode(v.getfirst('byline'))
    )
    db.insert(rec)
    message('Record ({}) added'.format(rec['byline']))
    main_page()
def edit():
    id = g['vars'].getfirst('id')
    rec = g['db'].getrec(id)
    set_form_vars(**rec)
    hidden('a', 'update')
    hidden('id', id)
    page('edit', 'Edit this testimonial')

def delete_confirm():
    id = g['vars'].getfirst('id')
    rec = g['db'].getrec(id)
    set_form_vars(**rec)
    hidden('a', 'delete_do')
    hidden('id', id)
    hidden('byline', rec['byline'])
    page('delconfirm', 'Delete this testimonial?')

def delete_do():
    db = g['db']
    v = g['vars']

    id = v.getfirst('id')
    byline = v.getfirst('byline')
    db.delete(id)
    message('Record ({}) deleted'.format(byline))
    main_page()

def update():
    db = g['db']
    v = g['vars']
    cgi = g['cgi']

    id = v.getfirst('id')
    rec = dict(
        id = id,
        testimonial = cgi.entity_encode(v.getfirst('testimonial')),
        byline = cgi.entity_encode(v.getfirst('byline'))
    )
    db.update(id, rec)
    message('Record ({}) updated'.format(rec['byline']))
    main_page()

### manage template variables
def var(n, v = None):
    ''' shortcut for setting a variable '''
    return g['tl'].var(n, v)

def set_form_vars(**kwargs):
    t = kwargs.get('testimonial', '')
    b = kwargs.get('byline', '')
    id = kwargs.get('id', '')
    var('testimonial', t)
    var('byline', b)
    var('id', id)
    var('SELF', g['linkback'])

def stackmessage(stack, *list, **kwargs):
    sep = kwargs.get('sep', ' ')
    m = sep.join(str(i) for i in list)
    g['stacks'][stack].append(m)


def message(*list, **kwargs):
    stackmessage('messages', *list, **kwargs)

def error(*list, **kwargs):
    if 'cgi' in g:
        stackmessage('errors', *list, **kwargs)
    else:
        errorexit(' '.join(list))

def hidden(n, v):
    g['stacks']['hiddens'].append([n, v])

def set_stack_vars():
    a = ''
    for m in g['stacks']['messages']:
        a += '<p class="message">{}</p>\n'.format(m)
    var('MESSAGES', a)
    a = ''
    for m in g['stacks']['errors']:
        a += '<p class="error">{}</p>\n'.format(m)
    var('ERRORS', a)
    a = ''
    for m in g['stacks']['hiddens']:
        a += '<input type="hidden" name="{}" value="{}" />\n'.format(*m)
    var('hiddens', a)

### utilities
def errorexit(e):
    me = os.path.basename(sys.argv[0])
    print('<p style="color:red">')
    print('{}: {}'.format(me, e))
    print('</p>')
    exit(0)

def message_page(*list):
    message(*list)
    main_page()

def debug(*args):
    print(*args, file=sys.stderr)

if __name__ == "__main__": main()
