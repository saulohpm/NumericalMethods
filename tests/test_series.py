import math

from series.fourier import approx_function
from series.taylor import approx_function

def test_fourier_cos():
    result = approx_function(math.cos, math.pi / 4, L=math.pi, n=5)
    expected = math.cos(math.pi / 4)

    assert abs(result - expected) < 1e-3


def test_taylor_exp():
    result = approx_function(math.exp, 1, a=0, n=8)

    assert abs(result - math.e) < 1e-4