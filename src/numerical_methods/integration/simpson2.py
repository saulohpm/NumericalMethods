def integrate(f, a: float, b: float, n: int = 100):
    """
    Approximate the definite integral of a function using Simpson's 3/8 rule.

    Parameters
    ----------
    f : callable
        Function to integrate. Must accept and return a float.
    a : float
        Lower bound of integration.
    b : float
        Upper bound of integration.
    n : int, optional
        Number of subintervals (default 100). Must be a multiple of 3.

    Returns
    -------
    float
        Approximate value of the definite integral of f over [a, b].

    Raises
    ------
    ValueError
        If n is not a multiple of 3, since Simpson's 3/8 rule requires it.
    """
    if n % 3 != 0:
        raise ValueError("ERROR: 'n' must be a multiple of 3 for Simpson's 3/8 rule.")

    soma = 0
    L = b - a
    deltax = L / n

    for i in range(0, n - 2, 3):
        zeta1 = a + i * deltax
        zeta2 = a + (i + 1) * deltax
        zeta3 = a + (i + 2) * deltax
        zeta4 = a + (i + 3) * deltax
        soma += f(zeta1) + 3 * f(zeta2) + 3 * f(zeta3) + f(zeta4)
    
    area = soma * 3 * deltax / 8
    return area