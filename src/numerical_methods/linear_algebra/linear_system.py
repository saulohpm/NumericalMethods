import numpy as np
from . import elimination, decomposition

def solve(A, b, method: str = "LU"):
    """
    Solve a linear system Ax = b using numerical decomposition methods.

    Parameters
    ----------
    A : array_like
        Coefficient matrix of the linear system.
    b : array_like
        Right-hand side vector.
    method : str, optional
        Solution method. Available options are "LU", "gauss", and
        "cholesky".

    Returns
    -------
    x : ndarray
        Solution vector of the system.

    Notes
    -----
    The default method uses LU decomposition. Gaussian elimination
    with pivoting is also available for general systems.
    """

    A = A.copy()
    b = b.copy()

    if method == "gauss":

        A_tilde = np.column_stack((A, b))
        A_pivoted = elimination.pivoting(A_tilde)[0]
        U_tilde = elimination.gauss(A_pivoted)[0]
        U = U_tilde[:, :-1]
        b_new = U_tilde[:, -1]
        n = len(U)
        x = np.zeros(n)

        for i in range(n - 1, -1, -1):
            soma = 0

            for k in range(i + 1, n):
                soma += U[i][k] * x[k]

            x[i] = b_new[i] - soma

    elif method.upper() == "LU":

        L, U = decomposition.LU(A)
        n = len(L)
        y = np.zeros(n)
        x = np.zeros(n)

        for i in range(n):
            soma = 0

            for k in range(i):
                soma += L[i][k] * y[k]

            y[i] = (b[i] - soma) / L[i][i]

        for i in range(n - 1, -1, -1):
            soma = 0

            for k in range(i + 1, n):
                soma += U[i][k] * x[k]

            x[i] = y[i] - soma

    else:

        U = decomposition.cholesky(A)
        n = len(U)
        y = np.zeros(n)
        x = np.zeros(n)

        for i in range(n):
            soma = 0

            for k in range(i):
                soma += U[k][i] * y[k]

            y[i] = (b[i] - soma) / U[i][i]

        for i in range(n - 1, -1, -1):
            soma = 0

            for k in range(i + 1, n):
                soma += U[i][k] * x[k]

            x[i] = (y[i] - soma) / U[i][i]

    return x