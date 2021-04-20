import unittest

from simple_functions import circle_area, solve_quadratic
from math import pi, sqrt


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, 3 + 5j)
        self.assertRaises(TypeError, circle_area, "2")


class TestQuadratic(unittest.TestCase):
    def test_solve_quadratic(self):
        self.assertEqual(solve_quadratic(1, -5, 6), (3, 2))
        self.assertEqual(solve_quadratic(1, 2, 1), (-1, ))
        self.assertEqual(solve_quadratic(1, -2, -1), (1 + sqrt(2), 1 - sqrt(2)))

    def test_types(self):
        # Raise the correct errors if the input is the wrong type
        # or if the quadratic does not have real solutions
        self.assertRaises(TypeError, solve_quadratic, 3 + 1j, 2, 3)
        self.assertRaises(ValueError, solve_quadratic, 1, 1, 2)

if __name__ == '__main__':
    unittest.main()
