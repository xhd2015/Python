
"""
Person Class
------------

1. Write a class that represents a person with first and last name that
can be initialized like so::

    p = Person('eric', 'jones')

Write a method that returns the person's full name.

Write a __repr__ method that prints out an official representation
of the person that would produce an identical object if evaluated::

    Person('eric', 'jones')

"""


class Person(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return '%s %s' % (self.first, self.last)

    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.first, self.last)

p = Person('eric', 'jones')
print p.full_name()
print p
