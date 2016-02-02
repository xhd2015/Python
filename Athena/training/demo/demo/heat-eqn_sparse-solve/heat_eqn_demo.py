"""Solve for the steady state of the 1D heat equation with a nonhomogenous heat
source in the interior of the domain.

This module demonstrates the use of several features of numpy, scipy and pylab,
including the creation a sparse matrix and solving a sparse linear system.

"""

from numpy import linspace, concatenate
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve

from pylab import plot, show, title, legend, xlabel, grid, figure


def heat_source(x,length=1,gmax=1):
    """A parabolic 'bump' in the interval (length/4,length/2); zero elsewhere."""
    f = gmax*64.0*(x-0.25*length)*(0.5*length-x)/length**2
    g = f.clip(0.0,gmax+1)
    return g


# Length of the interval.
L = 8.0

# M is the number of interior points in the discretization.
M = 200

# Create the x discretization.  Add 2 to M to allow for the boundary points.
x = linspace(0,L,M+2)

# The interior x coordinates.
xint = x[1:-1]

# Nonhomogenous heat source.
gint = heat_source(xint,length=L,gmax=0.4)

# A is a second order centered difference operator. A is tridiagonal: -2 on the 
# diagonal, 1 on the first upper and lower off-diagonals, and zero elsewhere.
# We implement A as a sparse matrix.
A = spdiags([[1.]*M, [-2.]*M, [1.]*M], [-1, 0, 1], M, M, format='csr')

# Grid spacing
h = L/(M+1.)

# Heat coefficient
alpha2 = 0.55

# Create the 'right hand side' for the linear algebra problem to be solved.
b = -(h**2/alpha2)*gint

# Find the steady state; use the sparse solver spsolve from the
# scipy.linsolve module.
yint = spsolve(A,b)

# Extend yint with the zero boundary values.
y = concatenate(([0],yint,[0]))

figure()
plot(x,y,'b')
plot(xint,gint,'r--')
title('1D Heat Equation (Dirichlet BCs)')
legend(['Steady State','Heat Source'])
xlabel('x')
grid()
show()
