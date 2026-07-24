from src.numerical_methods.root import ridders
from src.numerical_methods.root import bisection, newton_raphson

def quadratic(x):
    return x ** 2 - 9

expected = 3
error = 1e-4


def test_bisection():
    result = bisection.calculate(quadratic, 0, 5, 1e-4)

    assert abs(result - expected) < error


def test_newton_raphson():
    result, _ = newton_raphson.calculate(quadratic, 5, 100)

    assert abs(result - expected) < error


def test_ridders():
    result, _ = ridders.calculate(quadratic, 0, 5, 100)

    assert abs(result - expected) < error