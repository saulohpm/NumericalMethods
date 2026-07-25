from .finite_differences import central

def calculate(f, x0, h):

    Dh = central(f, x0, h)
    Dh_half = central(f, x0, h / 2)

    Dr = (4 * Dh_half - Dh) / 3

    return Dr