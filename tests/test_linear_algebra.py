import numpy as np
from src.numerical_methods.linear_algebra import jacobian, elimination, decomposition, determinant

def F(x):
    return np.array([x[0] ** 2 + x[1], x[0] * x[1]])

# Jacobian
x = np.array([3.0, 2.0])
h = 1e-6
EXPECTED_jacobian = np.array([[6.0, 1.0], [2.0, 3.0]])
J = jacobian.calculate(F, x, h)
assert np.all(np.abs(J - EXPECTED_jacobian) < 1e-4)

# Gauss Elimination
matrix = np.array([[2.0, 1.0, 5.0], [4.0, 4.0, 6.0], [2.0, 3.0, 8.0]])
EXPECTED_gausselimination = np.array([[1.0, 0.5, 2.5], [0.0, 1.0, -2.0], [0.0, 0.0, 1.0]])
result, _ = elimination.gauss(matrix.copy())
assert np.all(np.abs(result - EXPECTED_gausselimination) < 1e-6)

# Pivoting
matrix_pivoting = np.array([[1.0, 2.0, 2.0], [3.0, 6.0, 1.0], [2.0, 6.0, -1.0]])
EXPECTED_pivoting = np.array([[3.0, 6.0, 1.0], [2.0, 6.0, -1.0], [1.0, 2.0, 2.0]])
result_pivoting, _ = elimination.pivoting(matrix_pivoting.copy())
assert np.all(np.abs(result_pivoting - EXPECTED_pivoting) < 1e-6)

# Determinant
A = np.array([[1., 2., 1.], [2., 4.01, 1.], [1., 1., 5.]])

EXPECTED_determinant_A = -0.96
result_A = determinant.calculate(A)
assert np.abs(result_A - EXPECTED_determinant_A) < 1e-6

# LU Decomposition (Crout)
A = np.array([[2., 1., 1.], [4., -6., 0.], [-2., 7., 2.]])

EXPECTED_L = np.array([[2., 0., 0.], [4., -8., 0.], [-2., 8., 1.]])

EXPECTED_U = np.array([[1., 0.5, 0.5], [0., 1., 0.25], [0., 0., 1.]])

L, U = decomposition.LU(A.copy())

assert np.allclose(L, EXPECTED_L)
assert np.allclose(U, EXPECTED_U)
assert np.allclose(np.tril(L), L)
assert np.allclose(np.triu(U), U)
assert np.allclose(np.diag(U), np.ones(A.shape[0]))
assert np.allclose(L @ U, A)