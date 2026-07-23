def integrate(math_function, a: float, b: float, n : int = 100):
    """
    Approximate the definite integral of a function using the composite
    trapezoidal rule.

    Parameters
    ----------
    math_function : callable
        Function to integrate. Must accept and return a float.
    a : float
        Lower bound of integration.
    b : float
        Upper bound of integration.
    n : int, optional
        Number of subintervals (default 100). Higher values increase accuracy.

    Returns
    -------
    float
        Approximate value of the definite integral of math_function over [a, b].
    """
    
    soma = 0
    L = b - a
    deltax = L / n

    for i in range(0, n):
        k1 = a + i * deltax
        k2 = a + (i + 1) * deltax
        soma += math_function(k1) + (1 / 2) * (math_function(k2) - math_function(k1))
    
    area = soma * deltax
    return area