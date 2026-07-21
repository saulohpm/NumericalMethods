def forward(f, x0, deltax):
    return (f(x0 + deltax) - f(x0)) / deltax

def backward(f, x0, deltax):
    return (f(x0) - f(x0 - deltax)) / deltax

def central(f, x0, deltax):
    return (f(x0 + deltax) - f(x0 - deltax)) / (2 * deltax)