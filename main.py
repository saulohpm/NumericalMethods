import numpy as np
from integration import retangle, trapezoidal, simpson1, simpson2

# Intervalo de Integração
a = 0
b = 1

# Malha (Domínio)
x = np.linspace(a, b, 1000)

# Função f(x)
f = lambda x: 3 * x ** 2 - 6 * x ** 3

# Calculo da Integral
retantulo = retangle.integrate(f, a, b)
trapezio = trapezoidal.integrate(f, a, b)
regrasimpson = simpson1.integrate(f, a, b)
regrasimpson2 = simpson2.integrate(f, a, b)

# Print no CLI
print(f"Integrando f(x) usando a Regra do Retangulo, obtemos: {round(retantulo, 5)}")
print(f"\nIntegrando f(x) usando a Regra do Trapézio, obtemos: {round(trapezio, 5)}")
print(f"\nIntegrando f(x) usando a Primeira Regra de Simpson, obtemos: {round(regrasimpson, 5)}")
print(f"\nIntegrando f(x) usando a Segunda Regra de Simpson, obtemos: {round(regrasimpson2, 5)}")