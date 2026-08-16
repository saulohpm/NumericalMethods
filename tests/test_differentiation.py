from numerical_methods.differentiation.finite_differences import forward, backward, central
from numerical_methods.differentiation import richardson

EXPECTED = 6

def quadratic(x):
    return x ** 2


def test_forward():
    assert abs(forward(quadratic, 3) - EXPECTED) < 1e-4


def test_backward():
    assert abs(backward(quadratic, 3) - EXPECTED) < 1e-4


def test_central():
    assert abs(central(quadratic, 3) - EXPECTED) < 1e-6


def test_richardson():
    assert abs(richardson.calculate(quadratic, 3, 1e-2) - EXPECTED) < 1e-10