import unittest
import math
from finite_difference import f, known_derivative, approx_derivative, abs_error, cleve_moler_epsilon

class TestFiniteDifference(unittest.TestCase):
    """Test suite for finite difference approximation functions."""

    def test_f_function(self):
        """Test the f(x) = sin(x) function."""
        self.assertAlmostEqual(f(0), 0.0, places=10)
        self.assertAlmostEqual(f(math.pi/2), 1.0, places=10)
        self.assertAlmostEqual(f(math.pi), 0.0, places=10)
        self.assertAlmostEqual(f(3*math.pi/2), -1.0, places=10)
        self.assertAlmostEqual(f(2*math.pi), 0.0, places=10)

    def test_known_derivative(self):
        """Test the known derivative cos(x)."""
        self.assertAlmostEqual(known_derivative(0), 1.0, places=10)
        self.assertAlmostEqual(known_derivative(math.pi/2), 0.0, places=10)
        self.assertAlmostEqual(known_derivative(math.pi), -1.0, places=10)
        self.assertAlmostEqual(known_derivative(3*math.pi/2), 0.0, places=10)
        self.assertAlmostEqual(known_derivative(2*math.pi), 1.0, places=10)

    def test_approx_derivative_basic(self):
        """Test finite difference approximation with known cases."""
        # Test at x=0 where derivative should be 1
        h = 0.01
        approx = approx_derivative(0, h)
        expected = known_derivative(0)
        self.assertAlmostEqual(approx, expected, places=2)
        
        # Test at x=pi/2 where derivative should be 0
        approx = approx_derivative(math.pi/2, h)
        expected = known_derivative(math.pi/2)
        self.assertAlmostEqual(approx, expected, places=2)

    def test_approx_derivative_convergence(self):
        """Test that approximation improves as h gets smaller."""
        x = 1.0
        true_val = known_derivative(x)
        
        h1 = 0.1
        h2 = 0.01
        h3 = 0.001
        
        error1 = abs(approx_derivative(x, h1) - true_val)
        error2 = abs(approx_derivative(x, h2) - true_val)
        error3 = abs(approx_derivative(x, h3) - true_val)
        
        # Errors should generally decrease (until round-off dominates)
        self.assertLess(error2, error1)
        self.assertLess(error3, error2)

    def test_approx_derivative_edge_cases(self):
        """Test edge cases for finite difference."""
        # Very small h
        result = approx_derivative(1.0, 1e-15)
        self.assertIsInstance(result, float)
        self.assertFalse(math.isnan(result))
        
        # Zero x
        result = approx_derivative(0.0, 0.01)
        self.assertIsInstance(result, float)
        self.assertFalse(math.isnan(result))

    def test_abs_error(self):
        """Test absolute error calculation."""
        self.assertEqual(abs_error(5.0, 3.0), 2.0)
        self.assertEqual(abs_error(3.0, 5.0), 2.0)
        self.assertEqual(abs_error(5.0, 5.0), 0.0)
        self.assertEqual(abs_error(-3.0, 2.0), 5.0)
        self.assertEqual(abs_error(2.0, -3.0), 5.0)

    def test_cleve_moler_epsilon(self):
        """Test Cleve-Moler epsilon calculation."""
        eps = cleve_moler_epsilon()
        
        self.assertGreater(eps, 0) # Should be positive
        
        self.assertLess(eps, 1e-10) # Should be small (typically around machine epsilon)
        
        eps2 = cleve_moler_epsilon()
        self.assertEqual(eps, eps2) # Should be consistent across calls

    def test_mathematical_consistency(self):
        """Test mathematical consistency between functions."""
        x = 1.5
        h = 0.001
        
        # The finite difference should approximate the known derivative
        approx = approx_derivative(x, h)
        known = known_derivative(x)
        error = abs_error(approx, known)
        
        self.assertLess(error, 0.01) # Error should be small for reasonable h
        
        error2 = abs(approx - known)
        self.assertEqual(error, error2) # The error calculated two ways should be the same

    def test_function_domains(self):
        """Test functions work across their expected domains."""
        test_points = [0, math.pi/4, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi, -math.pi/2]
        
        for x in test_points:
            # All functions should return finite values
            f_val = f(x)
            deriv_val = known_derivative(x)
            approx_val = approx_derivative(x, 0.01)
            
            self.assertFalse(math.isnan(f_val))
            self.assertFalse(math.isnan(deriv_val))
            self.assertFalse(math.isnan(approx_val))
            self.assertFalse(math.isinf(f_val))
            self.assertFalse(math.isinf(deriv_val))
            self.assertFalse(math.isinf(approx_val))

if __name__ == '__main__':
    # Run the tests
    unittest.main()