import pandas as pd

"""This module runs some unit test"""

def inc(x):
    """Increments and returns the value x

    Keyword arguments:
    x -- the number we want to increment
    """
    return x + 1


def test_answer():
    """Run a unit test on the inc function"""
    assert inc(4) == 5
