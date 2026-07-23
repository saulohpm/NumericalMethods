import numpy as np
from numpy.polynomial.legendre import leggauss

def integrate(f, a: float, b: float, n: int = 5):
    """
    Approximate the definite integral of a function using Gauss-Legendre
    quadrature.

    Parameters
    ----------
    f : callable
        Function to integrate. Must accept and return a float.
    a : float
        Lower bound of integration.
    b : float
        Upper bound of integration.
    n : int, optional
        Number of quadrature points/nodes (default 5). Higher values
        increase accuracy, especially for smooth functions.

    Returns
    -------
    float
        Approximate value of the definite integral of f over [a, b].
    """
    r, w = leggauss(n)
    #r = (r1​,r2​,…,rn​)
    #w = (w1​,w2​,…,wn​)
    
    soma = 0.0

    for i in range(n):
        x = (b - a)/2 * r[i] + (a + b)/2
        soma += w[i] * f(x)

    return (b - a)/2 * soma