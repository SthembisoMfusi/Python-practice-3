
import unittest
import assessment
# --- Helper function tests---
# We test for expected helper functions.
# This encourages good practice in terms of modulating your code.

class TestHelperFunctions(unittest.TestCase):
    def test_is_prime(self):
        # checks to see if students created a helper function named 'is_prime'
        if hasattr(assessment, 'is_prime'):
            self.assertFalse(assessment.is_prime(0))
            self.assertFalse(assessment.is_prime(1))
            self.assertTrue(assessment.is_prime(2))
            self.assertTrue(assessment.is_prime(3))
            self.assertFalse(assessment.is_prime(4))
            self.assertTrue(assessment.is_prime(29))
            self.assertFalse(assessment.is_prime(30))

    def test_factorial(self):
        # checks to see if students created a helper function named 'factorial'
        if hasattr(assessment, 'factorial'):
            self.assertEqual(assessment.factorial(0), 1)
            self.assertEqual(assessment.factorial(1), 1)
            self.assertEqual(assessment.factorial(4), 24)
            self.assertEqual(assessment.factorial(6), 720)


class TestShapeDrawing(unittest.TestCase):

    # --- Part 1 Tests ---
    def test_draw_horizontal_line(self):
        self.assertEqual(assessment.draw_horizontal_line(5, '*'), '*****')
        self.assertEqual(assessment.draw_horizontal_line(0, '$'), '')

    def test_draw_solid_rectangle(self):
        expected = ['*****', '*****', '*****']
        self.assertEqual(assessment.draw_solid_rectangle(5, 3, '*'), expected)
        self.assertEqual(assessment.draw_solid_rectangle(5, 0, '*'), [])

    def test_draw_hollow_rectangle(self):
        expected = ['######', '#    #', '#    #', '######']
        self.assertEqual(assessment.draw_hollow_rectangle(6, 4, '#'), expected)

    # --- Part 2 Tests ---
    def test_draw_prime_triangle(self):
        # Test case from docstring
        expected_h4 = [
            ' 2',
            ' 3  5',
            ' 7 11 13',
            '17 19 23 29'
        ]
        self.assertEqual(assessment.draw_prime_triangle(4), expected_h4)

        # Edge case: height = 1
        self.assertEqual(assessment.draw_prime_triangle(1), ['2'])

        # Edge case: height = 0
        self.assertEqual(assessment.draw_prime_triangle(0), [])

        # Test case: height = 2
        expected_h2 = [
            '2',
            '3 5'
        ]
        self.assertEqual(assessment.draw_prime_triangle(2), expected_h2)

    def test_draw_square_of_squares(self):
        # Test case from docstring
        expected_s3 = [
            '  1   4   9',
            ' 16  25  36',
            ' 49  64  81'
        ]
        self.assertEqual(assessment.draw_square_of_squares(3), expected_s3)

        # Edge case: size = 1
        self.assertEqual(assessment.draw_square_of_squares(1), ['1'])

        # Edge case: size = 0
        self.assertEqual(assessment.draw_square_of_squares(0), [])

        expected_s2 = [
            '  1   4',
            '  9  16'
        ]
        self.assertEqual(assessment.draw_square_of_squares(2), expected_s2)

    def test_draw_factorial_square(self):
        # Test case from docstring
        expected_s4 = [
            '  1   1   2    6',
            '  1   2   6   24',
            '  2   6  24  120',
            '  6  24 120  720'
        ]
        self.assertEqual(assessment.draw_factorial_square(4), expected_s4)

        # Edge case: size = 1
        self.assertEqual(assessment.draw_factorial_square(1), ['1'])

        # Edge case: size = 0
        self.assertEqual(assessment.draw_factorial_square(0), [])

        # Test case: size = 2
        expected_s2 = [
            '1 1',
            '1 2'
        ]
        self.assertEqual(assessment.draw_factorial_square(2), expected_s2)


if __name__ == '__main__':
    # To run the tests, execute `python -m unittest test_assessment.py` in your terminal
    unittest.main()