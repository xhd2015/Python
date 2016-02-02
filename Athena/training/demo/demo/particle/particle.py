""" This example demonstrates creating a class and using
    custom sorting algorithms to sort list of these items.

    We create a Particle class and then sort a list of particles
    based on mass, velocity, and momentum.
"""


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
        This determines how the Particle object will appear in the
        interpreter read-eval-print loop (REPL).
        """
        return "Particle(mass={0!r}, velocity={0!r})".format( self.mass, self.velocity )

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


# Sorting methods
def by_mass(x, y):
    return cmp(x.mass, y.mass)


def by_velocity(x, y):
    return cmp(x.velocity, y.velocity)


def by_momentum(x, y):
    return cmp(x.momentum(), y.momentum())


def example():
    """ Sort particles in a list by their various properties.
    """
    particles = [Particle(1.2, 3.4), Particle(2.1, 2.3), Particle(4.6, .7)]
    print "Particles:", particles

    particles.sort(by_mass)
    print "sorted by mass:", particles
    particles.sort(by_velocity)
    print "sorted by velocity:", particles
    particles.sort(by_momentum)
    print "sorted by momentum:", particles


if __name__ == "__main__":
    example()
