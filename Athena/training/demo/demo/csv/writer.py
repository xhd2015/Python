import csv

data = [("One", 1, 1.5), ("Two", 2, 8.0)]
f = open("out.csv", "w")
wrtr = csv.writer(f)
wrtr.writerows(data)
f.close()
