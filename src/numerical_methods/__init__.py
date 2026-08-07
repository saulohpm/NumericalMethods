"""
NumericalMethods
=================

Educational implementations of classic numerical methods: numerical
integration, differentiation, root finding, series approximation,
linear algebra and simple visualization utilities.

Modules:
    integration       - rectangle, trapezoidal, Simpson (1st/2nd), Monte Carlo,
                         Gauss-Legendre quadrature
    differentiation    - forward/backward/central finite differences, Richardson
                         extrapolation
    root               - bisection, Newton-Raphson, Ridders' method
    series             - Taylor and Fourier series approximation
    linear_algebra     - Gauss elimination with pivoting, LU and Cholesky
                         decomposition, determinant, linear system solve,
                         Jacobian
    visualization      - plotting utilities

Usage:
    from numerical_methods import trapezoidal_integrate, fd

    df = fd.central(f, x)
"""

# src/numerical_methods/__init__.py
from .differentiation.finite_differences import forward as fd_forward_derivative
from .differentiation.finite_differences import backward as fd_backward_derivative
from .differentiation.finite_differences import central as fd_central_derivative
from .differentiation.finite_differences import central_nth as fd_nth_derivative
from .differentiation.finite_differences import forward as fd_forward_derivative
from .differentiation.finite_differences import backward as fd_backward_derivative
from .differentiation.finite_differences import central as fd_central_derivative
from .differentiation.finite_differences import central_nth as fd_nth_derivative
from .differentiation.richardson import calculate as richardson_derivative

from .integration.rectangle import integrate as rectangle_integrate
from .integration.trapezoidal import integrate as trapezoidal_integrate
from .integration.trapezoidal import double_integrate as trapezoidal_double_integrate
from .integration.midpoint import integrate as midpoint_integrate
from .integration.midpoint import double_integrate as midpoint_double_integrate
from .integration.midpoint import triple_integrate as midpoint_triple_integrate
from .integration.trapezoidal import integrate as trapezoidal_integrate
from .integration.trapezoidal import double_integrate as trapezoidal_double_integrate
from .integration.midpoint import integrate as midpoint_integrate
from .integration.midpoint import double_integrate as midpoint_double_integrate
from .integration.midpoint import triple_integrate as midpoint_triple_integrate
from .integration.simpson1 import integrate as simpson1_integrate
from .integration.simpson2 import integrate as simpson2_integrate
from .integration.monte_carlo import integrate as monte_carlo_integrate
from .integration.gauss_legendre import integrate as gauss_legendre_integrate

from .linear_algebra.jacobian import calculate as jacobian_calculate
from .linear_algebra.elimination import gauss as gauss_elimination, pivoting as pivoting_elimination
from .linear_algebra.decomposition import LU as lu_decomposition, cholesky as cholesky_decomposition, QR as QR_decomposition
from .linear_algebra.determinant import calculate as determinant_calculate
from .linear_algebra.linear_system import solve as linearsystem_solve

from .roots.bisection import calculate as bisection_calculate
from .roots.newton_raphson import calculate as newton_raphson_calculate
from .roots.ridders import calculate as ridders_calculate

from .series.taylor import approx_function as taylor_approx
from .series.fourier import approx_function as fourier_approx

from .visualization.plotter import plot_function

__version__ = "4.6"

__all__ = [
    # Differentiation
    "fd_forward_derivative",
    "fd_backward_derivative",
    "fd_central_derivative",
    "fd_nth_derivative",
    # Differentiation
    "fd_forward_derivative",
    "fd_backward_derivative",
    "fd_central_derivative",
    "fd_nth_derivative",
    "richardson_derivative",

    # Integration

    # Integration
    "rectangle_integrate",
    "trapezoidal_integrate",
    "trapezoidal_double_integrate",
    "midpoint_integrate",
    "midpoint_double_integrate",
    "midpoint_triple_integrate",
    "trapezoidal_integrate",
    "trapezoidal_double_integrate",
    "midpoint_integrate",
    "midpoint_double_integrate",
    "midpoint_triple_integrate",
    "simpson1_integrate",
    "simpson2_integrate",
    "monte_carlo_integrate",
    "gauss_legendre_integrate",

    # Linear Algebra

    # Linear Algebra
    "jacobian_calculate",
    "gauss_elimination",
    "pivoting_elimination",
    "lu_decomposition",
    "cholesky_decomposition",
    "QR_decomposition",
    "determinant_calculate",
    "linearsystem_solve",

    # Root Finding

    # Root Finding
    "bisection_calculate",
    "newton_raphson_calculate",
    "ridders_calculate",

    # Series

    # Series
    "taylor_approx",
    "fourier_approx",

    # Visualization
    "plot_function",

    # Visualization
    "plot_function",
]