import math

from src.numerical_methods.series.fourier import approx_function as fourier
from src.numerical_methods.series.taylor import approx_function as taylor

def test_fourier_cos():
    result = fourier(math.cos, math.pi / 4, L = math.pi, n = 5)
    expected = math.cos(math.pi / 4)

    assert abs(result - expected) < 1e-3


def test_taylor_exp():
    result = taylor(math.exp, 1, a = 0, n = 8)

    assert abs(result - math.e) < 1e-4