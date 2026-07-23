"""
NumericalMethods
=================

Educational implementations of classic numerical methods: numerical
integration, differentiation, series approximation and simple
visualization utilities.

The most commonly used functions are re-exported here for convenience,
so they can be imported directly from the top-level package, e.g.:

    from src import trapezoidal_integrate, central
"""

# src/numerical_methods/__init__.py

from .integration.rectangle import integrate as rectangle_integrate
from .integration.trapezoidal import integrate as trapezoidal_integrate
from .integration.simpson1 import integrate as simpson1_integrate
from .integration.simpson2 import integrate as simpson2_integrate
from .integration.monte_carlo import integrate as monte_carlo_integrate
from .integration.gauss_legendre import integrate as gauss_legendre_integrate

from .differentiation.finites_differences import forward, backward, central

from .series.taylor import approx_function as taylor_approx
from .series.fourier import approx_function as fourier_approx

from .root.bisection import calculate as bisection_calculate

__version__ = "2.0.0"

__all__ = [
    "rectangle_integrate",
    "trapezoidal_integrate",
    "simpson1_integrate",
    "simpson2_integrate",
    "monte_carlo_integrate",
    "gauss_legendre_integrate",
    "forward",
    "backward",
    "central",
    "taylor_approx",
    "fourier_approx",
    "bisection_calculate"
]