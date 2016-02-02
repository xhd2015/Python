results = []
f = open('rcs.txt','r') 

# skip first line
f.readline()

# read values and convert to float.
for line in f:
   all = [float(val) for val in line.split()]
   results.append(all)
f.close()

# print results
for i in results: 
    print i
