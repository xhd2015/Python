import numpy
import matplotlib.pyplot

# http://en.wikipedia.org/wiki/Seashell_surface

u = numpy.linspace(0, 2 * numpy.pi, 30)
v = numpy.linspace(-2 * numpy.pi, 2 * numpy.pi, 30)

first_term = (5./4) * (1 - v/(2 * numpy.pi))
second_term = (1 + numpy.cos(u))
x = first_term * numpy.cos(2 * v) * second_term + numpy.cos(2 * v)
y = first_term * numpy.sin(2 * v) * second_term + numpy.sin(2 * v)
z = 5 * v / numpy.pi + first_term * numpy.sin(u) + 15

fig = matplotlib.pyplot.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(x, y, z)

matplotlib.pyplot.show()
