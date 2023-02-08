import pytest


def test_add():
    from add import addition
    answer = addition(0.1, 0.2)
    print(pytest.approx(0.3))
