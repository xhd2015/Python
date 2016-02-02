#!/usr/bin/env python3.3

# Build Script
# -------------------

# ..  sectnum::
#
# ..  contents::
#

# Design
# ===============

# This is a tool somewhat like ant or scons which will track dependencies
# among files and rebuild dependent files when the sources have
# changed.

# We have to model two kinds of dependencies.
#
# -   A generic ``*.txt`` on ``*.py``, as well as ``*.html`` on ``*.txt``.
#
# -   A specific index.rst on ``[*.py]``.
#
# The distinction here is that a generic rule is a template
# that applies to a number of files in a kind of 1-1 relationship.
#
# The specific rule is a slightly more general 1-m target-source relationship.
#
# We'll define a function to build if necessary. This will be a higher-order
# function which requires a builder which can rebuild the target if
# any of the sources have been changed.
#
# We'll define a number of builders for the various tools we need to automate.

# Module Overheads
# =================

# Module Docstring
# ::

"""Build all the code sample files into slightly more readable HTML pages.

1. Run pylit to build the RST *.txt files from the code in *.py files.
2. Create the index.rst page as an additional file.
3. Run rst2html.py to build the *.html versions of the *.txt files.

Requires pylit and docutils.
"""

# Our includes
# ::

import os
import glob
import subprocess
import datetime
import sys
import logging
from functools import partial

# Some Logging Setup
# ==================

# We'll define a decorator to create function-specific loggers.
# This will provide an extra keyword argument with a named logger.
# It slightly simplifies the function because we don't have
# to create the logger, we can just assume it will be provided
# as an argument.

# ::

from functools import wraps
def logged(some_function):
    @wraps(some_function)
    def decorated(*args, **kw):
        logger= logging.getLogger(some_function.__name__)
        return some_function(*args, logger=logger, **kw)
    return decorated

# When we put the ``@logged`` decorator on a function, then
# a ``logger=`` keyword parameter is set with a
# properly named named logger.

# Here's the logging setup done as context management.
# We'll initialized logging and shutdown logging, also.

# ::

class Logging_Config:
    def __enter__( self, filename="logging.config" ):
        logging.basicConfig( stream=sys.stderr, level=logging.INFO )
    def __exit__( self, *exc ):
        logging.shutdown()

# The Core Functions
# ===================

# The core feature is a ``build_if_needed()`` function. This will
# check the modification times of the named files. This function
# has a simple body:
#
# -  If the target is newer than the source, do nothing.
#
# -  If the target is older than the source, apply the builder function.
#
# In order to determine if we should build, we need to compare
# the modification times of the target and all of the sources.

# ::

@logged
def target_ok( target_file, *source_list, logger=logging ):
    """Was the target file created after all the source files?
    If so, this is OK.
    If there's no target, or the target is out-of-date,
    it's not OK.
    """
    try:
        mtime_target= datetime.datetime.fromtimestamp(
            os.path.getmtime( target_file ) )
    except Exception:
        logger.debug( "File {0} not found".format(target_file) )
        return False

    logger.debug( "Compare {0} {1} >ALL {2}".format(
            target_file, mtime_target,
            source_list ) )

    # If a source doesn't exist, we have bigger problems.
    times = (datetime.datetime.fromtimestamp(
            os.path.getmtime( source ) ) for source in source_list)

    return all(mtime_target > mtime_source for mtime_source in times)

# The ``build_if_needed()`` function requires a builder, a target and
# one or more sources. It will apply the ``target_ok()`` function
# to the target and source files. If necessary, it will apply
# the builder.

# ::

@logged
def build_if_needed( builder, target_file, *source, logger=logging ):
    logger.info( "Checking {0}".format(target_file) )
    if target_ok( target_file, *source ):
        return "ok({0},...)".format(target_file)
    builder( target_file, *source )
    return "{0}({1},...)".format(builder.__class__.__name__,target_file)

