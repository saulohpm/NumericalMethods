import numpy as np

def LU(matrix):
    """
    Performs the LU decomposition of a square matrix using Crout's method.

    Parameters
    ----------
    matrix : numpy.ndarray
        Square matrix to decompose.

    Returns
    -------
    L : numpy.ndarray
        Lower triangular matrix.

    U : numpy.ndarray
        Upper triangular matrix with unit diagonal.
    """

    n = len(matrix)
    A = matrix.copy()
    U = np.zeros((n, n))
    L = np.zeros((n, n))

    for j in range(n):
        for i in range(n):

            if i > j:
                soma = 0

                for k in range(0, j):
                    soma += L[i][k] * U[k][j]

                L[i][j] = A[i][j] - soma

            elif i < j:
                soma = 0

                for k in range(0, i):
                    soma += L[i][k] * U[k][j]

                U[i][j] = (A[i][j] - soma) / L[i][i]

            else:
                soma = 0
                U[i][i] = 1

                for k in range(i):
                    soma += L[i][k] * U[k][i]

                L[i][i] = A[i][i] - soma

                
                
    return L, U

