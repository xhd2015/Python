import sys
err = sys.stderr

import nose
import re
from nose.plugins import Plugin

class BddPrinter(Plugin):
    name = "bdd"

    def __init__(self):
        Plugin.__init__(self)
        self.current_module = None

    def beforeTest(self, test):
        test_name = test.address()[-1]
        module, test_method = test_name.split(".")
        if self.current_module != module:
            self.current_module = module
            fmt_mod = re.sub(r"([A-Z])([a-z]+)", \
                             r"\1\2 ", module)
            err.write("\nGiven a %s" % fmt_mod[:-1].lower())
        message = test_method[len("test"):]
        message = " ".join(message.split("_"))
        err.write("\n- %s" % message)

    def addSuccess(self, *args, **kwargs):
        test = args[0]
        err.write(" : Ok")

    def addError(self, *args, **kwargs):
        test, error = args[0], args[1]
        err.write(" : ERROR!\n")

    def addFailure(self, *args, **kwargs):
        test, error = args[0], args[1]
        err.write(" : Failure!\n")
