print [[float(val) for val in l.split()] for l in open("rcs.txt","r") if l[0] !="#"]

