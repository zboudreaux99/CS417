import unittest
import math
from derivation import f, known_derivative, approx_derivative, abs_error

class TestFiniteDifference(unittest.TestCase):
    def test_known_derivative(self):
        """Test that the known derivative is correctly computed as cos(1)."""
        self.assertAlmostEqual(known_derivative(1.0), math.cos(1.0), places=10)

    def test_approximation_converges(self):
        """Test that as h decreases, the approximation gets closer to the true derivative up to a point."""
        x = 1.0
        true_val = known_derivative(x)
        h_values = [2**-i for i in range(1, 10)]  # Smaller h → better accuracy

        prev_error = None
        for h in h_values:
            approx = approx_derivative(x, h)
            error = abs_error(approx, true_val)
            if prev_error is not None:
                self.assertLessEqual(error, prev_error + 1e-10)  # Allow small float wiggle
            prev_error = error

    def test_abs_error_function(self):
        """Test that abs_error returns the correct absolute difference."""
        self.assertEqual(abs_error(5.0, 3.0), 2.0)
        self.assertEqual(abs_error(3.0, 5.0), 2.0)
        self.assertEqual(abs_error(-1.0, 1.0), 2.0)

    def test_extremely_small_h(self):
        """Test behavior with extremely small h"""
        x = 1.0
        h = 2**-30
        approx = approx_derivative(x, h)
        true_val = known_derivative(x)
        error = abs_error(approx, true_val)

        self.assertLess(error, 1e-5)

if __name__ == '__main__':
    unittest.main()