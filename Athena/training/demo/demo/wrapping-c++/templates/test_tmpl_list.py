from tmpl_list import List

N = 10
# Python list of List instances, one for each datatype.
lists = [List(N, tp) for tp in 'ilfd']

for l in lists:
    for i in range(N):
        l.append(i)

print "   {:>4s}{:>4s}{:>4s}{:>4s}".format(*'ilfd')
for i in range(N):
    print "{:2d}:{:4d}{:4d}{:4.1f}{:4.1f}".format(i, *[l.get(i) for l in lists])
