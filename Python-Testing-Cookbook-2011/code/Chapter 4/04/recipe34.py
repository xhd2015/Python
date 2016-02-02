import getopt
import logging
import nose
import os
import os.path
import re
import sys
import lettuce
import doctest
from glob import glob

def usage():
    print
    print "Usage: python recipe34.py [command]"
    print
    print "\t--help"
    print "\t--test"
    print "\t--package"
    print "\t--publish"
    print "\t--register"
    print

try:
    optlist, args = getopt.getopt(sys.argv[1:],
            "h",
           ["help", "test", "package", "publish", "register"])
except getopt.GetoptError:
    # print help information and exit:
    print "Invalid command found in %s" % sys.argv
    usage()
    sys.exit(2)

def test_with_bdd():
    from recipe26_plugin import BddPrinter

    suite = ["recipe26", "recipe30", "recipe31"]
    print("Running suite %s" % suite)
    args = [""]
    args.extend(suite)
    args.extend(["--with-bdd"])
    nose.run(argv=args, plugins=[BddPrinter()])

def test_plain_old_doctest():
    for extension in ["doctest", "txt"]:
        for doc in glob("recipe27*.%s" % extension):
            print("Testing %s" % doc)
            doctest.testfile(doc)

def test_customized_doctests():
    from recipe28 import BddDocTestRunner

    old_doctest_runner = doctest.DocTestRunner
    doctest.DocTestRunner = BddDocTestRunner

    for recipe in ["recipe28", "recipe29"]:
        for file in glob("%s*.doctest" % recipe):
            given = file[len("%s_" % recipe):]
            given = given[:-len(".doctest")]
            given = " ".join(given.split("_"))
            print("===================================")
            print("%s: Given a %s..." % (recipe, given))
            print( "===================================")
            doctest.testfile(file)
            print

    doctest.DocTestRunner = old_doctest_runner

def test_lettuce_scenarios():
    print("Running suite recipe32")
    lettuce.Runner(os.path.abspath("recipe32"), verbosity=3).run()
    print

    print("Running suite recipe33")
    lettuce.Runner(os.path.abspath("recipe33"), verbosity=3).run()
    print

def test():
    test_with_bdd()
    test_plain_old_doctest()
    test_customized_doctests()
    test_lettuce_scenarios()

def package():
    print "This is where we can plug in code to run " + \
          "setup.py to generate a bundle."

def publish():
    print "This is where we can plug in code to upload " + \
          "our tarball to S3 or some other download site."

def register():
    print "setup.py has a built in function to " + \
          "'register' a release to PyPI. It's " + \
          "convenient to put a hook in here."
    # os.system("%s setup.py register" % sys.executable)

if len(optlist) == 0:
    usage()
    sys.exit(1)

# Check for help requests, which cause all other 
# options to be ignored. 
for option in optlist:
    if option[0] in ("--help", "-h"):
        usage()
        sys.exit(1)


# Parse the arguments, in order
for option in optlist:
    if option[0] in ("--test"):
        test()

    if option[0] in ("--package"):
        package()
	
    if option[0] in ("--publish"):
        publish()

    if option[0] in ("--register"):
        register()


