"""
This version is about 35% faster than the original on largish files
because it reads in all the data at once and then uses array slicing 
to assign the data elements to the correct column (or log).
"""

log_file = open('long_logs.crv')

# The first line is a header that has all the log names:
header = log_file.readline()
log_names = header.split()
log_count = len(log_names)

# Everything left is data.
# Now, read in all of the data in one fell swoop, translating
# it into floating point values as we go:
value_text = log_file.read()
values = [float(val) for val in value_text.split()]

# Once this is done, we can go back through and split the "columns" out 
# of the values and associating them with their log names.  This can be
# done efficiently using strided slicing. The starting position for 
# each log is just its column number, and, the "stride" for the slice
# is the number of logs in the file:
logs = {}
for offset, log_name in enumerate(log_names):
    logs[log_name] = values[offset::log_count]    
    
