"""
Print out only words that start with "o", ignoring case::
    
    lyrics = '''My Bonnie lies over the ocean.
                My Bonnie lies over the sea.
                My Bonnie lies over the ocean.
                Oh bring back my Bonnie to me.
                '''

Bonus points: print out words only once.
"""

lyrics = """My Bonnie lies over the ocean.
            My Bonnie lies over the sea.
            My Bonnie lies over the ocean.
            Oh bring back my Bonnie to me.
         """

# Ignore case:
lyrics = lyrics.lower()

# Get rid of periods:
lyrics = lyrics.replace('.'," ")

# Split into a list of words:
words = lyrics.split()

# Make a list to fill with 'o' words:
o_words = []

for word in words:
    if word[0] == "o":
        o_words.append(word)
        
print "words that start with 'o':"
print o_words

# Converting the list to a set removes all non-unique entries:
print "unique words that start with 'o':"
print set(o_words)

