import numpy as np
from . import linear_system

def power_method(A, x0, tol: float, n: int):
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


def inverse_power_method(A, x0, tol: float, n: int):
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


def jacobi_method(A, n: int):
    """
    Compute the eigenvalues and eigenvectors of a symmetric matrix using
    the Jacobi eigenvalue method (successive rotations).

    The method applies successive orthogonal rotations R to iteratively
    zero out the largest off-diagonal element of A, so that A converges
    to a diagonal matrix whose entries are the eigenvalues, while the
    accumulated product of the rotations converges to the matrix of
    eigenvectors.

    Parameters
    ----------
    A : numpy.ndarray
        Square, symmetric matrix of shape (m, m) whose eigenvalues and
        eigenvectors are to be computed.
    n : int
        Number of iterations (Jacobi rotations) to perform.

    Returns
    -------
    A : numpy.ndarray
        Resulting matrix after `n` rotations, approximately diagonal,
        whose diagonal entries approximate the eigenvalues of A.
    X : numpy.ndarray
        Matrix whose columns approximate the eigenvectors of A,
        given by the accumulated product of the applied rotation
        matrices.

    Raises
    ------
    ValueError
        If `A` is not a square matrix.

    Notes
    -----
    At each iteration, the off-diagonal pair of indices (i, j) with the
    largest absolute value is selected (via `high_value_position`), and
    the rotation angle theta is chosen so as to annihilate the entry
    A[i, j]:

    .. math::
        \\theta = \\frac{1}{2} \\arctan\\left(
            \\frac{2 A_{ij}}{A_{ii} - A_{jj}}
        \\right)

    The update is performed as A = Rᵀ A R, and the eigenvectors are
    accumulated as X = X @ R.

    Examples
    --------
    >>> A = np.array([[4.0, 1.0], [1.0, 3.0]])
    >>> A_diag, X = jacobi_method(A, n=10)
    >>> np.diag(A_diag)  # approximate eigenvalues
    array([4.618, 2.382])
    """

    if A.shape[0] != A.shape[1]:
        raise ValueError("The matrix must be square.")

    if not np.allclose(A, A.T):
        raise ValueError("The matrix must be symmetric.")

    Alenght = len(A)
    X = np.eye(Alenght)

    for i in range(1, n):
        mi, mj = high_value_position(A)

        if mi == mj:
            break

        theta = 0.5 * np.arctan(2 * A[mi, mj] / (A[mi, mi] - A[mj, mj]))

        R = np.eye(Alenght)
        R[mi, mi] = np.cos(theta)
        R[mi, mj] = -1 * np.sin(theta)
        R[mj, mi] = np.sin(theta)
        R[mj, mj] = np.cos(theta)

        A = R.T @ A @ R
        X = X @ R

    return A, X


def high_value_position(A):
    """
    Find the position of the largest off-diagonal element (in absolute
    value) of a matrix.

    Scans only the upper triangular part of `A` (excluding the main
    diagonal), returning the indices (i, j) of the entry with the
    largest absolute value. Used by the Jacobi method to select the
    rotation pivot at each iteration.

    Parameters
    ----------
    A : numpy.ndarray
        Square matrix of shape (n, n).

    Returns
    -------
    posi : int
        Row index of the largest off-diagonal element in absolute value.
    posj : int
        Column index of the largest off-diagonal element in absolute
        value.

    Notes
    -----
    If all off-diagonal elements are zero, the function returns (0, 0),
    since `maxvalue` is initialized to 0 and no entry exceeds it.

    Examples
    --------
    >>> A = np.array([[4.0, 1.0, 0.5],
    ...               [1.0, 3.0, 2.0],
    ...               [0.5, 2.0, 5.0]])
    >>> high_value_position(A)
    (1, 2)
    """

    n = len(A)
    posi = 0
    posj = 0
    maxvalue = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            v = np.abs(A[i][j])

            if v > maxvalue:
                posi = i
                posj = j
                maxvalue = v


    return posi, posj