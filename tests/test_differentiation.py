from src.numerical_methods.differentiation.finites_differences import forward, backward, central

EXPECTED = 6

def quadratic(x):
    return x ** 2


def test_forward():
    assert abs(forward(quadratic, 3) - EXPECTED) < 1e-4


def test_backward():
    assert abs(backward(quadratic, 3) - EXPECTED) < 1e-4


def test_central():
    assert abs(central(quadratic, 3) - EXPECTED) < 1e-6