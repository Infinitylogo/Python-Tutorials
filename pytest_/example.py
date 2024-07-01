# Example of pytest.

# def func(x):
#     return x + 1

# def test_answer():
#     assert func(3) == 5

"""
Pytest is a popular testing framework for Python. 
It allows you to write simple and scalable test cases. 
Pytest can be used for all types and levels of testing
"""

import pytest

@pytest.fixture
def _add_():
    return 5

def test_value(_add_):
    v = _add_
    assert v==5
