import math
import matplotlib.pyplot as plt

def f(x):
    """The function f(x) = sin(x)."""
    return math.sin(x)

def known_derivative(x):
    """The known derivative of f(x) = sin(x) is cos(x)."""
    return math.cos(x)

def approx_derivative(x, h):
    """Finite difference approximation of f'(x)."""
    return (f(x + h) - f(x)) / h

def abs_error(approx, known):
    """Compute absolute error between approximation and known value."""
    return abs(approx - known)

def cleve_moler_epsilon():
    """Compute machine epsilon using the Cleve-Moler trick."""
    a = 4.0 / 3.0
    b = a - 1.0
    c = b + b + b
    return abs(1.0 - c)

def print_derivative_table_and_plot(x=1.0, max_power=30):
    """Prints the derivative table and plots h vs absolute error (log-log)."""
    true_val = known_derivative(x)
    hs = []
    errors = []

    # Print table header
    print(f"|{'h':^5}|{'x':^15}|{'Approx. f(x)':^15}|{'Known f(x)':^15}|{'Abs. Error':^15}|")
    print(f"|:---:|{'':->15}|{'':->15}|{'':->15}|{'':->15}|")

    for i in range(1, max_power + 1):
        h = 2 ** -i
        approx = approx_derivative(x, h)
        error = abs_error(approx, true_val)
        hs.append(h)
        errors.append(error)
        print(f"|2^-{i:02}|{x:15.8f}|{approx:15.8f}|{true_val:15.8f}|{error:15.8f}|")

    # Plot on log-log scale
    plt.figure(figsize=(8, 6))
    plt.loglog(hs, errors, marker='o', linestyle='-', color='blue')
    plt.xlabel('h (log scale)')
    plt.ylabel('Absolute Error (log scale)')
    plt.title('Finite Difference Approximation Error')
    plt.grid(True, which="both", ls="--")
    plt.savefig("error_plot.png")
    plt.show()

    return hs, errors

if __name__ == "__main__":
    eps = cleve_moler_epsilon()
    sqrt_eps = math.sqrt(eps)
    print(f"\nCleve-Moler epsilon: {eps:.20f}")
    print(f"Square root of epsilon: {sqrt_eps:.20f}\n")

    hs, errors = print_derivative_table_and_plot()

    min_error = min(errors)
    print(f"\nMinimum Absolute Error: {min_error:.20f}")
    print(f"Compare to sqrt(eps): {sqrt_eps:.20f}")
