import sys

MANTISSA_DIGITS = 4 # Maximum number of digits after decimal in binary

def convert_integer_part(n):
    """
    Manually convert an integer part to binary.
    """
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n = n // 2
    return ''.join(reversed(bits))

def convert_fractional_part(frac):
    """
    Manually convert a fractional part to binary up to MANTISSA_DIGITS digits.
    """
    bits = []
    count = 0
    while frac > 0 and count < MANTISSA_DIGITS:
        frac *= 2
        if frac >= 1:
            bits.append("1")
            frac -= 1
        else:
            bits.append("0")
        count += 1
    return ''.join(bits) if bits else "0"

def decimal_to_binary(num):
    """
    Convert any real number to binary string.
    """
    if num == 0:
        return "0"

    sign = "-" if num < 0 else ""
    num = abs(num)

    integer_part = int(num)
    fractional_part = num - integer_part

    binary_int = convert_integer_part(integer_part)
    binary_frac = convert_fractional_part(fractional_part)

    if fractional_part == 0:
        return f"{sign}{binary_int}"
    else:
        return f"{sign}{binary_int}.{binary_frac}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 convert_dec_to_bin.py <number1> <number2> ...")
        sys.exit(1)

    inputs = [float(arg) for arg in sys.argv[1:]]

    print("| Base 10 | Base 2       |")
    print("| :------ | :----------- |")

    for num in inputs:
        binary = decimal_to_binary(num)
        print(f"| {num:<8}| {binary:<11}  |")

if __name__ == "__main__":
    main()
