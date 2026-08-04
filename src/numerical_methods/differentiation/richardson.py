from .finite_differences import central

def calculate(f, x0: float, h: float):
    """
    Improves the accuracy of a numerical derivative using Richardson
    extrapolation on the central finite difference method.

    Parameters
    ----------
    f : callable
        Function to be differentiated.
    x0 : float
        Point at which the derivative is evaluated.
    h : float
        Base step size used for the finite difference approximation.

    Returns
    -------
    float
        Richardson-extrapolated approximation of the derivative at `x0`.
    """
    Dh = central(f, x0, h)
    Dh_half = central(f, x0, h / 2)

    Dr = (4 * Dh_half - Dh) / 3

    return Dr