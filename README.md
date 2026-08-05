# Numerical Methods

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-4.2-orange)

A small Python library with implementations of classic numerical methods for
integration, differentiation, and series approximation.

This started as a study project to practice numerical analysis concepts and has since been reorganized as an installable Python package, with unit tests and docstrings, as a way to also practice good project structure.

## Project structure

```text
NumericalMethods/
│
├── pyproject.toml
├── LICENSE.txt
├── README.md
├── .gitattributes
├── .gitignore
│
├── examples/
│   ├── benchmark.ipynb
│   └── demonstration.ipynb
│
├── src/
│   └── numerical_methods/
│       ├── __init__.py
│       │
│       ├── differentiation/
│       │   ├── __init__.py
│       │   ├── finite_differences.py
│       │   └── richardson.py
│       │
│       ├── integration/
│       │   ├── __init__.py
│       │   ├── gauss_legendre.py
│       │   ├── midpoint.py
│       │   ├── monte_carlo.py
│       │   ├── rectangle.py
│       │   ├── simpson1.py
│       │   ├── simpson2.py
│       │   └── trapezoidal.py
│       │
│       ├── linear_algebra/
│       │   ├── __init__.py
│       │   ├── decomposition.py
│       │   ├── determinant.py
│       │   ├── elimination.py
│       │   ├── jacobian.py
│       │   └── linear_system.py
│       │
│       ├── roots/
│       │   ├── __init__.py
│       │   ├── bisection.py
│       │   ├── newton_raphson.py
│       │   └── ridders.py
│       │
│       ├── series/
│       │   ├── __init__.py
│       │   ├── fourier.py
│       │   └── taylor.py
│       │
│       └── visualization/
│           ├── __init__.py
│           └── plotter.py
│
└── tests/
    ├── __init__.py
    ├── test_differentiation.py
    ├── test_integration.py
    ├── test_linear_algebra.py
    ├── test_roots.py
    └── test_series.py
```

## Installation

```bash
gh repo clone saulohpm/NumericalMethods
cd NumericalMethods
pip install -e ".[dev]"
```

This installs the package in editable mode, along with `pytest` for running
the tests.

## Usage

```python
from src.integration import trapezoidal

f = lambda x: x ** 2
result = trapezoidal.integrate(f, 0, 1, n = 1000)
print(result)
```

For more detailed examples, including comparisons between methods and
plots, see `notebook.ipynb`.

## Notes and limitations

This project is meant for learning and experimentation, not for
production-grade numerical computing (for that, `numpy`/`scipy` are the
better choice). Some things worth knowing if you look at the code:

* The Taylor series approximation builds higher-order derivatives by
  repeatedly applying finite differences, which is numerically fragile —
  the default step size was chosen to keep results stable for a
  reasonable range of inputs, but it isn't a general-purpose solution.
* Methods are implemented directly from their mathematical definitions,
  favoring clarity over performance.

## License

This project is distributed under the MIT License. See the `LICENSE` file for more information.