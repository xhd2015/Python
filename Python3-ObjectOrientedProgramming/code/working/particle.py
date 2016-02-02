__author__ = 'Plamen'


class Particle(object):

    """ Initialize method
        Good practice to initialize class member attributes
    """
    def __init__(self, m, v):
        self.mass = m
        self.velocity = v

    # Method for calculating object momentum
    def momentum(self):
        return self.mass * self.velocity

    # A magic method defines object's string representation
    def __repr__(self):
        # return "Particle({0}, {1})".format(repr(self.mass), repr(self.velocity))
        return "(m:{0}, v:{1})".format(repr(self.mass),repr(self.velocity))

    # Overwrite class builtin __add__() => a + b
    def __add__(self, other):

        if not isinstance(other, Particle):
            return NotImplemented       # special singleton will ask "other" to do the call
        mnew = self.mass + other.mass
        vnew = (self.momentum() + other.momentum())/mnew
        return Particle(mnew, vnew)


def by_mass(x):
    return x.mass


def by_momentum(x):
    return x.momentum()


def by_kinetic_energy(x):
    return 0.5 * x.mass * x.velocity**2


def main():
    a = Particle(3.2, 4.1)
    print a.momentum()
    print a

if __name__ == "__main__":
    main()