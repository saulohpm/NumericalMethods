def integrate(math_function, a: float, b: float, n: int = 100):
    """
    Approximate the definite integral of a function using the rectangle
    (midpoint-less, right-endpoint) rule.

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

    for i in range(1, n + 1):
        k = a + i * deltax
        soma += math_function(k)
    
    area = soma * deltax
    return area