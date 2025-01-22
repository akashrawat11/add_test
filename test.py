# test_add_numbers.py
import pytest
from main import add

def test_positive_integers():
    assert add("1,2,3") == 6
