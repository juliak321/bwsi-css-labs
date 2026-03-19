import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_example_case():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_empty_array():
    assert max_subarray_sum([]) == 0

def test_single_element():
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-5]) == -5

def test_all_negative():
    assert max_subarray_sum([-2,-3,-1,-5]) == -1

def test_all_positive():
    assert max_subarray_sum([2,3,1,5]) == 11

def test_mixed_numbers():
    assert max_subarray_sum([-2,3,-1,5,-3]) == 7