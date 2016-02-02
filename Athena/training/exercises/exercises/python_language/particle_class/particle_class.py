"""
Particle Class
--------------

This is a quick exercise to practice working with a class.
The Particle class has already been defined.  In this exercise,
your task is to make a few simple changes to the class.

1. Change the __repr__() method so that the output includes
   the 'mass' and 'velocity' argument names.  That is, the
   output should have the form "Particle(mass=2.3, velocity=0.1)"
   instead of "Particle(2.3, 0.1)".

2. Add an energy() method, where the energy is given
   by the formula m*v**2/2.

3. Convert energy, mass, velocity to property

See :ref:`particle-class-solution`.
"""

# Here is the Particle class.  Edit this to complete
# the exercise.


class Particle(object):
    """ Simple particle with mass and velocity attributes.
    """

    def __init__(self, mass, velocity):
        """ Constructor method.
        """

        self.mass = mass
        self.velocity = velocity

    def momentum(self):
        """ Calculate the momentum of a particle (mass*velocity).
        """
        return self.mass * self.velocity

    def __repr__(self):
        """ A "magic" method defines object's string representation.
        """
        return "Particle({0!r}, {1!r})".format(self.mass, self.velocity)

    def __add__(self, other):
        """ A "magic" method to overload the '+' operator by
        adding the masses and determining the velocity to conserve
        momentum.
        """
        if not isinstance(other, Particle):
            return NotImplemented
        mnew = self.mass + other.mass
        vnew = (self.momentum() + other.momentum()) / mnew
        return Particle(mnew, vnew)

if __name__ == "__main__":
    p = Particle(2.0, 13.0)
    print p
    # The following won't work until you add the energy() method.
    print "Energy is", p.energy()
