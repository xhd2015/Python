
"""

You have the string below, which is a set of "yes/no" votes,
where "y" or "Y" means yes and "n" or "N" means no. Determine 
the percentages of yes and no votes.

::

    votes = "y y n N Y Y n n N y Y n Y"
"""

votes = "y y n N Y Y n n N y Y n Y"

# Force everything to lower case:
votes = votes.lower()

# Now count the yes votes:
yes = votes.count("y")
no = votes.count("n")

total = yes + no

# Notice cast to float! Otherwise you have an integer division.

print "vote outcome:"
print "% yes:", yes/float(total) * 100
print "% no:", no/float(total) * 100

# Alternative approach using future behavior of integer
# division yielding floats.

#from __future__ import division

#print "% yes:", yes/total * 100
#print "% no:", no/total * 100
