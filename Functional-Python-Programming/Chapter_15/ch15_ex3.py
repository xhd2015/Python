#!/usr/bin/env python3
"""Functional Python Programming

Chapter 15, Example Set 3
"""

from wsgiref.simple_server import make_server, demo_app
import wsgiref.util
import urllib
import datetime
import os
import sys
import glob

def test_app(environ, start_response):
    if environ['REQUEST_METHOD'] == "GET":
        # send form and previous results (if any)
        if environ['QUERY_STRING']:
            query= urllib.parse.parse_qs(environ['QUERY_STRING'])
            filename= query['filename'][0]
            with open(environ['TMPDIR']+filename) as results:
                results= results.read()
        else:
            results= ""
        page="""<html>
<head><title>Run Tests</title></head>
<body>
<h1>Tests</h1>
<p>Results</p>
<pre><code>{0}
</code></pre>
<form method="POST" action="">
<hr/>
<input type="submit" value="Run Tests"/>
</form>
</body>
</html>""".format( results )
        content= page.encode("utf-8")
        headers= [
            ("Content-Type",'text/html; charset="utf-8"'),
            ("Content-Length",str(len(content))),
            ]
        start_response('200 OK', headers)
        return [ content ]
    elif environ['REQUEST_METHOD'] == "POST":
        # Run tests, collect data in a cache file
        import test_all
        with open(environ['TMPDIR']+"results","w") as results:
            sys.stderr= results
            content= sorted( glob.glob("Chapter_*"), key=test_all.chap_key )
            test_all.master_test_suite( test_all.package_module_iter(*content) )
            sys.stderr= sys.__stderr__
        # Might want to compute a distinct filename
        filename= {"filename":"results"}
        encoded_filename= urllib.parse.urlencode(filename)
        headers= [
            ("Location", "/test?{0}".format(encoded_filename) )
        ]
        start_response( "302 FOUND", headers )
        return []

CONTENT_HOME = "/Users/slott/Documents/Writing/Functional Python Progamming/Code"

def index_app(environ, start_response):
    log= environ['wsgi.errors']
    print("PATH_INFO '{0}'".format(environ['PATH_INFO']), file=log )
    page= """<html>
<head><title>Chapter 15</title></head>
<body><h1>Files in {0}</h1>
    """.format(environ['PATH_INFO'])
    for name in os.listdir(CONTENT_HOME+environ['PATH_INFO']):
        if name.startswith('.'): continue
        path= environ['PATH_INFO']+"/"+name
        page += '<p><a href="/static{0}">{1}</a></p>'.format(path, name)
    page += "</body></html>"
    content= page.encode("utf-8")
    headers= [
        ("Content-Type",'text/html; charset="utf-8"'),
        ("Content-Length",str(len(content))),
        ]
    start_response('200 OK', headers)
    return [ content ]

def static_app(environ, start_response):
    try:
        with open(CONTENT_HOME+environ['PATH_INFO']) as static:
            content= static.read().encode("utf-8")
            headers= [
                ("Content-Type",'text/plain; charset="utf-8"'),
                ("Content-Length",str(len(content))),
                ]
            start_response('200 OK', headers)
            return [ content ]
    except IsADirectoryError as e:
        return index_app(environ, start_response)
    except FileNotFoundError as e:
        start_response('404 NOT FOUND', [])
        return( [repr(e).encode("utf-8")] )

def welcome_app(environ, start_response):
    page = """<html>
<head><title>Chapter 15</title></head>
<body><h1>Chapter 15</h1>
<p><a href="demo">The WSGI Demo App</a></p>
<p><a href="static">All Code</a></p>
<p><a href="test">Run Test Suite</a></p>
<p><a href="static/Chapter_15/ch15_ex3.py">This Code</a></p>
</body>
</html>"""
    content= page.encode("utf-8")
    headers= [
        ("Content-Type","text/html; charset=utf-8"),
        ("Content-Length",str(len(content))),
    ]
    start_response( '200 OK', headers )
    return [content]

SCRIPT_MAP = {
    "demo": demo_app,
    "static": static_app,
    "test": test_app,
    "": welcome_app,
}
def routing(environ, start_response):
    top_level= wsgiref.util.shift_path_info(environ)
    app= SCRIPT_MAP.get(top_level, SCRIPT_MAP[''])
    content= app(environ, start_response)
    return content

def server_demo():
    httpd = make_server('', 8080, routing)
    print("Serving HTTP on port 8080...")

    # Respond to requests until process is killed
    httpd.serve_forever()

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
    #server_demo()