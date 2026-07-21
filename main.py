import numpy as np

from integration import simpson1
from differentiation.finite_differences import central

# ==========================================================
# Numerical Methods Library - Quick Example
#
# This file contains only a minimal example of how to use
# the library.
#
# For benchmarks, comparisons between methods, plots and
# detailed explanations, see the Jupyter Notebook.
# ==========================================================

# Function
f = lambda x: np.cos(x)**5 - x**50

# Integration example
integral = simpson1.integrate(f, -np.pi, np.pi, 12)
print(f"Integral (Simpson's Rule): {integral:.6f}")

# Differentiation example
derivative = central(f, 2.0, 0.001)
print(f"Derivative at x = 2: {derivative:.6f}")