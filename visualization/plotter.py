import numpy as np
import matplotlib.pyplot as plt
from integration.gauss_legendre import integrate

def plot_function(f, x, a=None, b=None, f2 = None):

    y = f(x)

    plt.figure(figsize = (14,6))

    if a is not None and b is not None and f2 is None:
        plt.plot(x, y, color='blue')
        plt.fill_between(x, y, alpha=0.3)

        plt.title("Definite Integral")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.xlim(a, b)
        plt.ylim(0, float(f(b)))

    else:
        plt.title(f"Interactions using fourier series")
        plt.plot(x, y, label='f(x)')
        plt.plot(x, f2, label='Fourier')
        
    plt.legend()
    plt.grid(True, alpha=0.75)

    plt.show()