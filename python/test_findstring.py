import pytest
import findstring
from curses.ascii import isdigit

def test_ispresent():
    assert findstring.ispresent("AL")

def test_nodigit():
    assert findstring.nodigit("N7")