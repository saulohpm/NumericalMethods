from src.integration.rectangle import integrate as rectangle
from src.integration.trapezoidal import integrate as trapezoidal
from src.integration.simpson1 import integrate as simpson1
from src.integration.simpson2 import integrate as simpson2
from src.integration.gauss_legendre import integrate as gauss_legendre

def f(x):
    return x ** 2

EXPECTED = 1/3

def test_rectangle():
    assert abs(rectangle(f, 0, 1, 1000) - EXPECTED) < 1e-3

def test_trapezoidal():
    assert abs(trapezoidal(f, 0, 1, 1000) - EXPECTED) < 1e-5

def test_simpson1():
    assert abs(simpson1(f, 0, 1, 100) - EXPECTED) < 1e-8

def test_simpson2():
    assert abs(simpson2(f, 0, 1, 99) - EXPECTED) < 1e-8

def test_gauss():
    assert abs(gauss_legendre(f, 0, 1) - EXPECTED) < 1e-12