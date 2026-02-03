
import os

# Level 1 Template
level_1_content = r'''def greeting_generator(name: str, age: int) -> str:
    """
    Constructs a personalized greeting message.
    
    This function demonstrates string formatting, which is essential for creating
    dynamic messages based on user input. You need to combine the static parts of
    the string with the variable values provided as arguments.
    
    Goal: Return a string in the format "Hello {name}, you are {age} years old!".
    """
    pass

def get_first_and_last(numbers: list) -> list:
    """
    Extracts the boundary elements of a list.
    
    Accessing elements at specific positions (indices) is a fundamental operation in
    list manipulation. This function asks you to identify and isolate the
    beginning and end of a sequence.
    
    Goal: Return a new list containing only the first and last elements.
          Handle the edge case where the list might be empty.
    """
    pass

def filter_even_numbers(numbers: list) -> list:
    """
    Filters a list to keep only elements satisfying a specific condition.
    
    Data processing often involves selecting a subset of data. Here, the condition
    is mathematical (parity). You'll need to iterate through the input and
    decide which elements to keep.
    
    Goal: Return a new list containing only the even numbers from the input.
    """
    pass

def factorial_recursive(n: int) -> int:
    """
    Computes the factorial of a number using recursion.
    
    Recursion is a technique where a function calls itself to solve a smaller instance
    of the problem. Factorial (n!) is a classic example: 5! = 5 * 4!
    
    Goal: Calculate n * (n-1) * ... * 1. 
          The base case is 0! = 1.
    """
    pass

def get_value_from_dict(d: dict, key: str):
    """
    Retrieves a value from a dictionary safely.
    
    Dictionaries are key-value stores. Accessing them is common, but you must handle
    cases where the key doesn't exist to avoid program crashes.
    
    Goal: Return the value for the given key. If the key is missing, return None.
    """
    pass

def capitalize_words(sentence: str) -> str:
    """
    Formats a sentence to Title Case.
    
    Text processing often requires normalizing or styling strings. This function
    focuses on modifying text at the word level.
    
    Goal: Capitalize the first letter of every word (e.g., "hello world" -> "Hello World").
    """
    pass

def reverse_string(s: str) -> str:
    """
    Reverses the characters in a string.
    
    String manipulation is a core skill. Reversing a sequence can be done via
    slicing or iteration.
    
    Goal: Return the string with characters in reverse order.
    """
    pass

def sum_natural_numbers(n: int) -> int:
    """
    Summation of numbers using recursion.
    
    Similar to factorial, this tests your ability to break a problem down:
    sum(n) is simply n plus the sum of all numbers before it.
    
    Goal: Return the sum of natural numbers up to n (i.e., 1 + 2 + ... + n) recursively.
    """
    pass

def add_to_set(my_set: set, item) -> set:
    """
    Modifies a set by adding a new element.
    
    Sets are unique collections. This function demonstrates how sets handle
    membership—adding a duplicate item changes nothing, while a new item grows the set.
    
    Goal: Add the item to the set and return the modified set.
    """
    pass

def find_max_number(numbers: list) -> int:
    """
    Identifies the largest value in a sequence.
    
    Finding an extreme value (smallest or biggest) requires iterating through data and
    keeping track of the "best so far".
    
    Goal: Return the biggest number found in the list.
    """
    pass
'''

# Level 2 Template
level_2_content = r'''def format_greeting(name: str, city: str) -> str:
    """
    Constructs a sentence using given variables.
    
    This simpler formatting task focuses on embedding multiple variables into a 
    single coherent sentence.
    
    Goal: Return a string "My name is {name} and I live in {city}."
    """
    pass

def get_dict_value_safe(d: dict, key: str):
    """
    Safely retrieves a value from a dictionary.
    
    Direct access (d[key]) crashes if the key is missing. Using .get() allows
    providing a default value (like None) to handle missing data gracefully.
    
    Goal: Return the value for 'key' if it exists, otherwise return "Missing".
    """
    pass

def find_passing_students(students: list) -> list:
    """
    Filters a list of dictionaries based on a numeric condition.
    
    Given a list of student dicts (e.g., [{'name': 'Ali', 'score': 50}]),
    you need to keep only those who met a threshold.
    
    Goal: Return a list of names of students with score >= 50.
    """
    pass

def recursive_power(base: int, exp: int) -> int:
    """
    Calculates base to the power of exp recursively.
    
    2^3 = 2 * 2^2.
    This helps visualize recursion as repeating a multiplication operation.
    
    Goal: Return base^exp. Base case: ANY^0 = 1.
    """
    pass

def clean_and_lowercase(text: str) -> str:
    """
    Cleans up a string input.
    
    User input often has extra spaces or inconsistent casing.
    
    Goal: Strip whitespace from both ends and convert the string to all lowercase.
    """
    pass

def create_dict_from_lists(keys: list, values: list) -> dict:
    """
    Combines two lists into a dictionary.
    
    You have a list of keys and a corresponding list of values.
    
    Goal: Return a dictionary where keys[i] maps to values[i].
    """
    pass

def count_vowels(text: str) -> int:
    """
    Counts specific characters in a string.
    
    Iterating through a string and checking each character against a target set (vowels).
    
    Goal: Return the total count of 'a', 'e', 'i', 'o', 'u' (case insensitive).
    """
    pass

def recursive_sum(numbers: list) -> int:
    """
    Sums a list of numbers using recursion.
    
    Instead of a loop, think: sum([1, 2, 3]) = 1 + sum([2, 3]).
    
    Goal: Return the sum of the list. Base case: empty list sum is 0.
    """
    pass

def get_unique_items(numbers: list) -> set:
    """
    Extracts unique elements from a list.
    
    Lists can have duplicates, Sets cannot. converting a list to a set is
    the standard way to deduplicate.
    
    Goal: Return a set containing the unique numbers from the input list.
    """
    pass

def concatenate_lists(list1: list, list2: list) -> list:
    """
    Joins two lists together.
    
    List concatenation is merging two sequences into one larger sequence.
    
    Goal: Return a new list containing all elements of list1 followed by all elements of list2.
    """
    pass
'''

# Level 3 Template
level_3_content = r'''def censor_text(text: str, forbidden_word: str) -> str:
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
'''

def reset_file(filepath, content):
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"✅ Reset: {filepath}")
    except OSError as e:
        print(f"❌ Error resetting {filepath}: {e}")

def main():
    print("--- Resetting Assessments ---")
    reset_file("level_1/assessment.py", level_1_content)
    reset_file("level_2/assessment.py", level_2_content)
    reset_file("level_3/assessment.py", level_3_content)
    print("\nAll assessments have been reset to their initial state.")

if __name__ == "__main__":
    main()