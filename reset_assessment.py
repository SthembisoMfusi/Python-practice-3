
# This script resets the assessment.py file to its original state.
# Run this script if you want to clear your answers and start over.

import os

# The original content of the assessment.py file
assessment_template = """
# TODO: return pattern name from user input (it can't be blank and must be a valid pattern!)
def get_pattern()-> str:
    \"\"\"
    Prompts the user to enter a pattern name from a predefined list.
    The function will keep asking until a valid pattern name is entered.
    Valid patterns are: 'solid_rectangle', 'hollow_square', 'right_triangle', 
    'inverted_right_triangle', 'checkerboard', 'diamond'.
    \"\"\"
    
    return ""


# TODO: return size from user input (it must be an int!)
#       The maximum possible size must be 50.
def get_size()->int:
    \"\"\"
    Prompts the user to enter a size for the pattern.
    The function will ensure the input is an integer between 1 and 50.
    It will keep asking until a valid size is entered.
    \"\"\"
    
    return 0


# TODO: Complete the required pattern functions below
#       with reference to the unittests.

def draw_solid_rectangle(size: int) -> None:
    \"\"\"
    Draws a solid rectangle of asterisks (*) with the given size as both height and width.
    
    Parameters:
        size (int): The height and width of the rectangle. Must be a positive integer.
        
    Returns:
        None: Prints the rectangle pattern directly to the console.
        
    Example for size = 4:
    ****
    ****
    ****
    ****
    \"\"\"
    pass

def draw_hollow_square(size: int) -> None:
    \"\"\"
    Draws a hollow square pattern of asterisks (*) with the given size.
    Only the border of the square should be printed.
    
    Parameters:
        size (int): The height and width of the square. Must be a positive integer.
        
    Returns:
        None: Prints the hollow square pattern directly to the console.

    Example for size = 5:
    *****
    *   *
    *   *
    *   *
    *****
    \"\"\"
    pass

def draw_right_triangle(size: int) -> None:
    \"\"\"
    Draws a right-aligned triangle of asterisks (*).
    
    Parameters:
        size (int): The height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the triangle pattern directly to the console.

    Example for size = 4:
    *
    **
    ***
    ****
    \"\"\"
    pass

def draw_inverted_right_triangle(size: int) -> None:
    \"\"\"
    Draws an inverted right-aligned triangle of asterisks (*).
    
    Parameters:
        size (int): The starting height of the triangle. Must be a positive integer.
        
    Returns:
        None: Prints the inverted triangle pattern directly to the console.

    Example for size = 4:
    ****
    ***
    **
    *
    \"\"\"
    pass

def draw_checkerboard(size: int) -> None:
    \"\"\"
    Draws a checkerboard pattern of 'X' and 'O' characters.
    The top-left character should always be 'X'.
    
    Parameters:
        size (int): The height and width of the checkerboard. Must be a positive integer.
        
    Returns:
        None: Prints the checkerboard pattern directly to the console.

    Example for size = 5:
    XOXOX
    OXOXO
    XOXOX
    OXOXO
    XOXOX
    \"\"\"
    pass

def draw_diamond(size: int) -> None:
    \"\"\"
    Draws a diamond shape made of asterisks (*).
    The size determines the widest point of the diamond.
    
    Parameters:
        size (int): The height of the top half of the diamond. Must be a positive integer.
        
    Returns:
        None: Prints the diamond pattern directly to the console.

    Example for size = 4:
       *
      ***
     *****
    *******
     *****
      ***
       *
    \"\"\"
    pass

# TODO: Add support for calling the correct drawing function based on the 'pattern' string.
def draw(pattern: str, size: int) -> None:
    \"\"\"
    Main drawing function that calls the appropriate pattern-specific drawing function.
    
    Parameters:
        pattern (str): The type of pattern to draw.
        size (int): The size of the pattern.
        
    Returns:
        None: Prints the requested pattern directly to the console.
    \"\"\"
    if pattern == "solid_rectangle":
        draw_solid_rectangle(size)
    # Add other patterns here...


# TODO: (Standalone function) - Solve the Fibonacci Sequence
def fibonacci_sequence(n: int) -> list:
    \"\"\"
    Generates the Fibonacci sequence up to the n-th term.

    The Fibonacci sequence is a series of numbers where each number is the sum of the
    two preceding ones, usually starting with 0 and 1.
    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    Parameters:
        n (int): The number of terms to generate in the sequence.
                 If n is 0, return an empty list.
                 If n is 1, return [0].
                 If n is 2, return [0, 1].

    Returns:
        list: A list containing the first n Fibonacci numbers.
    \"\"\"
    return []


if __name__ == "__main__":
    print("--- Pattern Generator ---")
    pattern_param = get_pattern()
    size_param = get_size()
    if pattern_param and size_param > 0:
        print(f"\\nDrawing a '{pattern_param}' of size {size_param}:\\n")
        draw(pattern_param, size_param)
    
    #Example for testing Fibonacci
    print("\\n--- Fibonacci Sequence ---")
    fib_terms = 10
    print(f"The first {fib_terms} terms are: {fibonacci_sequence(fib_terms)}")
"""

def main():
    """Writes the template content to assessment.py."""
    try:
        with open("assessment.py", "w") as f:
            f.write(assessment_template)
        print("✅ Success: 'assessment.py' has been reset to its original state.")
        print("You can now start the assessment from scratch.")
    except IOError as e:
        print(f"❌ Error: Could not write to file 'assessment.py'.")
        print(f"Details: {e}")

if __name__ == "__main__":
    main()