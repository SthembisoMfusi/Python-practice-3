import pytest
from level_2.assessment import *

def test_format_greeting():
    assert format_greeting("Alice", "Paris") == "My name is Alice and I live in Paris."
    assert format_greeting("Bob", "NY") == "My name is Bob and I live in NY."

def test_get_dict_value_safe():
    d = {'a': 1, 'b': 2}
    assert get_dict_value_safe(d, 'a') == 1
    assert get_dict_value_safe(d, 'z') == "Missing"

def test_find_passing_students():
    students = [
        {'name': 'Alice', 'score': 40},
        {'name': 'Bob', 'score': 60},
        {'name': 'Charlie', 'score': 50}
    ]
    assert find_passing_students(students) == ['Bob', 'Charlie']
    assert find_passing_students([]) == []

def test_recursive_power():
    assert recursive_power(2, 3) == 8
    assert recursive_power(5, 0) == 1
    assert recursive_power(3, 2) == 9

def test_clean_and_lowercase():
    assert clean_and_lowercase("  Hello  ") == "hello"
    assert clean_and_lowercase("PYTHON") == "python"
    assert clean_and_lowercase("   ") == ""

def test_create_dict_from_lists():
    k = ['a', 'b']
    v = [1, 2]
    assert create_dict_from_lists(k, v) == {'a': 1, 'b': 2}
    assert create_dict_from_lists([], []) == {}

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Apple") == 2
    assert count_vowels("sky") == 0

def test_recursive_sum():
    assert recursive_sum([1, 2, 3]) == 6
    assert recursive_sum([]) == 0
    assert recursive_sum([5]) == 5

def test_get_unique_items():
    assert get_unique_items([1, 2, 2, 3]) == {1, 2, 3}
    assert get_unique_items([]) == set()

def test_concatenate_lists():
    assert concatenate_lists([1, 2], [3]) == [1, 2, 3]
    assert concatenate_lists([], [1]) == [1]
