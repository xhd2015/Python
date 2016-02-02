from numpy import array, dtype, lexsort

particle_dtype = dtype([('mass','f4'), ('velocity', 'f4')])

# This must be a list of tuples.  numpy doesn't like a list of arrays
# or an tuple of tuples.
particles = array([(1,1),
                   (1,2),
                   (2,1),
                   (1,3)],dtype=particle_dtype)

# print particles
print 'Mass for all particles:', particles['mass']
print 'Particle 0:', particles[0]

print 'particles (mass, velocity)'
print particles

print 'sorted by mass then velocity:',
particles.sort()
print particles

print 'sorted by velocity then mass:',
particles.sort(order=('velocity','mass'))
print particles
