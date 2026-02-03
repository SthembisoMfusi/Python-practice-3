def censor_text(text: str, forbidden_word: str) -> str:
    """
    Replaces a specific word in text with asterisks.
    
    String replacement is a core text processing task.
    You need to find a substring and swap it out.
    
    Goal: Replace all occurrences of 'forbidden_word' with '****'.
    """
    pass

def invert_dict_unique(d: dict) -> dict:
    """
    Inverts a dictionary assuming unique values.
    
    If you know values are unique, you don't need lists for the values.
    
    Goal: Return a dict where keys are the original values and values are keys.
          Assume d = {'a': 1, 'b': 2} -> {1: 'a', 2: 'b'}.
    """
    pass

def group_words_by_length(words: list) -> dict:
    """
    Groups a list of words by their length.
    
    This is a specific practical grouping task.
    
    Goal: Return a dict where keys are integers (lengths) and values are lists of words.
          e.g. ["cat", "dog", "at"] -> {3: ["cat", "dog"], 2: ["at"]}
    """
    pass

def fibonacci_recursive(n: int) -> int:
    """
    Calculates the Nth Fibonacci number recursively.
    
    Moved from Level 2. This is a standard recursion test.
    
    Goal: Return fib(n-1) + fib(n-2). Base cases: fib(0)=0, fib(1)=1.
    """
    pass

def validate_password(password: str) -> bool:
    """
    Checks if a password meets simple security criteria.
    
    Instead of regex, use logical checks (loops, string methods).
    
    Goal: Return True if length >= 8 and it contains at least one digit. 
    """
    pass

class Queue:
    """
    Implements a Queue data structure (FIFO).
    
    First In, First Out. Like a line at a store.
    
    Goal: Implement enqueue (add to back), dequeue (remove from front), and is_empty.
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to rear."""
        pass
    
    def dequeue(self):
        """Remove and return item from front. Return None if empty."""
        pass

    def is_empty(self) -> bool:
        """Return True if empty."""
        pass

def sum_matrix(matrix: list) -> int:
    """
    Calculates the sum of all numbers in a 2D matrix (list of lists).
    
    Requires nested loops to traverse rows and columns.
    
    Goal: Return the total sum of all elements.
    """
    pass

def recursive_nested_sum(nested_list: list) -> int:
    """
    Sums all numbers in a nested list of arbitrary depth.
    
    e.g. [1, [2, 3], 4].
    When encountering a list, recurse. When encountering a number, add it.
    
    Goal: Return the total sum.
    """
    pass

class Student:
    """
    A simple class representing a student.
    
    Classes group data (attributes) and behavior (methods).
    
    Goal: 
    1. __init__: store name and grades (list).
    2. average_grade(): return the average of grades. Return 0 if no grades.
    """
    def __init__(self, name: str, grades: list):
        pass
    
    def average_grade(self) -> float:
        pass

def check_parentheses_simple(s: str) -> bool:
    """
    Checks if parentheses '()' are balanced.
    
    You don't need a full stack for just one type. A simple counter works:
    +1 for '(', -1 for ')'. If counter goes negative, invalid. If not 0 at end, invalid.
    
    Goal: Return True if balanced.
    """
    pass
