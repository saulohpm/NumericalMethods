def integrate(math_function, a, b, n = 100):

    soma = 0
    L = b - a
    deltax = L / n

    for i in range(0, n):
        k1 = a + i * deltax
        k2 = a + (i + 1) * deltax
        soma += math_function(k1) + (1 / 2) * (math_function(k2) - math_function(k1))
    
    area = soma * deltax
    return area