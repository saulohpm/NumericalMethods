import numpy as np
import os
from integration import rectangle, trapezoidal, simpson1, simpson2, gauss_legendre
from series import fourier
from visualization.plotter import plot_function
from scipy.integrate import quad


# Integration Interval
a = -np.pi
b = np.pi
L = (b - a) / 2

n = 30

# Mesh (Domain)
x = np.linspace(a, b, 1000)

# Fuction f(x)
f = lambda x: np.cos(x) ** 2

# Integral Calculation
retantulo = rectangle.integrate(f, a, b, n)
trapezio = trapezoidal.integrate(f, a, b, n)
simpsonsrule = simpson1.integrate(f, a, b, n)
simpsonsrule2 = simpson2.integrate(f, a, b, n)
gausslegendre = gauss_legendre.integrate(f, a, b, n)

# Print on CLI
os.system("cls" if os.name == "nt" else "clear")

print(f"Integrating f(x) using:")

print(f"\nRectangle Rule, we obtain: {round(retantulo, 5)}")
print(f"\nTrapezoid Rule, we obtain: {round(trapezio, 5)}")
print(f"\nFirst Simpson's Rule, we obtain: {round(simpsonsrule, 5)}")
print(f"\nSecond Simpson's Rule, we obtain: {round(simpsonsrule2, 5)}")
print(f"\nGauss-Legendre Quadranture, we obtain: {round(gausslegendre, 5)}")
print(f"\nScipy Library Quadranture, we obtain: {round(quad(f, a, b)[0], 5)}")

# Plot:
plot_function(f, x, a, b, fourier.approx_function(f, x, L, n))