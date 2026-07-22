import numpy as np

def integrate(math_function, a, b, N = 2):

    soma = 0
    gama = (b - a) / N
    ui = np.random.random(N)

    for i in range(0, N):
        xi = a + (b - a) * ui[i]
        soma += math_function(xi)
    
    area = soma * gama
    return area