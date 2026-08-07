import numpy as np
from src.numerical_methods.linear_algebra import linear_system

def power_method(A, x0, tol, n):
    """
        Compute the dominant eigenvalue and associated eigenvector using the
        Power Method.

        Parameters
        ----------
        A : ndarray, shape (n, n)
            Coefficient matrix.
        x0 : ndarray, shape (n,)
            Nonzero initial vector.
        tol : float
            Convergence tolerance between successive lambda estimates.
        n : int
            Maximum number of iterations.

        Returns
        -------
        actual_lambda : float
            Dominant (largest in magnitude) eigenvalue of A.
        normalized_x : ndarray, shape (n,)
            Associated eigenvector, normalized by the Euclidean norm.
        """
    
    x = x0
    previous_lambda = 0

    for k in range(1, n):
        new_x = A @ x
        actual_lambda = np.linalg.norm(new_x) / np.linalg.norm(x)
        normalized_x = new_x / np.linalg.norm(new_x)

        if np.abs(actual_lambda - previous_lambda) < tol:
            return actual_lambda, normalized_x

        previous_lambda = actual_lambda
        x = new_x

    return actual_lambda, normalized_x


def inverse_power_method(A, x0, tol, n):
    """
    Compute the smallest-magnitude eigenvalue and associated eigenvector
    using the Inverse Power Method, solving A x_{k+1} = x_k at each
    iteration (without explicitly inverting A).

    Parameters
    ----------
    A : ndarray, shape (n, n)
        Coefficient matrix.
    x0 : ndarray, shape (n,)
        Nonzero initial vector.
    tol : float
        Convergence tolerance between successive lambda estimates.
    n : int
        Maximum number of iterations.

    Returns
    -------
    actual_lambda : float
        Smallest-magnitude eigenvalue of A.
    normalized_x : ndarray, shape (n,)
        Associated eigenvector, normalized by the Euclidean norm.
    """

    x = x0
    previous_lambda = 0

    for k in range(1, n):
        new_x = linear_system.solve(A, x)

        razao = np.linalg.norm(new_x) / np.linalg.norm(x)
        actual_lambda = 1 / razao

        normalized_x = new_x / np.linalg.norm(new_x)

        if np.abs(actual_lambda - previous_lambda) < tol:
            return actual_lambda, normalized_x

        previous_lambda = actual_lambda
        x = new_x

    return actual_lambda, normalized_x