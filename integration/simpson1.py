def integrate(f, a, b, n = 100):

    if n % 2 != 0:
        raise ValueError("ERRO: 'n' deve ser par para a Regra de Simpson")
    
    else:
        soma = 0
        L = b - a
        deltax = L / n

        for i in range(0, n - 1, 2):
            zeta1 = a + i * deltax
            zeta2 = a + (i + 1) * deltax
            zeta3 = a + (i + 2) * deltax
            soma += f(zeta1) + 4 * f(zeta2) + f(zeta3)
        
        area = soma * deltax / 3
        return area