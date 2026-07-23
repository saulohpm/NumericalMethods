import math
from src.differentiation import finites_differences

def approx_function(f, x, a = 1, n = 8, deltax = 1e-2):
    """
    Approximate f(x) using its Taylor series expansion around the point a.

    Parameters
    ----------
    f : callable
        Function to approximate. Must accept and return a float.
    x : float or ndarray
        Point, or array of points (mesh), at which the Taylor series
        approximation is evaluated.
    a : float, optional
        Point around which the function is expanded (default 1).
    n : int, optional
        Order (number of terms) of the Taylor series (default 8).
    deltax : float, optional
        Step size used to approximate each derivative (default 1e-2).
        See the note below on why this is larger than the usual 1e-5
        used for a single derivative.

    Returns
    -------
    float or ndarray
        Approximate value(s) of f(x) given by the n-th order Taylor
        polynomial centered at a.
    """

    total = f(a)
    derivative = f

    for i in range(1, n + 1):
        previous = derivative
        derivative = lambda x, previous=previous: finites_differences.central(previous, x, deltax)
        total += derivative(a) / math.factorial(i) * (x - a) ** i

    return total