import numpy as np
from src.numerical_methods.linear_algebra import jacobian, gauss_elimination

EXPECTED = 6

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
result = gauss_elimination.gauss_method(matrix.copy())
assert np.all(np.abs(result - EXPECTED_gausselimination) < 1e-6)