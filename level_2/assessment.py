def format_greeting(name: str, city: str) -> str:
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
