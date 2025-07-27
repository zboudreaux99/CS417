from least_squares import least_squares_fit

def write_core_interpolation_file(x_vals, y_vals_core, core_idx, base_filename):
    """
    Write a file containing piecewise linear interpolation + least-squares for a single core.
    """
    lines = []

    for i in range(len(x_vals) - 1):
        x0, x1 = x_vals[i], x_vals[i + 1]
        y0, y1 = y_vals_core[i], y_vals_core[i + 1]

        m = (y1 - y0) / (x1 - x0)
        b = y0 - m * x0

        line = f"{x0:>5.0f} <= x <= {x1:<5.0f} ; y = {b:11.4f} + {m:11.4f} x ; interpolation"
        lines.append(line)

    c0, c1 = least_squares_fit(x_vals, y_vals_core)
    x_min, x_max = x_vals[0], x_vals[-1]
    lsq_line = f"{x_min:>5.0f} <= x <= {x_max:<5.0f} ; y = {c0:11.4f} + {c1:11.4f} x ; least-squares"
    lines.append(lsq_line)

    filename = f"{base_filename}-core-{core_idx:02}.txt"
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + "\n")

def write_all_interpolations(x_vals, y_vals, base_filename):
    """
    Writes interpolation + least-squares files for all cores.
    """
    num_cores = len(y_vals[0])
    for core_idx in range(num_cores):
        y_vals_core = [row[core_idx] for row in y_vals]
        write_core_interpolation_file(x_vals, y_vals_core, core_idx, base_filename)
