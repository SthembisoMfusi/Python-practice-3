# Python Assessment Guide

Welcome to the Python Practice Assessment! This assessment is designed to test your skills in Data Structures, Data Manipulation, Recursion, and String Formatting across three levels of difficulty.

## Structure

The assessment is divided into three levels:

*   **Level 1 (Beginner)**: `level_1/assessment.py` - Basic concepts.
*   **Level 2 (Intermediate)**: `level_2/assessment.py` - Intermediate logic and data processing.
*   **Level 3 (Advanced)**: `level_3/assessment.py` - Advanced algorithms, custom classes, and complex recursion.

## How to Take the Assessment

1.  **Select a Level**: Start with Level 1 if you are new, or jump to a higher level if you feel confident.
2.  **Open the File**: Navigate to the folder of your chosen level (e.g., `level_1/assessment.py`).
3.  **Implement Functions**: You will see several functions with `pass` and docstrings explaining what to do. Replace `pass` with your code.
4.  **Run Tests**:
    *   Open your terminal.
    *   Run the tests for the specific level using `pytest`.

### Running Tests

To run tests for a specific level:

```bash
# Level 1
pytest level_1/tests/

# Level 2
pytest level_2/tests/

# Level 3
pytest level_3/tests/
```

To run all tests at once:

```bash
pytest
```

## Resetting the Assessment

If you want to start over, run the reset script:

```bash
python reset_assessment.py
```

This will clear your implementations in all `assessment.py` files while keeping the function signatures and docstrings intact.

Good luck!
