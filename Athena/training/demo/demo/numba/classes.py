from numba import double, jit, void


class Particle(object):
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

    def energy(self):
        return 0.5 * self.mass * self.velocity ** 2.0


@jit
class JitParticle(object):
    @void(double, double)
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

    @double()
    def energy(self):
        return 0.5 * self.mass * self.velocity ** 2.0
