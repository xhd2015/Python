import sys
inname, outname = sys.argv[1:3]

with open(inname) as infile:
    with open(outname, 'w') as outfile:
        warnings = (l.replace('\tWARNING', '') for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)

with open(outname, 'r') as file:
    for line in file:
        print(" {0}".format(line), end = " ")