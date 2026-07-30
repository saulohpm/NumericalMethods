"""
NumericalMethods
=================

Educational implementations of classic numerical methods: numerical
integration, differentiation, series approximation and simple
visualization utilities.

Usage:
    from numerical_methods import trapezoidal_integrate, fd
    
    df = fd.central(f, x)
"""

# src/numerical_methods/__init__.py
from .differentiation import finite_differences as fd
from .differentiation.richardson import calculate as richardson_derivative

from .integration.rectangle import integrate as rectangle_integrate
from .integration.trapezoidal import integrate as trapezoidal_integrate
from .integration.simpson1 import integrate as simpson1_integrate
from .integration.simpson2 import integrate as simpson2_integrate
from .integration.monte_carlo import integrate as monte_carlo_integrate
from .integration.gauss_legendre import integrate as gauss_legendre_integrate

from .linear_algebra.jacobian import calculate as jacobian_calculate
from .linear_algebra.elimination import gauss as gauss_elimination, pivoting as pivoting_elimination
from .linear_algebra.decomposition import LU as lu_decomposition
from .linear_algebra.determinant import calculate as determinant_calculate
from .linear_algebra.linear_system import solve as linearsystem_solve

from .roots.bisection import calculate as bisection_calculate
from .roots.newton_raphson import calculate as newton_raphson_calculate
from .roots.ridders import calculate as ridders_calculate

from .series.taylor import approx_function as taylor_approx
from .series.fourier import approx_function as fourier_approx

from .visualization.plotter import plot_function

__version__ = "3.7.0"

__all__ = [
    "fd",
    "richardson_derivative",
    "rectangle_integrate",
    "trapezoidal_integrate",
    "simpson1_integrate",
    "simpson2_integrate",
    "monte_carlo_integrate",
    "gauss_legendre_integrate",
    "jacobian_calculate",
    "gauss_elimination",
    "pivoting_elimination",
    "lu_decomposition",
    "determinant_calculate",
    "linearsystem_solve",
    "bisection_calculate",
    "newton_raphson_calculate",
    "ridders_calculate",
    "taylor_approx",
    "fourier_approx",
    "plot_function"
]