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

from .integration.rectangle import integrate as rectangle_integrate
from .integration.trapezoidal import integrate as trapezoidal_integrate
from .integration.simpson1 import integrate as simpson1_integrate
from .integration.simpson2 import integrate as simpson2_integrate
from .integration.monte_carlo import integrate as monte_carlo_integrate
from .integration.gauss_legendre import integrate as gauss_legendre_integrate

from .differentiation import finites_differences as fd
from .differentiation import jacobian

from .series.taylor import approx_function as taylor_approx
from .series.fourier import approx_function as fourier_approx

from .root.bisection import calculate as bisection_calculate
from .root.newton_raphson import calculate as newton_raphson_calculate
from .root.ridders import calculate as ridders_calculate

from .visualization.plotter import plot_function

__version__ = "2.4.8"

__all__ = [
    "rectangle_integrate",
    "trapezoidal_integrate",
    "simpson1_integrate",
    "simpson2_integrate",
    "monte_carlo_integrate",
    "gauss_legendre_integrate",
    "fd",
    "jacobian",
    "taylor_approx",
    "fourier_approx",
    "bisection_calculate",
    "newton_raphson_calculate",
    "ridders_calculate",
    "plot_function"
]