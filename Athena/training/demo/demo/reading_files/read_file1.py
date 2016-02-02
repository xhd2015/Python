results = [] 
f = open(r'rcs.txt','r')

# Read all the lines.
lines = f.readlines()
f.close()
# Discard the header.
lines = lines[1:]

for line in lines:
   # Split line into fields.
   fields = line.split()
   # Convert text to numbers.
   freq = float(fields[0])
   vv = float(fields[1])
   hh = float(fields[2])
   # Group & append to results.
   all = [freq,vv,hh]
   results.append(all)

for i in results:
    print i
