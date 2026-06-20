def integrate(f, a, b, n = 100):

    if n % 3 != 0:
        raise ValueError("ERRO: 'n' deve ser múltiplo de 3 para Simpson 3/8")
    
    soma = 0
    L = b - a
    deltax = L / n

    for i in range(0, n - 2, 3):
        zeta1 = a + i * deltax
        zeta2 = a + (i + 1) * deltax
        zeta3 = a + (i + 2) * deltax
        zeta4 = a + (i + 3) * deltax
        soma += f(zeta1) + 3 * f(zeta2) + 3 * f(zeta3) + f(zeta4)
    
    area = soma * 3 * deltax / 8
    return area