# Numerical Methods

Python implementations of classical numerical integration methods and related numerical analysis tools.

## Project Structure

```text
NumericalMethods/
│
├── main.py
├── notebook.ipynb
├── README.md
│
├── integration/
│   ├── rectangle.py
│   ├── trapezoidal.py
│   ├── simpson1.py
│   ├── simpson2.py
│   └── gauss_legendre.py
│
├── series/
│   └── fourier.py
│
├── differentiation
│   └── finites_differences.py
│
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