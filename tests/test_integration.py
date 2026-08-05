from src.numerical_methods.integration.rectangle import integrate as rectangle
from src.numerical_methods.integration.simpson1 import integrate as simpson1
from src.numerical_methods.integration.simpson2 import integrate as simpson2
from src.numerical_methods.integration.gauss_legendre import integrate as gauss_legendre
from src.numerical_methods.integration import midpoint
from src.numerical_methods.integration import trapezoidal

def f(x):
    return x ** 2

EXPECTED1 = 1 / 3

def test_rectangle():
    assert abs(rectangle(f, 0, 1, 1000) - EXPECTED1) < 1e-3

def test_trapezoidal():
    assert abs(trapezoidal.integrate(f, 0, 1, 1000) - EXPECTED1) < 1e-5

def test_simpson1():
    assert abs(simpson1(f, 0, 1, 100) - EXPECTED1) < 1e-8

def test_simpson2():
    assert abs(simpson2(f, 0, 1, 99) - EXPECTED1) < 1e-8

def test_gauss():
    assert abs(gauss_legendre(f, 0, 1, 100) - EXPECTED1) < 1e-12

def F(x, y):
    return (x ** 2) * y

EXPECTED2 = 2 / 3

def test_midpoint():
    assert abs(midpoint.double_integrate(F, 0, 1, 0, 2, 1000, 1000) - EXPECTED2) < 1e-3

def test_trapezoidal_double():
    assert abs(trapezoidal.double_integrate(F, 0, 1, 0, 2, 1000, 1000) - EXPECTED2) < 1e-3