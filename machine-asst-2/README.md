# Machine Assignment 2 - Decimal to Any Base
This Python script converts the *fractional part* of decimal (base 10) numbers into any specified base, producing a semicolon-separated digit string for the fraction. The conversion is done manually.

---

## Features
- Converts fractional parts of positive and negative decimal numbers to any base.
- Supports any base input
- Limits output to 8 fractional digits (configurable via `MAX_DIGITS`).
- Command-line interface for batch conversions.
- Outputs fractional digits separated by semicolons (e.g., `0.10;35;59`).

---

## How It Works
- **Fractional Conversion**: Repeatedly multiplies the fractional part by the target base, extracting integer digits at each step.
- **Rounding and Truncation**: Stops after 8 digits or when the fraction is close enough to zero to avoid floating-point errors.

---

## Usage
```bash
python3 convert_dec_to_any.py 60 0.5 0.25 0.75 0.8 0.16666
```

#### Example Output
```bash
| Base 10 | Base 60 |
| :------ | :------ |
| 0.5     | 0.30    |
| 0.25    | 0.15    |
| 0.75    | 0.45    |
| 0.8     | 0.48    |
| 0.16666 | 0.10    |
```

## Testing
```bash
python3 test_dec_to_any.py
```