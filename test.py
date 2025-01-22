# test_add_numbers.py
import pytest
from main import add

def test_positive_integers():
    assert add("1,2,3") == 6

def test_empty_string():
    assert add("") == 0

def test_delimiter_only():
    with pytest.raises(ValueError):
        add(",")

def test_different_delimiters():
    assert add("1,2\n3") == 6
    assert add("1|2\n3") == 6
    assert add("1(2)3") == 6
    assert add("1[2]3") == 6
    assert add("1{2}3") == 6
    assert add("1;2:3") == 6
    assert add("1_2_3") == 6
