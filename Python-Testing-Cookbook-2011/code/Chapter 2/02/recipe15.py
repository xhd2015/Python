import getopt
import glob
import logging
import nose
import os
import os.path
import pydoc
import re
import sys

def usage():
    print
    print "Usage: python recipe15.py [command]"
    print
    print "\t--help"
    print "\t--test"
    print "\t--suite [suite]"
    print "\t--debug-level [info|debug]"
    print "\t--package"
    print "\t--publish"
    print "\t--register"
    print "\t--pydoc"
    print

try:
    optlist, args = getopt.getopt(sys.argv[1:],
            "ht",
           ["help", "test", "suite=", \
            "debug-level=", "package", \
            "publish", "register", "pydoc"])
except getopt.GetoptError:
    # print help information and exit:
    print "Invalid command found in %s" % sys.argv
    usage()
    sys.exit(2)

def test(test_suite, debug_level):
    logger = logging.getLogger("recipe15")
    loggingLevel = debug_level
    logger.setLevel(loggingLevel)
    ch = logging.StreamHandler()
    ch.setLevel(loggingLevel)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    nose.run(argv=["", test_suite, "--verbosity=2"])
    
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

def create_pydocs():
    print "It's useful to use pydoc to generate docs."
    pydoc_dir = "pydoc"
    module = "recipe15_all"
    __import__(module)

    if not os.path.exists(pydoc_dir):
        os.mkdir(pydoc_dir)
 
    cur = os.getcwd()
    os.chdir(pydoc_dir)
    pydoc.writedoc("recipe15_all")
    os.chdir(cur)

debug_levels = {"info":logging.INFO, "debug":logging.DEBUG}
# Default debug level is INFO
debug_level = debug_levels["info"]  

for option in optlist:
    if option[0] in ("--debug-level"):
        # Override with a user-supplied debug level
        debug_level = debug_levels[option[1]] 

# Check for help requests, which cause all other 
# options to be ignored. 
for option in optlist:
    if option[0] in ("--help", "-h"):
        usage()
        sys.exit(1)
        
# Parse the arguments, in order
for option in optlist:
    if option[0] in ("--test"):
        print "Running recipe15_checkin tests..."
        test("recipe15_checkin", debug_level)

    if option[0] in ("--suite"):
        print "Running test suite %s..." % option[1]
        test(option[1], debug_level)

    if option[0] in ("--package"):
        package()
	
    if option[0] in ("--publish"):
        publish()

    if option[0] in ("--register"):
        register()

    if option[0] in ("--pydoc"):
        create_pydocs()
    

