def integrate(f, a: float, b: float, c: float, d: float, nx: int = 256, ny: int = 256):

    soma = 0
    hx = (b - a) / nx
    hy = (d - c) / ny 

    for i in range(nx):
        xi = a + hx / 2 + i * hx

        for j in range(ny):
            yj = c + hy / 2 + j * hy
            soma += f(xi, yj)

    return hx * hy * soma