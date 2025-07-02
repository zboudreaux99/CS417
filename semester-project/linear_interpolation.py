def linear_interpolate(x_vals, y_vals, x_query):
    """
    Perform piecewise linear interpolation.

    Args:
        x_vals: list of time values (must be sorted and unique)
        y_vals: list of corresponding temperature lists
        x_query: the time at which to estimate temperature

    Returns:
        A list of interpolated core temperatures at x_query
    """
    if x_query < x_vals[0] or x_query > x_vals[-1]:
        raise ValueError("Query time is out of bounds")

    # Find the interval [x_k, x_k+1] that contains x_query
    for k in range(len(x_vals) - 1):
        if x_vals[k] <= x_query <= x_vals[k + 1]:
            x0, x1 = x_vals[k], x_vals[k + 1]
            y0, y1 = y_vals[k], y_vals[k + 1]

            # Interpolate for each core
            interpolated = []
            for i in range(len(y0)):
                m = (y1[i] - y0[i]) / (x1 - x0)
                b = y0[i] - m * x0
                y = b + m * x_query
                interpolated.append(y)

            return interpolated

    raise ValueError("No interval found (unexpected error)")

def write_interpolation_files(x_vals, y_vals, base_filename="output"):
    """
    Generate and write interpolation equations to one file per core.

    Args:
        x_vals: list of time values (sorted)
        y_vals: list of core temperature lists (each sublist is temps at that time)
        base_filename: prefix for the output files (e.g., sample-input)
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("Time and temperature lists must be the same length")

    num_cores = len(y_vals[0])
    core_outputs = [[] for _ in range(num_cores)]

    for i in range(len(x_vals) - 1):
        x0 = x_vals[i]
        x1 = x_vals[i + 1]
        for core in range(num_cores):
            y0 = y_vals[i][core]
            y1 = y_vals[i + 1][core]

            m = (y1 - y0) / (x1 - x0)
            b = y0 - m * x0

            line = f"{x0:>4.0f} <= x <= {x1:<4.0f} ; y = {b:7.4f} + {m:+7.4f} x ; interpolation"
            core_outputs[core].append(line)

    for core_idx, lines in enumerate(core_outputs):
        filename = f"{base_filename}-core-{core_idx:02}.txt"
        with open(filename, 'w') as f:
            for line in lines:
                f.write(line + "\n")