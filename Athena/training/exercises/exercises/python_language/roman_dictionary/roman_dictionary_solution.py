"""
Mark Antony keeps a list of the people he knows in several dictionaries 
based on their relationship to him::
    
    friends = {'julius': '100 via apian', 'cleopatra': '000 pyramid parkway'}
    romans = dict(brutus='234 via tratorium', cassius='111 aqueduct lane')
    countrymen = dict([('plebius','786 via bunius'), 
                       ('plebia', '786 via bunius')])


1. Print out the names for all of Antony's friends.
2. Now all of their addresses.
3. Now print them as "pairs".
4. Hmmm.  Something unfortunate befell Julius.  Remove him from the 
   friends list.
5. Antony needs to mail everyone for his second-triumvirate party.  Make
   a single dictionary containing everyone.
6. Antony's stopping over in Egypt and wants to swing by Cleopatra's 
   place while he is there. Get her address.
7. The barbarian hordes have invaded and destroyed all of Rome.
   Clear out everyone from the dictionary.
"""

friends = {'julius': '100 via apian', 'cleopatra': '000 pyramid parkway'}
romans = dict(brutus='234 via tratorium', cassius='111 aqueduct lane')
countrymen = dict([('plebius','786 via bunius'), ('plebia', '786 via bunius')])

# Print out the names for all of Antony's friends:
print 'friend names:', friends.keys()
print

# Now all of their addresses:
print 'friend addresses:', friends.values()
print

# Now print them as "pairs":
print 'friend (name, address) pairs:', friends.items()
print

# Hmmm.  Something unfortunate befell Julius.  Remove him from the friends 
# list:
del friends['julius']
 
# Antony needs to mail everyone for his second-triaumvirate party.  Make a 
# single dictionary containing everyone:
mailing_list = {}
mailing_list.update(friends)
mailing_list.update(romans)
mailing_list.update(countrymen)
   
print 'party mailing list:'
print mailing_list
print
   
# Or, using a loop (which we haven't learned about yet...):
print 'party mailing list:'
for name, address in mailing_list.items():
    print name, ':\t', address    
print

# Antony's stopping over in Egypt and wants to swing by Cleopatra's place 
# while he is there. Get her address:
print "Cleopatra's address:", friends['cleopatra']
   
# The barbarian hordes have invaded and destroyed all of Rome. Clear out 
# everyone from the dictionary:
mailing_list.clear() 
