from src.numerical_methods.differentiation import finites_differences as fn

def calculate(f, x0: float, n: int, tolerance: float = 1e-6):
    """
    Finds a root of a function using the Newton-Raphson method.

    Parameters:
        f (callable): Function for which the root is searched.
        x0 (float): Initial guess for the root.
        n (int): Maximum number of iterations allowed.
        tolerance (float): Desired tolerance for convergence
    Returns:
        tuple:
            - float: Approximation of the root.
            - int: Number of iterations performed.

    Raises:
        ValueError: If the derivative is too close to zero or if the method
            does not converge within the maximum number of iterations.
    """

    x_actual = x0

    for k in range(1, n + 1):
        derivative = fn.central(f, x_actual)

        if abs(derivative) < 1e-12: raise ValueError("ERROR: Derivative very close to zero")

        x_new = x_actual - (f(x_actual) / derivative)

        if (abs(x_new - x_actual) < tolerance) or (abs(f(x_new)) < tolerance): return x_new, k

        x_actual = x_new

    raise ValueError("Did not converge within the maximum number of iterations.")