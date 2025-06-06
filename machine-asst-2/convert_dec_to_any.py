import sys

MAX_DIGITS = 8  # Max digits after base point
EPSILON = 1e-10  # Tolerance for floating-point comparison


def convert_fractional_to_base(frac, base):
    """
    Convert the fractional part of a decimal number to a given base.
    Returns a semicolon-separated digit string, limited to MAX_DIGITS.
    """
    digits = []
    count = 0
    while frac > EPSILON and count < MAX_DIGITS:
        frac *= base
        digit = int(round(frac))
        if digit >= base:
            digit = base - 1  # Cap digit to base-1 to avoid overflow
        digits.append(str(digit))
        frac -= digit
        if abs(frac) < EPSILON:
            break
        count += 1
    return "0." + ";".join(digits) if digits else "0.0"


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 convert_dec_to_any.py <base> <num1> <num2> ...")
        sys.exit(1)

    base = int(sys.argv[1])
    numbers = [float(arg) for arg in sys.argv[2:]]

    print(f"| Base 10 | Base {base} |")
    print(f"| :------ | :------ |")

    for num in numbers:
        converted = convert_fractional_to_base(num, base)
        print(f"| {num:<7} | {converted:<7} |")


if __name__ == "__main__":
    main()
