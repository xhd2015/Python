import csv

rdr = csv.reader(open("data.csv"))
for row in rdr:
    print row
