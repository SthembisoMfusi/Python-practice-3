import pytest
from level_3.assessment import *

def test_censor_text():
    assert censor_text("this is bad", "bad") == "this is ****"
    assert censor_text("hello world", "bad") == "hello world"

def test_invert_dict_unique():
    assert invert_dict_unique({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}

def test_group_words_by_length():
    words = ["a", "bb", "ccc", "dd"]
    grouped = group_words_by_length(words)
    assert set(grouped[1]) == {'a'}
    assert set(grouped[2]) == {'bb', 'dd'}
    assert set(grouped[3]) == {'ccc'}

def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(6) == 8

def test_validate_password():
    assert validate_password("password123") is True
    assert validate_password("short1") is False # Too short
    assert validate_password("password") is False # No digits

def test_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty() is True

def test_sum_matrix():
    assert sum_matrix([[1, 2], [3, 4]]) == 10
    assert sum_matrix([]) == 0

def test_recursive_nested_sum():
    assert recursive_nested_sum([1, [2, 3], 4]) == 10
    assert recursive_nested_sum([1, []]) == 1

def test_student_class():
    s = Student("Bob", [10, 20])
    assert s.name == "Bob"
    assert s.average_grade() == 15.0
    s2 = Student("Empty", [])
    assert s2.average_grade() == 0

def test_check_parentheses_simple():
    assert check_parentheses_simple("(())") is True
    assert check_parentheses_simple("(()") is False
    assert check_parentheses_simple(")(") is False
