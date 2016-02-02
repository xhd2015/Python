"""
Sort Words
----------

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

See :ref:`sort-words-solution`.
"""

def main():
    speech = '''Four score and seven years ago our fathers brought forth
             on this continent a new nation, conceived in Liberty, and
             dedicated to the proposition that all men are created equal.
             '''
    l = sorted(speech.lower().replace(',','').replace('.','').split())

    print l
    print l[:2]
    print l[-2:]

if __name__ == "__main__":
    main()
                 

