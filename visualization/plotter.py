import numpy as np
import matplotlib.pyplot as plt
from integration.gauss_legendre import integrate

def plot_function(f, a, b):

    x = np.linspace(a, b, 1000)
    y = f(x)

    plt.figure(figsize = (14,6))

    plt.plot(x, y, color='blue')
    plt.fill_between(x, y, alpha=0.3)
    plt.title("Integral Definida")
    plt.xlim(a, b)
    plt.ylim(0, float(f(b)))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.75)

    plt.show()