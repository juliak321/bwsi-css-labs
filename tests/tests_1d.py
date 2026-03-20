import pytest
from labs.lab_1.lab_1d import two_sum

def test_example_case():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_no_solution():
    assert two_sum([1, 2, 3], 7) == []

def test_negative_numbers():
    assert two_sum([-1, -2, -3, -6], -4) == [0, 2]
    assert two_sum([-1, -2, -3, -6], -5) == [1, 2]

def test_mixed_numbers():
    assert two_sum([-1, 2, -3, 4], 1) == [0, 1]
    assert two_sum([-2, 4, -6, 9], 3) == [2, 3]

def test_duplicate_numbers():
    assert two_sum([1, 2, 4, 2], 4) == [1, 3]
    assert two_sum([1, 2, 4, 2], 5) == [0, 2]

