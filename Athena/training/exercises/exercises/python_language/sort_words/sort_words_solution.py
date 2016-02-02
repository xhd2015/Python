"""
Given a (partial) sentence from a speech, print out
a list of the words in the sentence in alphabetical order.
Also print out just the first two words and the last
two words in the sorted list.

::

    speech = '''Four score and seven years ago our fathers brought forth 
             on this continent a new nation, conceived in Liberty, and 
             dedicated to the proposition that all men are created equal.
             '''


Ignore case and punctuation.
"""

speech = '''Four score and seven years ago our fathers brought forth 
      on this continent a new nation, conceived in Liberty, and 
      dedicated to the proposition that all men are created equal.
      '''
         
# Convert to lower case so that case is ignored in sorting:
speech = speech.lower()

# Replace punctuation with spaces 
# (you could just remove them as well):
speech = speech.replace(",", " ")
speech = speech.replace(".", " ")

# Split the words into a list:
words = speech.split()

# Sort the words "in place":
words.sort()

print "All words, in alphabetical order:"
print words
print
print "The first 2 words: "
print words[:2]
print
print "The last 2 words: "
print words[-2:]     
