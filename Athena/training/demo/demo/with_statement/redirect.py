
# Necessary for Python 2.5; don't need this in Python >= 2.6.
from __future__ import with_statement

import sys


class redirect(object):
    """
    This class provides a context manager in which one or more of stdin,
    stdout and stderr are redirected.
    
    The values provided to the constructor with the keyword arguments 'stdin',
    'stdout' and 'stderr' must implement the appropriate file interface.

    Example
    -------
    >>> out = open('out.txt', 'w')
    >>> with redirect(stdout=out):
    ...     print "Hello, world!"
    ...     print 100, 200, 300
    ... 
    >>> out.close()
    >>> open('out.txt').read()
    'Hello, world!\n100 200 300\n'

    """

    def __init__(self, stdin=None, stdout=None, stderr=None):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        if self.stdin is not None:
            self.save_stdin = sys.stdin
            sys.stdin = self.stdin
        if self.stdout is not None:
            self.save_stdout = sys.stdout
            sys.stdout = self.stdout
        if self.stderr is not None:
            self.save_stderr = sys.stderr
            sys.stderr = self.stderr

    def __exit__(self, type, value, traceback):
        if self.stdin is not None:
            sys.stdin = self.save_stdin
        if self.stdout is not None:
            sys.stdout = self.save_stdout
        if self.stderr is not None:
            sys.stderr = self.save_stderr
