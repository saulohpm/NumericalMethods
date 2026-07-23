def integrate(f, a: float, b: float, n: int = 100):
    """
    Approximate the definite integral of a function using Simpson's 1/3 rule.

    Parameters
    ----------
    f : callable
        Function to integrate. Must accept and return a float.
    a : float
        Lower bound of integration.
    b : float
        Upper bound of integration.
    n : int, optional
        Number of subintervals (default 100). Must be even.

    Returns
    -------
    float
        Approximate value of the definite integral of f over [a, b].

    Raises
    ------
    ValueError
        If n is not even, since Simpson's 1/3 rule requires an even number
        of subintervals.
    """
    if n % 2 != 0:
        raise ValueError("ERROR: 'n' must be even for Simpson's Rule")
    
    else:
        soma = 0
        L = b - a
        deltax = L / n

        for i in range(0, n - 1, 2):
            zeta1 = a + i * deltax
            zeta2 = a + (i + 1) * deltax
            zeta3 = a + (i + 2) * deltax
            soma += f(zeta1) + 4 * f(zeta2) + f(zeta3)
        
        area = soma * deltax / 3
        return area