from src.numerical_methods.root import bisection

def quadratic(x):
    return x ** 2 - 9


def test_bisection():
    result = bisection.calculate(quadratic, 0, 5, 1e-4)
    expected = 3

    assert abs(result - expected) < 1e-4