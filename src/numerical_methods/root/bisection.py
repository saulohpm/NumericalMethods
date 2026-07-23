def calculate(f, a: float, b: float, error):
    """
    Finds a root of a continuous function using the bisection method.

    Parameters:
        f (callable): Function for which the root is searched.
        a (float): Lower bound of the initial interval.
        b (float): Upper bound of the initial interval.
        error (float): Desired accuracy of the result.

    Returns:
        float: Approximation of the root.

    Raises:
        ValueError: If f(a) and f(b) do not have opposite signs.
    """

    if f(a) * f(b) >= 0:
        raise ValueError("ERROR: 'f(a) * f(b)' must be less than zero.")

    else:
        while (b - a) > error:
            x = (a + b) / 2

            if f(a) * f(x) < 0:
                b = x

            else:
                a = x

        alpha = (a + b) / 2

        return alpha