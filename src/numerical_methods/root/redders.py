def calculate(f, a: float, b: float, n: int, tolerance: float = 1e-6):
    """
    Finds a root of a function using Ridders' method.

    Parameters:
        f (callable): Continuous function for which the root is searched.
        a (float): Lower bound of the initial interval.
        b (float): Upper bound of the initial interval.
        n (int): Maximum number of iterations allowed.
        tolerance (float): Desired tolerance for convergence.

    Returns:
        tuple:
            - float: Approximation of the root.
            - int: Number of iterations performed.

    Raises:
        ValueError:
            - If 'a' is greater than 'b'.
            - If the initial interval does not satisfy f(a) * f(b) < 0.
            - If the auxiliary quantity S is too close to zero.
            - If the method does not converge within the maximum number of iterations.
    """

    def sgn(x):
        if x > 0: return 1
        elif x == 0: return 0
        else: return -1


    if a > b: raise ValueError("ERROR: 'a' must be less than 'b'")
    elif f(a) * f(b) >= 0: raise ValueError("ERROR: 'f(a) * f(b)' cant be zero or positive")

    for k in range(1, n + 1):

        fa = f(a)
        fb = f(b)

        m = (a + b) / 2
        fm = f(m)

        S = (fm ** 2 - fa * fb) ** (1 / 2)

        if abs(S) < 1e-15: raise ValueError("ERROR: Algorithm interrupted (resort to another method, such as bisection)")

        x = m + (m - a) * sgn(fa - fb) * fm / S
        fx = f(x)

        if abs(fx) < tolerance: return x, k

        if fm * fx < 0:
            if x > m:
                a = m
                b = x

            else:
                a = x
                b = m

        elif fa * fx < 0:
            b = x

        else:
            a = x

        if abs(b - a) < tolerance: return x

    raise ValueError("Method did not converge")