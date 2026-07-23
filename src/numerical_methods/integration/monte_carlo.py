import numpy as np

def integrate(math_function, a: float, b: float, N: int = 10000):
    """
    Approximate the definite integral of a function using the Monte Carlo
    method with uniformly sampled random points.

    Parameters
    ----------
    math_function : callable
        Function to integrate. Must accept and return a float.
    a : float
        Lower bound of integration.
    b : float
        Upper bound of integration.
    N : int, optional
        Number of random sample points (default 10,000). Higher values reduce
        variance and improve accuracy.

    Returns
    -------
    float
        Approximate value of the definite integral of math_function over [a, b].
    """

    soma = 0
    gama = (b - a) / N
    ui = np.random.random(N)

    for i in range(0, N):
        xi = a + (b - a) * ui[i]
        soma += math_function(xi)
    
    area = soma * gama
    return area