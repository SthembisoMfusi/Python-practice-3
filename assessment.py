"""
Python Shape & Algorithm Assessment

Instructions:
- Complete the functions below.
- Each function should RETURN the final result as specified in the docstring.
  Do NOT use the print() function inside the functions you are implementing.
- For Part 2, you will likely need to create your own "helper" functions
  to solve the main problem.
- The `if __name__ == "__main__":` block at the end is for you to test your
  functions visually.

Learning Outcomes Tested:
- Understanding and implementing functions (including helper functions)
- Using 1D and 2D loops
- Applying control flow (if/else)
- Working with lists and strings (including string formatting/padding)
- Algorithmic problem-solving and decomposition
"""

# --- Part 1: Basic Shape Drawing ---

def draw_horizontal_line(length: int, char: str) -> str:
    """
    Draws a single horizontal line of a given length and character.

    Args:
        length (int): The number of characters in the line.
        char (str): The character to use for the line.

    Returns:
        str: A string representing the horizontal line.
    """
    # Your code here
    pass


def draw_solid_rectangle(width: int, height: int, char: str) -> list[str]:
    """
    Draws a solid rectangle of a given width, height, and character.

    Returns:
        list[str]: A list of strings, each representing a row of the rectangle.
    """
    # Your code here
    pass


def draw_hollow_rectangle(width: int, height: int, char: str) -> list[str]:
    """
    Draws a hollow rectangle. The border is made of `char`, and the inside
    is filled with spaces.

    Returns:
        list[str]: A list of strings representing the hollow rectangle.
    """
    # Your code here
    pass


# --- Part 2: Algorithmic & Mathematical Shapes ---

# --- Problem 1: Prime Number Triangle ---

# It is highly recommended to create a helper function, for example:
# def is_prime(n: int) -> bool:
#     ...

def draw_prime_triangle(height: int) -> list[str]:
    """
    Draws a right-angled triangle filled with consecutive prime numbers.

    The numbers must be right-aligned within each column for neatness. To do
    this, you must find the largest prime number that will be in the triangle,
    determine its width (how many digits it has), and then pad all other
    numbers with leading spaces to match that width.

    HINT: A good first step is to write a helper function to find all the
          primes you'll need. The triangle will contain (height * (height + 1)) / 2 numbers.

    Args:
        height (int): The number of rows in the triangle.

    Returns:
        list[str]: A list of strings, representing the formatted triangle.

    Example:
        >>> draw_prime_triangle(4)
        [
            ' 2',
            ' 3  5',
            ' 7 11 13',
            '17 19 23 29'
        ]
        (Note: The largest prime is 29, which has 2 digits. All other numbers
        are padded to a width of 2, e.g., ' 2', ' 3', ' 5', etc.)
    """
    # Your code here
    pass


# --- Problem 2: Square of Squares ---

def draw_square_of_squares(size: int) -> list[str]:
    """
    Draws a square grid of numbers. The numbers are the squares of consecutive
    integers, starting from 1 (1*1, 2*2, 3*3, ...).

    The numbers must be right-aligned. You will need to calculate the largest
    number that will appear in the grid (which is (size*size)^2), find its
    width, and pad all other numbers to match.

    Args:
        size (int): The width and height of the square grid.

    Returns:
        list[str]: A list of strings, representing the formatted square.

    Example:
        >>> draw_square_of_squares(3)
        [
            '  1   4   9',
            ' 16  25  36',
            ' 49  64  81'
        ]
        (Note: The largest number is 81. The largest number in a 3x3 grid
         would be the 9th square (3*3=9), which is 9*9=81. All numbers are
         padded to a width of 3 to align with ' 81' if a larger number were present,
         but here the max is 2.)
    """
    # Your code here
    pass


# --- Problem 3: Factorial Square ---

# It is highly recommended to create a helper function, for example:
# def factorial(n: int) -> int:
#     ...

def draw_factorial_square(size: int) -> list[str]:
    """
    Draws a square grid where each cell (row, col) contains the factorial
    of the sum of its 0-indexed coordinates (factorial(row + col)).

    The numbers must be right-aligned. You need to find the maximum value
    in the grid (which will be at the bottom-right corner), determine its
    string length, and pad all other numbers to match.

    Args:
        size (int): The width and height of the square grid.

    Returns:
        list[str]: A list of strings, representing the formatted square.

    Example:
        >>> draw_factorial_square(4)
        [
            '  1   1   2    6',
            '  1   2   6   24',
            '  2   6  24  120',
            '  6  24 120  720'
        ]
        (Note: Max value is factorial(3+3)=720, which has 3 digits. All
        numbers are padded to a width of 3, e.g., '  1', '  2', '  6'.)
    """
    # Your code here
    pass


# Helper function to print shapes for visual testing
def print_shape(shape_data):
    if isinstance(shape_data, str):
        print(shape_data)
    elif isinstance(shape_data, list):
        for row in shape_data:
            print(row)
    print("-" * 30)


# --- You can test your functions here ---
if __name__ == "__main__":
    print("--- Testing Part 1: Basic Shapes ---")
    print_shape(draw_hollow_rectangle(7, 5, '@'))

    print("--- Testing Part 2: Algorithmic Shapes ---")

    print("Prime Triangle (height=4)")
    print_shape(draw_prime_triangle(4))

    print("Square of Squares (size=3)")
    print_shape(draw_square_of_squares(3))

    print("Factorial Square (size=4)")
    print_shape(draw_factorial_square(4))