# Machine Assignment 1 - Decimal to Binary Converter
This is a Python script that manually converts decimal (Base 10) numbers into binary (Base 2) format, including both the integer and fractional parts.

---

## Features
- Converts both positive and negative real numbers to binary.
- Handles integers, fractions, and mixed numbers.
- Limits the mantissa to 4 binary digits (configurable).
- Command-line interface for batch conversions.

---

## How It Works
- **Integer Conversion**: Uses repeated division by 2.
- **Fractional Conversion**: Uses repeated multiplication by 2, capturing the integer part.
- **Truncation**: Fractional binary digits are truncated after 4 digits.

---

## Usage
```bash
python3 convert_dec_to_bin.py 5 3.25 -0.5 0.1
```

## Testing
```bash
python3 test_dec_to_bin.py
```