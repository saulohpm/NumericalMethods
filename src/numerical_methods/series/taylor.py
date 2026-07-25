import math
from ..differentiation import finites_differences

def approx_function(f, x, a, n = 3, deltax = 1e-2):
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
        Point around which the function is expanded.
    n : int, optional
        Order (number of terms) of the Taylor series (default 3).
    deltax : float, optional
        Step size used to approximate each derivative (default 1e-2).

    Returns
    -------
    float or ndarray
        Approximate value(s) of f(x) given by the n-th order Taylor
        polynomial centered at a.
    """

    def derivatives_calculate(f, a, n, deltax):

        derivatives = [f(a)]
        derivative = f

        for i in range(n):
            deltax_progressive = deltax * (2 ** i)
            derivative = lambda x, derivative=derivative: finites_differences.central(derivative, x, deltax_progressive)
            derivatives.append(derivative(a))

        return derivatives

    derivatives = derivatives_calculate(f, a, n, deltax)
    total = 0

    for i in range(0, n + 1):
        total += derivatives[i] / math.factorial(i) * (x - a) ** i

    return total