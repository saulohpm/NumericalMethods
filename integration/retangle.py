def integrate(math_function, a, b, n = 100):

    soma = 0
    L = b - a
    deltax = L / n

    for i in range(1, n + 1):
        k = a + i * deltax
        soma += math_function(k)
    
    area = soma * deltax
    return area