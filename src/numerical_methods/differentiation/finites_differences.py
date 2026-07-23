def forward(f, x0: float, deltax: float = 1e-5):
    """
    Approximate the derivative of f at x0 using the forward difference formula.

    Parameters
    ----------
    f : callable
        Function to differentiate. Must accept and return a float.
    x0 : float
        Point at which the derivative is evaluated.
    deltax : float, optional
        Step size used in the finite difference approximation (default 1e-5).

    Returns
    -------
    float
        Approximate value of f'(x0).
    """
    return (f(x0 + deltax) - f(x0)) / deltax

def backward(f, x0, deltax = 1e-5):
    """
    Approximate the derivative of f at x0 using the backward difference formula.

    Parameters
    ----------
    f : callable
        Function to differentiate. Must accept and return a float.
    x0 : float
        Point at which the derivative is evaluated.
    deltax : float, optional
        Step size used in the finite difference approximation (default 1e-5).

    Returns
    -------
    float
        Approximate value of f'(x0).
    """
    return (f(x0) - f(x0 - deltax)) / deltax

def central(f, x0, deltax = 1e-5):
    """
    Approximate the derivative of f at x0 using the central difference formula.

    Parameters
    ----------
    f : callable
        Function to differentiate. Must accept and return a float.
    x0 : float
        Point at which the derivative is evaluated.
    deltax : float, optional
        Step size used in the finite difference approximation (default 1e-5).

    Returns
    -------
    float
        Approximate value of f'(x0). Generally more accurate than
        forward/backward difference for the same step size.
    """
    return (f(x0 + deltax) - f(x0 - deltax)) / (2 * deltax)