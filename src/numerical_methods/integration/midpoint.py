def integrate(f, a: float, b: float, n: int = 256):
    """
    Approximate the definite integral of a one-dimensional function using the midpoint rule.

    Parameters
    ----------
    f : callable
        Function of a single variable.
    a : float
        Lower integration limit.
    b : float
        Upper integration limit.
    n : int, default=256
        Number of subintervals.

    Returns
    -------
    float
        Approximation of the integral over [a, b].
    """

    soma = 0
    h = (b - a) / n

    for i in range(n):
        xi = a + h / 2 + i * h
        soma += f(xi)

    return h * soma

def double_integrate(f, a: float, b: float, c: float, d: float, nx: int = 256, ny: int = 256):
    """
    Approximate the definite integral of a two-dimensional function.

    Parameters
    ----------
    f : callable
        Function of two variables.
    a : float
        Lower limit for the first variable.
    b : float
        Upper limit for the first variable.
    c : float
        Lower limit for the second variable.
    d : float
        Upper limit for the second variable.
    nx : int, default=256
        Number of subintervals for the first variable.
    ny : int, default=256
        Number of subintervals for the second variable.

    Returns
    -------
    float
        Approximation of the double integral.
    """

    def g(x):
        return integrate(lambda y: f(x, y), c, d, ny)

    return integrate(g, a, b, nx)

def triple_integrate(g, a: float, b: float, c: float, d: float, e: float, f: float, nx: int = 256, ny: int = 256, nz: int = 256):
    """
    Approximate the definite integral of a three-dimensional function.

    Parameters
    ----------
    g : callable
        Function of three variables.
    a : float
        Lower limit for the first variable.
    b : float
        Upper limit for the first variable.
    c : float
        Lower limit for the second variable.
    d : float
        Upper limit for the second variable.
    e : float
        Lower limit for the third variable.
    f : float
        Upper limit for the third variable.
    nx : int, default=256
        Number of subintervals for the first variable.
    ny : int, default=256
        Number of subintervals for the second variable.
    nz : int, default=256
        Number of subintervals for the third variable.

    Returns
    -------
    float
        Approximation of the triple integral.
    """

    def p(x):
        return double_integrate(lambda y, z: g(x, y, z), c, d, e, f, ny, nz)

    return integrate(p, a, b, nx)