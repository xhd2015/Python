import doctest

class BddDocTestRunner(doctest.DocTestRunner):
    """
    This is a customized test runner. It is meant
    to run code examples like DocTestRunner, 
    but if a line preceeds the code example 
    starting with '#', then it prints that 
    comment.

    If the line starts with '#when', it is printed
    out like a sentence, but with no outcome.

    If the line starts with '#', but not '#when'
    it is printed out indented, and with the 
    outcome.
    """

    def report_start(self, out, test, example):
        prior_line = example.lineno-1
        line_before = test.docstring.splitlines()[prior_line]
        if line_before.startswith("#"):
            message = line_before[1:]
            if line_before.startswith("#when"):
                out("* %s\n" % message)
                example.silent = True
                example.indent = False
            else:
                out("  - %s: " % message)
                example.silent = False
                example.indent = True
        else:
            example.silent = True
            example.indent = False
        doctest.DocTestRunner(out, test, example)

    def report_success(self, out, test, example, got):
        if not example.silent:
            out("ok\n")
        if self._verbose: 
            if example.indent: out("    ")
            out(">>> %s\n" % example.source[:-1])

    def report_failure(self, out, test, example, got):
        if not example.silent:
            out("FAIL\n")
        if self._verbose:
            if example.indent: out("    ")
            out(">>> %s\n" % example.source[:-1])

if __name__ == "__main__":
    from glob import glob
 
    doctest.DocTestRunner = BddDocTestRunner

    for file in glob("recipe29*.doctest"):
        given = file[len("recipe29_"):]
        given = given[:-len(".doctest")]
        given = " ".join(given.split("_"))
        print "==================================="
        print "Given a %s..." % given
        print "==================================="
        doctest.testfile(file)