# We could approach this a different way. We could have
# had the build_if_needed() return one of two things:
#
# - builder(target,*source) for evaluation later.
#
# - ok(target,*source) which is a stub builder that doesn't do anything.
#
# The idea would be that the output from the above would be
# a script that clearly shows what needs to be done.

# The Builders
# =============

# Each builder is a function which takes the target filename
# and a list of source filenames. It's job is to create the target
# from the sources.
#
# Since we rely on the ``subprocess.check_call()`` function, each
# builder is properly a composition of the ``check_call()`` and
# another function that builds the command which is called.
#
# We'll have several ways to implement the functional composition:
# via subclass definition, decorators, or a higher-order function
# that combines the two other functions.
#
# We'll opt for a generic higher-order function and create a partial
# when we bind in the function that builds the arguments.

# ::

@logged
def subprocess_builder( make_command, target_file, *source_list, logger=logging ):
    command= make_command( target_file, *source_list )
    logger.debug( "Command {0}".format(command) )
    subprocess.check_call( command )

# The PyLit subprocess_builder creates a command to run PyLit.

# ::

def command_pylit( output, *input ):
        return ["python3", "-m", "pylit", input[0]]

pylit= partial( subprocess_builder, command_pylit )

# The rst2html subprocess_builder creates a command to run rst2html.
# It includes two common arguments required to make acceptable-looking
# content.

# ::

def command_rst2html( output, *input ):
        return ["rst2html.py", "--syntax-highlight=long", "--input-encoding=utf-8", input[0], output]

rst2html= partial( subprocess_builder, command_rst2html )

# A builder to create an index page. This will apply three internal functions
# to create a header, create the body, and create a footer.
# ::

header= lambda : """
#############################################
Function Python Programming Bonus Code
#############################################

© 2014, Steven F. Lott

..  raw:: html

    <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>
    <br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Some Bonus Material.
"""

footer = lambda : "Updated {0}".format(datetime.datetime.now())

def body( source_list ):
    return "\n".join(
        "-   `{0} <{0}>`_".format(ext_to( name, ".html" ))
        for name in source_list)

def make_index( target_file, *source_list ):
    with open(target_file,"w") as target:
        print( header(), file=target )
        print( file=target )
        print( body(source_list), file=target )
        print( file=target )
        print( footer(), file=target )

# File Name Transformations
# ==========================

# When we think about a generic rule, we're usually talking about
# simple rewrite from a filename to a filename with a different
# extension. We have two filename extension rewriters.

# The ``ext_to()`` function changes the extension on a filename.

# ::

def ext_to( filename, new_ext ):
    """Switch .ext"""
    name, ext = os.path.splitext( filename )
    return name + new_ext

# The ``ext_add()`` function appends an additional extension to
# a filename.

# ::

def ext_add( filename, add_ext ):
    """Add .ext"""
    return filename + add_ext

# We can these functions to transform names so that a generic
# rule can apply to many similarly-named files.

# Main Script
# ===========================

# Here's the top-level definition of the dependencies.
# There are three sets of rules.
#
# -  ``.txt`` based on ``.py`` files for files in ``\.py``.
#
# -  ``index.txt`` based on ``.txt`` files built from names in ``*.py``.
#
# -  ``*.html`` based on ``.txt`` files for files in ``*.txt``
#
# We've stated the rules two ways below. One has a list of
# dependency function values. The other as a **for** loop.
# Both versions seem reasonably clear.

# ::

def make_files():
    files_py = glob.glob( "*.py" )
    [build_if_needed( pylit, ext_add(f,'.txt'), f )
        for f in files_py]

    build_if_needed( make_index, "index.txt",
                    *[ext_add(f,'.txt') for f in files_py] )

    files_txt = glob.glob( "*.txt" )
    for f in files_txt:
        build_if_needed( rst2html, ext_to(f,'.html'), f )

# The Main script that does all the work.
# We create a logging context. We apply the build-if-needed rules.

# ::

if __name__ == "__main__":
    with Logging_Config():
        os.chdir("Bonus")
        make_files()
