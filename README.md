# Numerical Methods

A small Python library with implementations of classic numerical methods for
integration, differentiation, and series approximation.

This started as a study project to practice numerical analysis concepts and
has since been reorganized as an installable Python package, with unit
tests and docstrings, as a way to also practice good project structure.

## Project structure

```text
Numerical-Methods/
│
├── main.py                     # Minimal usage example (usando 'from src...')
├── notebook.ipynb              # Detailed examples and plots
├── pyproject.toml              # Project settings and setuptool
├── README.md                   # Basic Document
│
├── src/
│   └── numerical_methods/
│       ├── __init__.py
│       │
│       ├── integration/
│       │   ├── __init__.py
│       │   ├── rectangle.py
│       │   ├── trapezoidal.py
│       │   ├── simpson1.py
│       │   ├── simpson2.py
│       │   ├── monte_carlo.py
│       │   └── gauss_legendre.py
│       │
│       ├── root/
│       │   ├── __init__.py
│       │   └── bisection.py
│       │
│       ├── differentiation/
│       │   ├── __init__.py
│       │   └── finites_differences.py
│       │
│       ├── series/
│       │   ├── __init__.py
│       │   ├── taylor.py
│       │   └── fourier.py
│       │
│       └── visualization/
│           └── __init__.py
│
└── tests/
    ├── __init__.py
    ├── test_integration.py
    ├── test_differentiation.py
    └── test_series.py
```

## Requirements

* Python 3.9 or later

## Installation

```bash
git clone <repository-url>
cd Numerical-Methods
pip install -e ".[dev]"
```

This installs the package in editable mode, along with `pytest` for running
the tests.

## Usage

```python
from src.integration import trapezoidal

f = lambda x: x ** 2
result = trapezoidal.integrate(f, 0, 1, n=1000)
print(result)
```

A quick runnable example is also available in `main.py`:

```bash
python main.py
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