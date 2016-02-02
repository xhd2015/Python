from numpy import array, dtype, lexsort

person_dtype = dtype([('first','S10'), ('last', 'S10'), ('age', 'i4')])

# This must be a list of tuples.  numpy doesn't like a list of arrays
# or an tuple of tuples.
people = array([('sam', 'smith', 39, ),
                ('jan', 'smith', 31),
                ('sue', 'jones', 35),
                ('tom', 'jones', 29)],dtype=person_dtype)

# do some data base like queries.
print 'all people'
print people
print
print 'people over 30'
print people[people['age']>30]                
print
print 'people over 30 named "smith"'
print people[ (people['age']>30) & (people['last']=='smith') ]

print 'people sorted by last name then first name:'
people.sort(order=['last','first'])
print people
