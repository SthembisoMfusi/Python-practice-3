def greeting_generator(name: str, age: int) -> str:
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
