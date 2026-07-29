from .elimination import pivoting, gauss
from .decomposition import LU

def calculate(matrix, method: str = "auto"):
    """
    Computes the determinant of a square matrix.

    Parameters
    ----------
    matrix : numpy.ndarray
        Square matrix.

    method : {"auto", "gauss", "lu"}, default = "auto"
        Algorithm used to compute the determinant.

    Returns
    -------
    float
        Determinant of the input matrix.
    """

    if method == "gauss":
        return _gauss(matrix)
    else:
        return _lu(matrix)


def _gauss(matrix):
    """
    Computes the determinant using Gaussian elimination.

    Parameters
    ----------
    matrix : numpy.ndarray
        Square matrix. The input is not modified.

    Returns
    -------
    float
        Determinant of the input matrix.
    """

    A_pivoted, p = pivoting(matrix)
    _, factors = gauss(A_pivoted)

    det = (-1) ** p
    for f in factors:
        det *= f

    return det


def _lu(matrix):
    """
    Computes the determinant using the LU decomposition.

    Parameters
    ----------
    matrix : numpy.ndarray
        Square matrix.

    Returns
    -------
    float
        Determinant of the input matrix.
    """

    L, _ = LU(matrix)
    n = len(L)
    det = 1

    for i in range(n):
        det *= L[i][i]

    return det