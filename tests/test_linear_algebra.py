import numpy as np
from src.numerical_methods.linear_algebra import jacobian

EXPECTED = 6

def F(x):
    return np.array([x[0] ** 2 + x[1], x[0] * x[1]])

x = np.array([3.0, 2.0])
h = 1e-6
EXPECTED = np.array([[6.0, 1.0], [2.0, 3.0]])

J = jacobian.calculate(F, x, h)

assert np.all(np.abs(J - EXPECTED) < 1e-4)