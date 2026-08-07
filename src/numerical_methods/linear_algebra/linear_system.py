import numpy as np
from . import elimination, decomposition

def solve(A, b, method: str = "LU"):
    """
    Solve a linear system Ax = b using direct numerical methods.

    Parameters
    ----------
    A : array_like
        Coefficient matrix of the linear system.
    b : array_like
        Right-hand side vector.
    method : str, optional
        Solution method. Available options are:
        - "LU" : LU decomposition (default).
        - "gauss" : Gaussian elimination with partial pivoting.
        - "cholesky" : Cholesky decomposition (for symmetric positive definite matrices).
        - "QR" : QR decomposition.

    Returns
    -------
    x : ndarray
        Solution vector of the linear system.

    Notes
    -----
    LU decomposition is used by default. Gaussian elimination, Cholesky
    decomposition, and QR decomposition are also available. Cholesky
    requires the coefficient matrix to be symmetric positive definite,
    while QR decomposition is applicable to general matrices and is
    particularly useful for numerically stable solutions.
    """

    A = A.copy()
    b = b.copy()

    if A.shape[0] != A.shape[1] or A.shape[0] != b.shape[0]:
        raise ValueError("ERROR: The linear system must be 'A[n×n] * x[n] = b[n]'")

    if method.lower() == "gauss":

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

    elif method.lower() == "cholesky":

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

    elif method.upper() == "QR":

        Q, R = decomposition.QR(A)
        n = len(Q)
        y = np.zeros(n)
        x = np.zeros(n)

        for i in range(n):
            soma = 0
            for j in range(n):
                soma += Q[j][i] * b[j]

            y[i] = soma

        for i in range(n - 1, -1, -1):
            soma = 0

            for k in range(i + 1, n):
                soma += R[i][k] * x[k]

            x[i] = (y[i] - soma) / R[i][i]

    return x