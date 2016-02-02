"""An example that uses the argparse module to handle command line arguments.

This example sets up the argument "--db filename", with a default filename
of "test.db", and the argument "--more", a boolean flag with the default
value False.

The ArgumentParser class will also automatically add the options "-h" and
"--help".  When given, a message about the program and its command line
arguments is printed to the console.

Try running the example with several variations:

python argparse_example.py
python argparse_example.py --help
python argparse_example.py --db myfile.db
python argparse_example.py --db another.db --more
python argparse_example.py --db    # (Missing argument!)

"""

import argparse

default_db = "test.db"

# Create an ArgumentParser.
parser = argparse.ArgumentParser(description="An example that uses the argparse module.")

# Add the --db and --more arguments to the parser.
parser.add_argument('--db', help='Database filename; default is "%s"' % default_db, default=default_db)
parser.add_argument('--more', help='Do something more.', action="store_true")

# Tell the parser to parse the command line arguments.  The results are
# assigned to attributes of the object returned by parse_args().
args = parser.parse_args()

print "args.db =", args.db
print "args.more =", args.more
