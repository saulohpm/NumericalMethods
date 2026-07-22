import numpy as np

from integration import simpson1, monte_carlo
from differentiation.finites_differences import central

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
f = lambda x: x ** 2

n = 12 * 1000

# Integration example
integral = simpson1.integrate(f, -np.pi, np.pi, n)
print(f"Integral (Simpson's Rule): {integral:.6f}")

integral2 = monte_carlo.integrate(f, -np.pi, np.pi, n)
print(f"Integral (Monte Carlo): {integral2:.6f}")

# Taylor Series Example


# Differentiation example
derivative = central(f, 2.0, 0.001)
print(f"Derivative at x = 2: {derivative:.6f}")