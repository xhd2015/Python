"""
Vote String
-----------
You have the string below, which is a set of "yes/no" votes,
where "y" or "Y" means yes and "n" or "N" means no. Determine 
the percentages of yes and no votes.

::

    votes = "y y n N Y Y n n N y Y n Y"

See :ref:`vote-string-solution`.
"""
# Begin exercise

def main():
    votes = "y y n N Y Y n n N y Y n Y"
    l = votes.lower().split()
    s = set(l)
    d = {}
    for x in s:
        d[x] = round(((l.count(x))*100.0/len(l)),2)
    print d

if __name__ == "__main__":
    main()