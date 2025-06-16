# Pattern Generator Assessment

## Overview

Welcome to the Pattern Generator assessment! The goal of this exercise is to complete a Python script that can draw various text-based patterns to the console. You will also implement a function to generate the Fibonacci sequence.

This assessment will test your understanding of:
- Functions and parameters
- User input and validation
- `for` and `while` loops
- Conditional logic (`if`/`elif`/`else`)
- Basic algorithms

---

## Files

- `assessment.py`: This is the **main file you need to edit**. It contains function stubs with `TODO` comments indicating where you need to write your code.
- `test_assessment.py`: This file contains a set of unit tests to help you check if your functions are working correctly. **Do not modify this file.**
- `reset_assessment.py`: A helper script. If you want to clear all your work and start over, you can run this script to restore `assessment.py` to its original, empty state.

---

## Instructions

1.  **Complete the Functions**: Open `assessment.py` and fill in the code for each function marked with a `TODO`. Read the docstrings carefully to understand what each function is supposed to do, its parameters, and what it should return or print.

2.  **Run Your Code**: To see your patterns in action, you can run the `assessment.py` file directly from your terminal. It will prompt you for a pattern name and a size.
    ```bash
    python assessment.py
    ```

3.  **Test Your Work**: To verify that your functions meet the requirements, run the unit tests from your terminal. This will give you a detailed report on which functions are passing and which are failing.
    ```bash
    python -m unittest test_assessment.py
    ```

4.  **Reset (Optional)**: If you want a clean slate, run the reset script.
    ```bash
    python reset_assessment.py
    ```

---

## Function Requirements

You need to implement the following functions in `assessment.py`:

-   `get_pattern()`: Prompt the user to enter a valid pattern name.
-   `get_size()`: Prompt the user to enter a valid integer size (1-50).
-   `draw_solid_rectangle(size)`: Draws a filled `size` x `size` rectangle.
-   `draw_hollow_square(size)`: Draws the outline of a `size` x `size` square.
-   `draw_right_triangle(size)`: Draws a right triangle with a height of `size`.
-   `draw_inverted_right_triangle(size)`: Draws an upside-down right triangle.
-   `draw_checkerboard(size)`: Draws a `size` x `size` checkerboard of 'X's and 'O's.
-   `draw_diamond(size)`: Draws a diamond shape where `size` is the height of the top half.
-   `draw(pattern, size)`: This function acts as a dispatcher. You must add `elif` blocks to call the correct drawing function based on the `pattern` string.
-   `fibonacci_sequence(n)`: A standalone function that returns a list containing the first `n` numbers of the Fibonacci sequence.

Good luck!