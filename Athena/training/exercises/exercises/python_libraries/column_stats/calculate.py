# If one argument is passed to the function, then this is the name of the
#   file to process and "{3} > 53.0" is the command
#
# If two arguments are passed to the function, then they are the file name
#   and the command to process.
#
# If no arguments are passed then this function reads from standard in
#   the filename and possibly the command to process. 
#
# The command to process is a calculation expression where the
#   column number is prvided in braces {}.
#
# Examples: 
#   echo "sp500hst_part.txt {3} > 53.0" | python calculate.py
#   echo "sp500hst_part.txt {6} > 50000" | python calculate.py
#   echo "sp500hst_part.txt" | python calculate.py
#   python calculate.py sp500hst_part.txt "{6}>50000"
#   python calculate.py sp500hst_part.txt

import sys
import numpy

if len(sys.argv) > 1:
    filename = sys.argv[1]
    if len(sys.argv) > 2:
        command = sys.argv[2]
    else:
        command = ''
else:
    data = sys.stdin.read()
    res = data.split()
    filename = res[0]
    command = ' '.join(res[1:]).strip()

if len(command) == 0:
    command = "{3} > 53.0"    

dtype = [('date', 'i4'),
         ('symbol', 'S4'),
         ('OPEN', 'f4'),
         ('HIGH', 'f4'),
         ('LOW', 'f4'),
         ('CLOSE', 'f4'),
         ('VOLUME', 'i4')]

# Open file and convert to array
array = numpy.loadtxt(filename, dtype=dtype, delimiter=',')

# Execute command on the specific column
start_col = command.find('{')
end_col = command.find('}',start_col)
column = int(command[start_col+1:end_col])
field_name = dtype[column][0]
res = array[field_name]
evstr = "res %s" % command[end_col+1:]
new = eval(evstr)
sys.stdout.write("%s\n" % new.sum())
sys.stdout.flush()
