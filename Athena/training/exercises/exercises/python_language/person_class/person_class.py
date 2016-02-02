
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

Bonus:
~~~~~~
2. Extend this class in such as way that the code about Homer in the slides
on OOP works: for that create the methods eat, take_nap, speak.

See :ref:`person-class-solution`.
"""

class Human(object):

    def eat(self, food):
        raise NotImplementedError

    def take_nap(self):
        raise NotImplementedError

    def speak(self, word):
        raise NotImplementedError

class Person(Human):
    # put your code here.
    def __init__(self, first_name, second_name):
        self._first_name = first_name
        self._second_name = second_name

    def __get_first_name(self):
        return self._first_name

    def __set_first_name(self, first_name):
        self._first_name = first_name

    def __get_last_name(self):
        return self._second_name

    def __set_last_name(self, second_name):
        self._second_name = second_name

    def __full_name(self):
        fullname = ' '
        return fullname.join([str(self._first_name).capitalize(),str(self._second_name).capitalize()])

    def __repr__(self):
        string = "{}('{}','{}')".format(self.__class__.__name__,str(self._first_name).capitalize(),str(self._second_name).capitalize())
        return string

    def eat(self,food):
        print '{} eats {}'.format(str(self._first_name).capitalize(), food)

    def take_nap(self):
        print '{} takes nap'.format(str(self._first_name).capitalize())

    def speak(self, word):
        print '{} says {}'.format(str(self._first_name).capitalize(),word)

    #interface
    fullname = property(__full_name,None)
    firstname = property(__get_first_name,__set_first_name)
    lastname = property(__get_last_name, __set_last_name)

p = Person('eric', 'jones')
print p.fullname
print p
p.eat('donut')
p.take_nap()
p.speak('Hello World')