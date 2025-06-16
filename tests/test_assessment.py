# test_assessment.py

import unittest
import io
import sys
from assessment import (
    draw_solid_rectangle,
    draw_hollow_square,
    draw_right_triangle,
    draw_inverted_right_triangle,
    draw_checkerboard,
    draw_diamond,
    fibonacci_sequence
)

class TestPatternGenerator(unittest.TestCase):

    def setUp(self):
        """Redirect stdout to capture print statements."""
        self.held_stdout = sys.stdout
        sys.stdout = self.captured_output = io.StringIO()

    def tearDown(self):
        """Restore stdout."""
        sys.stdout = self.held_stdout

    def test_draw_solid_rectangle(self):
        draw_solid_rectangle(4)
        output = self.captured_output.getvalue()
        expected = "****\n****\n****\n****\n"
        self.assertEqual(output, expected)

    def test_draw_hollow_square(self):
        draw_hollow_square(5)
        output = self.captured_output.getvalue()
        expected = "*****\n*   *\n*   *\n*   *\n*****\n"
        self.assertEqual(output, expected)

    def test_draw_right_triangle(self):
        draw_right_triangle(4)
        output = self.captured_output.getvalue()
        expected = "*\n**\n***\n****\n"
        self.assertEqual(output, expected)

    def test_draw_inverted_right_triangle(self):
        draw_inverted_right_triangle(4)
        output = self.captured_output.getvalue()
        expected = "****\n***\n**\n*\n"
        self.assertEqual(output, expected)

    def test_draw_checkerboard(self):
        draw_checkerboard(5)
        output = self.captured_output.getvalue()
        expected = "XOXOX\nOXOXO\nXOXOX\nOXOXO\nXOXOX\n"
        self.assertEqual(output, expected)

    def test_draw_diamond(self):
        draw_diamond(4)
        output = self.captured_output.getvalue()
        expected = (
            "   *\n"
            "  ***\n"
            " *****\n"
            "*******\n"
            " *****\n"
            "  ***\n"
            "   *\n"
        )
        self.assertEqual(output, expected)

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1])
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])


if __name__ == '__main__':
    unittest.main(verbosity=2)