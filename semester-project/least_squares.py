def least_squares_fit(x_vals, y_vals):
    """
    Compute least squares fit: y = c0 + c1 * x using A|b method.

    Args:
        x_vals: list of x values
        y_vals: list of y values

    Returns:
        (c0, c1): best-fit line coefficients
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("x and y lists must be the same length")

    n = len(x_vals)
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xx = sum(x * x for x in x_vals)
    sum_xy = sum(x * y for x, y in zip(x_vals, y_vals))

    denom = n * sum_xx - sum_x * sum_x
    if denom == 0:
        raise ValueError("Denominator in least squares computation is zero")

    c0 = (sum_y * sum_xx - sum_x * sum_xy) / denom
    c1 = (n * sum_xy - sum_x * sum_y) / denom

    return (c0, c1)
