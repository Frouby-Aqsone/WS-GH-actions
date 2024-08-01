"""This module runs some unit test"""

def inc(x):
  return x + 1


def test_answer():
  """Run a unit test on the inc function"""
  assert inc(4) == 5
