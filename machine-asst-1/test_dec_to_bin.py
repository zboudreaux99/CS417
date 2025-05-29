import unittest
from convert_dec_to_bin import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), "0")

    def test_positive_integer(self):
        self.assertEqual(decimal_to_binary(5), "101")
        self.assertEqual(decimal_to_binary(1), "1")
        self.assertEqual(decimal_to_binary(16), "10000")

    def test_negative_integer(self):
        self.assertEqual(decimal_to_binary(-3), "-11")
        self.assertEqual(decimal_to_binary(-1), "-1")

    def test_positive_fraction(self):
        self.assertEqual(decimal_to_binary(0.5), "0.1")
        self.assertEqual(decimal_to_binary(0.25), "0.01")
        self.assertEqual(decimal_to_binary(0.75), "0.11")

    def test_negative_fraction(self):
        self.assertEqual(decimal_to_binary(-0.5), "-0.1")
        self.assertEqual(decimal_to_binary(-0.25), "-0.01")

    def test_mixed_numbers(self):
        self.assertEqual(decimal_to_binary(5.25), "101.01")
        self.assertEqual(decimal_to_binary(-2.75), "-10.11")

    def test_truncation(self):
        # Should only show up to 4 digits after decimal
        self.assertEqual(decimal_to_binary(0.1), "0.0001")
        self.assertEqual(decimal_to_binary(0.3), "0.0100")

if __name__ == '__main__':
    unittest.main()
