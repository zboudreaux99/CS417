import unittest
from convert_dec_to_any import convert_fractional_to_base, MAX_DIGITS

class TestConvertFractionalToBase(unittest.TestCase):
    def test_base2(self):
        # Base 2
        self.assertEqual(convert_fractional_to_base(0.5, 2), "0.1")
        self.assertEqual(convert_fractional_to_base(0.25, 2), "0.0;1")
        self.assertEqual(convert_fractional_to_base(0.75, 2), "0.1;1")

    def test_base10(self):
        # Base 10 (should be the same fractional digits as input's decimal places if no rounding)
        self.assertEqual(convert_fractional_to_base(0.5, 10), "0.5")
        self.assertEqual(convert_fractional_to_base(0.1, 10), "0.1")
        self.assertEqual(convert_fractional_to_base(0.01, 10), "0.0;1")

    def test_base60(self):
        # Base 60
        self.assertEqual(convert_fractional_to_base(0.5, 60), "0.30")
        self.assertEqual(convert_fractional_to_base(0.25, 60), "0.15")
        self.assertEqual(convert_fractional_to_base(0.75, 60), "0.45")
        self.assertEqual(convert_fractional_to_base(0.8, 60), "0.48")

        # This is a tricky one that was failing before because of rounding issues
        self.assertEqual(convert_fractional_to_base(0.16666, 60), "0.10")

    def test_zero_fraction(self):
        self.assertEqual(convert_fractional_to_base(0.0, 2), "0.0")
        self.assertEqual(convert_fractional_to_base(0.0, 60), "0.0")

    def test_max_digits_limit(self):
        # This test ensures output is no longer than MAX_DIGITS
        result = convert_fractional_to_base(0.1, 2)
        digits = result[2:].split(';')
        self.assertLessEqual(len(digits), MAX_DIGITS)

if __name__ == "__main__":
    unittest.main()
