import numpy as np
from numpy.polynomial.legendre import leggauss

def integrate(f, a, b, n=5):

    r, w = leggauss(n)
    #r = (r1​,r2​,…,rn​)
    #w = (W1​,W2​,…,Wn​)

    soma = 0.0

    for i in range(n):
        x = (b - a)/2 * r[i] + (a + b)/2
        soma += w[i] * f(x)

    return (b - a)/2 * soma