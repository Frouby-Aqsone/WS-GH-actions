"""This module runs some unit test"""

import pandas as pd

def inc(x):
    """Increments and returns the value x

    Keyword arguments:
    x -- the number we want to increment
    """

    df = pd.DataFrame([{'number': x}])
    df['number'] = df['number'] + 1

    new_x = df['number'].to_list()[0]

    return new_x


def test_answer():
    """Run a unit test on the inc function"""
    assert inc(4) == 5
