# Numerical Methods

A simple Python library for numerical integration.

## Overview

This repository contains implementations of classical numerical integration methods:

* Rectangle Rule
* Trapezoidal Rule
* Simpson's 1/3 Rule (First Rule of Simpson)

The project was created for studying numerical methods and approximating definite integrals of arbitrary mathematical functions.

## Project Structure

```text
NumericalMethods/
│
├── main.py
│
├── visualization/
│   ├── __init__.py
│   └── plotter.py
│
├── series/
│   ├── __init__.py
│   └── fourier.py
│
└── integration/
    │   __init__.py
    ├── rectangle.py
    ├── trapezoidal.py
    ├── simpson1.py
    ├── simpson2.py
    └── gauss_legendre.py
```

## Requirements

* Python 3.10+

## Usage

Import the desired integration method and provide:

* A mathematical function `f(x)`
* Lower integration bound `a`
* Upper integration bound `b`
* Number of subdivisions `n`

Example:

```python
f = lambda x: x ** 2

result = integrate.trapezius(f, 0, 1, 1000)
print(result)
```