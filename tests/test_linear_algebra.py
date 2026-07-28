import numpy as np
from src.numerical_methods.linear_algebra import jacobian
from src.numerical_methods.linear_algebra.gauss_elimination import pivoting, gauss_method, determinant

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
result, _ = gauss_method(matrix.copy())
assert np.all(np.abs(result - EXPECTED_gausselimination) < 1e-6)

# Pivoting
matrix_pivoting = np.array([[1.0, 2.0, 2.0], [3.0, 6.0, 1.0], [2.0, 6.0, -1.0]])
EXPECTED_pivoting = np.array([[3.0, 6.0, 1.0], [2.0, 6.0, -1.0], [1.0, 2.0, 2.0]])
result_pivoting, _ = pivoting(matrix_pivoting.copy())
assert np.all(np.abs(result_pivoting - EXPECTED_pivoting) < 1e-6)

# Determinant
A = np.array([[1., 2., 1.], [2., 4.01, 1.], [1., 1., 5.]])

EXPECTED_determinant_A = -0.96
result_A = determinant(A)
assert np.abs(result_A - EXPECTED_determinant_A) < 1e-6