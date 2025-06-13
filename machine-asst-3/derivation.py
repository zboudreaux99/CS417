import math

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

def print_derivative_table(x=1.0, max_power=30):
    """Prints the finite difference table for f(x) = sin(x) at x = 1."""
    true_val = known_derivative(x)

    # Table header
    print(f"|{'h':^5}|{'x':^15}|{'Approx. f(x)':^15}|{'Known f(x)':^15}|{'Abs. Error':^15}|")
    print(f"|:---:|{'':->15}|{'':->15}|{'':->15}|{'':->15}|")

    for i in range(1, max_power + 1):
        h = 2 ** -i
        approx = approx_derivative(x, h)
        error = abs_error(approx, true_val)
        print(f"|2^-{i:02}|{x:15.8f}|{approx:15.8f}|{true_val:15.8f}|{error:15.8f}|")

if __name__ == "__main__":
    print_derivative_table()
