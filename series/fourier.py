import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

L = 1
n = 30

x = np.linspace(-L, L, 1000)

f = lambda x: (x ** 2) ** (1 / 2)

a0 = 1 / L * integrate.quad(f, -L, L)[0]

cn = lambda k, x: np.cos((k * np.pi * x) / L)
sn = lambda k, x: np.sin((k * np.pi * x) / L)

an = lambda k: (1 / L) * integrate.quad(lambda x: f(x) * cn(k, x), -L, L)[0]
bn = lambda k: (1 / L) * integrate.quad(lambda x: f(x) * sn(k, x), -L, L)[0]

def fn(x):

    un = a0 * 1 / 2

    for k in range(1, n + 1):
        un += an(k) * cn(k, x)
        un += bn(k) * sn(k, x)

    return un

plt.title(f"Interações usando Serie de Fourier: {n}")
plt.plot(x, f(x), label='f(x)')
plt.plot(x, fn(x), label='Fourier')
plt.legend()
plt.grid()
plt.show()