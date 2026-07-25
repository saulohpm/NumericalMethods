import math
import sys
from ..differentiation import finites_differences as fn

def approx_function(f, x, a, n = 3, deltax = 1e-4):
    """
    Approximate f(x) using its Taylor series expansion around the point a.

    Parameters
    ----------
    f : callable
        Function to approximate. Must accept and return a float.
    x : float or ndarray
        Point, or array of points (mesh), at which the Taylor series
        approximation is evaluated.
    a : float
        Point around which the function is expanded.
    n : int, optional
        Order (number of terms) of the Taylor series (default 3).
    deltax : float, optional
        Step size used to approximate each derivative (default 1e-4).

    Returns
    -------
    float or ndarray
        Approximate value(s) of f(x) given by the n-th order Taylor
        polynomial centered at a.
    """

    EPS = sys.float_info.epsilon

    def derivatives_calculate(f, a, n):
        derivatives = [f(a)]

        for i in range(1, n + 1):
            deltax_new = EPS ** (1 / (i + 2))
            derivatives.append(fn.central_nth(f, a, deltax_new, i))

        return derivatives

    derivatives = derivatives_calculate(f, a, n)
    total = 0

    for i in range(n + 1):
        total += derivatives[i] / math.factorial(i) * (x - a) ** i

    return total