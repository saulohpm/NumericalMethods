def integrate(f, a: float, b: float, n : int = 256):
    """
    Approximate the definite integral of a function using the composite
    trapezoidal rule.

    Parameters
    ----------
    f : callable
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

    h = (b - a) / n
    soma = 0

    for i in range(n):
        k1 = a + i * h
        k2 = a + (i + 1) * h
        soma += f(k1) + (1 / 2) * (f(k2) - f(k1))
    
    return soma * h

def double_integrate(f, a: float, b: float, c: float, d: float, nx: int = 256, ny: int = 256):
    """
    Approximate the double integral of a two-dimensional function using the
    trapezoidal rule over a rectangular domain.

    Parameters
    ----------
    f : callable
        Function of two variables to integrate.
    a : float
        Lower bound of the first integration dimension.
    b : float
        Upper bound of the first integration dimension.
    c : float
        Lower bound of the second integration dimension.
    d : float
        Upper bound of the second integration dimension.
    nx : int, default=256
        Number of subdivisions along the first dimension.
    ny : int, default=256
        Number of subdivisions along the second dimension.

    Returns
    -------
    float
        Approximation of the double integral of `f` over the rectangular domain
        [a, b] x [c, d].
    """
    
    hx = (b - a) / nx
    hy = (d - c) / ny

    soma = 0

    for i in range(nx):
        k1 = a + i * hx
        k2 = a + (i + 1) * hx

        for j in range(ny):
            l1 = c + j * hy
            l2 = c + (j + 1) * hy

            soma += (f(k1, l1) + f(k2, l1) + f(k1, l2) + f(k2, l2)) / 4

    return soma * hx * hy