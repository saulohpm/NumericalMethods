import numpy as np

def calculate(F, x, h):
    """
    Compute the Jacobian matrix using forward finite differences.

    Parameters
    ----------
    F : callable
        Vector-valued function.
    x : numpy.ndarray
        Evaluation point.
    h : float
        Finite difference step size.

    Returns
    -------
    numpy.ndarray
        Jacobian matrix evaluated at `x`.
    """

    F0 = F(x)

    m = len(F0)
    n = len(x)

    J = np.zeros((m, n))

    for column in range(n):

        x_copy = x.copy()
        x_copy[column] += h

        F1 = F(x_copy)

        for line in range(0, m - 1):
            J[line][column] = (F1[line] - F0[line]) / h

    return J