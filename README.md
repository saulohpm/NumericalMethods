# Numerical Methods

Python implementations of classical numerical integration methods and related numerical analysis tools.

## Overview

This repository provides implementations of deterministic numerical integration techniques for approximating definite integrals of arbitrary functions. The project is intended for educational purposes and numerical analysis studies.

Currently implemented methods include:

- Rectangle Rule
- Trapezoidal Rule
- Simpson's 1/3 Rule
- Simpson's 3/8 Rule
- Gauss–Legendre Quadrature

Additional modules include Fourier series approximation and visualization utilities.

## Project Structure

```text
NumericalMethods/
│
├── main.py
├── integration/
│   ├── rectangle.py
│   ├── trapezoidal.py
│   ├── simpson1.py
│   ├── simpson2.py
│   └── gauss_legendre.py
├── series/
│   └── fourier.py
└── visualization/
    └── plotter.py
```

## Requirements

- Python 3.10 or later

## Example

```python
from integration import trapezoidal

f = lambda x: x ** 2

result = trapezoidal.integrate(f, 0, 1, 1000)
print(result)
```