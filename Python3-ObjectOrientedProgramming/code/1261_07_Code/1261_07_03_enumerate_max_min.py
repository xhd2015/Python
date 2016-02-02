def min_max_indexes(seq):
    minimum = min(enumerate(seq), key=lambda s: s[1])
    maximum = max(enumerate(seq), key=lambda s: s[1])
    return minimum[0], maximum[0]


ll = [5,0,1,4,6,3]
print(ll)
print(min_max_indexes(ll))
print(ll[1], ll[4])