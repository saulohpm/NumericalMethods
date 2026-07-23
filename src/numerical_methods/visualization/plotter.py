import matplotlib.pyplot as plt

def plot_function(f, x, a = None, b = None, f2 = None):
    """
    Plot a function, optionally shading the area under the curve between
    a and b, or overlaying a second function (e.g. a Fourier approximation).

    Parameters
    ----------
    f : callable
        Function to plot. Must accept an array-like x and return an
        array-like y.
    x : array_like
        Array of x-values over which f is evaluated and plotted.
    a : float, optional
        Lower bound used to shade the area under the curve (default None).
    b : float, optional
        Upper bound used to shade the area under the curve (default None).
    f2 : array_like, optional
        Precomputed y-values of a second function to overlay on the same
        plot, e.g. a Fourier series approximation (default None).

    Returns
    -------
    None
        Displays the plot; does not return a value.
    """
    
    y = f(x)

    plt.figure(figsize=(14,6))

    if a is not None and b is not None and f2 is None:
        plt.plot(x, y, color='blue')
        plt.fill_between(x, y, alpha=0.3)

        plt.title("Definite Integral")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.xlim(a, b)
        plt.ylim(0, float(f(b)))

    elif a is None and b is None and f2 is None:
        raise ValueError("ERROR: a and b and f2 cannot be None")

    else:
        plt.title(f"Interactions using fourier series")
        plt.plot(x, y, label='f(x)')
        plt.plot(x, f2, label='Fourier')
        
    plt.legend()
    plt.grid(True, alpha=0.75)

    plt.show()