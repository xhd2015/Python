
import numpy as np


def SIR(y, t, alpha, gamma):
    """
    This function implements the right-hand side of the SIR differential
    equations:
        dS/dt = -alpha * S * I
        dI/dt = alpha * S * I - gamma * I
        dR/dt = gamma * I
    """
    S, I, R = y

    f = np.zeros((3,), np.float)
    f[0] = -alpha * S * I
    f[1] = alpha * S * I - gamma * I
    f[2] = gamma * I

    return f


def SIR_jac(y, t, alpha, gamma):
    """
    The Jacobian of the SIR differential equations.
    """
    S, I, R = y

    # Create the Jacobian matrix, initialized with zeros.
    jac = np.zeros((3, 3), np.float)

    # Compute the nonzero entries of the Jacobian.
    jac[0, 0] = -alpha * I
    jac[0, 1] = -alpha * S
    jac[1, 0] = alpha * I
    jac[1, 1] = -gamma + alpha * S
    jac[2, 1] = gamma

    return jac


