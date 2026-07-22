import math
from differentiation import finites_differences

def approx_function(f, x, a = 1, n = 8):

    sum = f(a)
    derivative = f

    for i in range(1, n + 1):
        previous = derivative
        derivative = lambda x: finites_differences.central(previous, x)
        sum += derivative(a) / math.factorial(i) * (x - a) ** i

    return sum