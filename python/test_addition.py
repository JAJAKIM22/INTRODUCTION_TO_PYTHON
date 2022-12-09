import addition
import pytest

def test_add():
    # assert True
    assert addition.add(4, 5) == 9

def test_sub():
    assert addition.sub(4, 5) == -1
    # pass

# python3 -m pytest test_addition.py::test_add