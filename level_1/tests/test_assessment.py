import pytest
from level_1.assessment import *

def test_greeting_generator():
    assert greeting_generator("Alice", 30) == "Hello Alice, you are 30 years old!"
    assert greeting_generator("Bob", 5) == "Hello Bob, you are 5 years old!"

def test_get_first_and_last():
    assert get_first_and_last([1, 2, 3, 4]) == [1, 4]
    assert get_first_and_last(['a', 'b']) == ['a', 'b']
    assert get_first_and_last([10]) == [10, 10]
    assert get_first_and_last([]) == []

def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([1, 3, 5]) == []
    assert filter_even_numbers([2, 4, 8]) == [2, 4, 8]
    assert filter_even_numbers([]) == []

def test_factorial_recursive():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(6) == 720

def test_get_value_from_dict():
    d = {'a': 1, 'b': 2}
    assert get_value_from_dict(d, 'a') == 1
    assert get_value_from_dict(d, 'c') is None

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python practice") == "Python Practice"
    assert capitalize_words("a") == "A"
    assert capitalize_words("") == ""

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""

def test_sum_natural_numbers():
    assert sum_natural_numbers(0) == 0
    assert sum_natural_numbers(1) == 1
    assert sum_natural_numbers(5) == 15  # 5+4+3+2+1
    assert sum_natural_numbers(10) == 55

def test_add_to_set():
    s = {1, 2, 3}
    assert add_to_set(s, 4) == {1, 2, 3, 4}
    assert add_to_set(s, 1) == {1, 2, 3}

def test_find_max_number():
    assert find_max_number([1, 5, 3, 9, 2]) == 9
    assert find_max_number([-10, -5, -20]) == -5
    assert find_max_number([100]) == 100
