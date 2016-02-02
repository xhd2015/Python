
from numpy import zeros, linspace
from scipy.integrate import odeint
from pylab import figure, show, xlabel, ylabel
# The following import is necessary to enable 3D plots in matplotlib.
from mpl_toolkits.mplot3d import Axes3D


def lorenz_sys(q, t ,sigma, rho, beta):

    x = q[0]
    y = q[1]
    z = q[2]

    f = zeros((3,))
    f[0] = sigma * (y - x)
    f[1] = -y - z*x + x*rho
    f[2] = -beta*z + y*x

    return f


def lorenz_jac(q, t, sigma, rho, beta):

    x = q[0]
    y = q[1]
    z = q[2]

    jac = zeros((3,3))
    jac[0,0] = -sigma
    jac[0,1] = sigma
    jac[1,0] = -z + rho
    jac[1,1] = -1.0
    jac[1,2] = -x
    jac[2,0] = y
    jac[2,1] = x
    jac[2,2] = -beta
    return jac


def main():
    ic = [1.0, 2.0, 1.0]
    t = linspace(0, 50, 5000)
    sigma = 10.0
    rho = 28.0
    beta = 10.0/3
    sol = odeint(lorenz_sys, ic, t, args=(sigma, rho, beta), Dfun=lorenz_jac)

    fig = figure()
    ax = fig.gca(projection='3d')
    print type(ax)
    ax.plot(sol[:,0], sol[:,1], sol[:,2])
    xlabel('x')
    ylabel('y')
    show()


if __name__ == "__main__":
    main()
